import os
import time
import datetime
from pprint import pformat

from SDK import utils
from .api import SCWorkforcemanagement

_LOG_LEVEL = os.getenv('LOG_LEVEL', 'debug')
LOG = utils.get_logger_for_module(__name__, _LOG_LEVEL)


class LastTaskCompletedTime:

    def __init__(self, org: str, prop_id: str, request_client: str = 'Async', human_time_fmt: str = '%Y-%m-%d %H:%M:%S(+0000)'):

        self.org = org
        self.prop_id = prop_id
        self.request_client = request_client
        self.service_client = SCWorkforcemanagement()
        self.desired_time_format = human_time_fmt

    def get_for_zone(self, pid: str, zone_id: str, duration_seconds: int = 900, unix_timestamp_end: int = None) -> dict:
        """
        Gets time of last Task completed for Zone

        :param pid: (str) ID of Building / Project
        :param zone_id: (str) ID of Zone / Installation
        :param duration_seconds: (int) Duration (in seconds) for querying Tasks.
        :param unix_timestamp_end: (int) End time (in unix timestamp) for querying Tasks.
        :return:
        """

        function_name = f'time of last task completed for Zone: {zone_id} in Building: {pid}'
        LOG.info(f'Getting {function_name}...')

        function_arguments = locals()
        LOG.debug(f'Options in function are:\n{pformat(function_name)}')

        response_data = {
            'value': None,
            'text': f'Failed to get {function_name}',
            'value_in_human_time_utc': None,
            'desired_human_time_range_utc': None
        }

        if unix_timestamp_end is None:
            LOG.info('End timestamp not given. Will use current timestamp as the end time')
            unix_timestamp_end = int(time.time())

        unix_timestamp_start = unix_timestamp_end - duration_seconds
        LOG.debug(f'{unix_timestamp_start} is timestamp {duration_seconds} before end time: {unix_timestamp_end}')

        _datetime_obj_time_end = datetime.datetime.utcfromtimestamp(unix_timestamp_end)
        time_string_end = _datetime_obj_time_end.strftime(self.desired_time_format)
        _datetime_obj_time_start = datetime.datetime.utcfromtimestamp(unix_timestamp_start)
        time_string_start = _datetime_obj_time_start.strftime(self.desired_time_format)

        time_range_text = f'{time_string_start} to {time_string_end}'
        response_data['desired_human_time_range_utc'] = time_range_text
        LOG.info(f'Time range (in UTC) for getting Tasks for Zone is:\n{time_range_text}')

        tasks_for_zone = self.service_client.get_atmost_10_tasks_for_zone_in_time_range(
            self.org, pid, self.prop_id, zone_id, unix_timestamp_start, unix_timestamp_end, self.request_client
        )

        if not tasks_for_zone:
            response_data['text'] += f' (No Tasks found in time range: {time_range_text})'
            return response_data

        no_of_tasks = len(tasks_for_zone)

        if no_of_tasks == 1:
            info_logs = ['Only 1 Task found']
            response_data['text'] += f'. Only 1 Task found'
            task_object = tasks_for_zone[0]

            # region Get Status of this Task
            _get_status_response = Task.get_status(task_object)
            _get_status_text = _get_status_response['text']

            info_logs.append(_get_status_text)

            if _get_status_response['value'] is None:
                _info_log_text = ', '.join(info_logs)
                response_data['text'] += f'. {_info_log_text}'
                LOG.info(response_data['text'])
                return response_data

            task_status = _get_status_response['value']
            # endregion

            # region Return if Task is not Completed
            if task_status != Task.StatusCompleted:
                _info_log_text = ', '.join(info_logs)
                response_data['text'] += f'. {_info_log_text}'
                LOG.info(response_data['text'])
                return response_data
            # endregion

            # region Get action end time (AEnd) of this Completed Task
            _get_aend_response = Task.get_action_end_time(task_object)
            _get_aend_text = _get_aend_response['text']

            info_logs.append(_get_aend_text)

            if _get_aend_response['value'] is None:
                _info_log_text = ', '.join(info_logs)
                response_data['text'] += f'. {_info_log_text}'
                LOG.info(response_data['text'])
                return response_data

            task_aend_timestamp = _get_aend_response['value']
            # endregion

            _datetime_obj_task_aend = datetime.datetime.utcfromtimestamp(task_aend_timestamp)
            time_string_task_and = _datetime_obj_task_aend.strftime(self.desired_time_format)

            response_data['value'] = task_aend_timestamp
            response_data['value_in_human_time_utc'] = time_string_task_and
            response_data['text'] = f'Successfully obtained value from single task in this time range.'

            return response_data

        else:
            response_data['text'] += f'. {no_of_tasks} Tasks found'
            info_logs = [f'{no_of_tasks} Tasks found']
            aend_time_of_completed_tasks = []

            LOG.debug('Looping over these tasks to get the latest action end time...')
            for index, task_object in enumerate(tasks_for_zone):

                _task_number = index + 1
                log_for_this_task = f'Task {_task_number}'

                # region Get Status of this Task
                _get_status_response = Task.get_status(task_object)
                _get_status_text = _get_status_response['text']

                log_for_this_task += f': {_get_status_text}'

                info_logs.append(log_for_this_task)

                if _get_status_response['value'] is None:
                    LOG.debug(log_for_this_task)
                    continue

                task_status = _get_status_response['value']
                # endregion

                if task_status != Task.StatusCompleted:
                    continue

                # region Get action end time (AEnd) of this Completed Task
                _get_aend_response = Task.get_action_end_time(task_object)
                _get_aend_text = _get_aend_response['text']

                log_for_this_task += f', {_get_aend_text}'
                info_logs.append(_get_aend_text)

                if _get_aend_response['value'] is None:
                    LOG.debug(log_for_this_task)
                    continue

                task_aend_timestamp = _get_aend_response['value']
                # endregion
                aend_time_of_completed_tasks.append(task_aend_timestamp)

            LOG.debug('Loop over Tasks complete.')
            LOG.debug(f'Logs for this loop are:\n{pformat(info_logs)}')

            if not aend_time_of_completed_tasks:
                response_data['text'] += ', Could not get desired data from these Tasks'
                LOG.info(response_data['text'])
                return response_data

            no_of_action_end_times = len(aend_time_of_completed_tasks)
            LOG.debug(f'action end times of {no_of_action_end_times} completed tasks in this range are:\n'
                      f'{pformat(aend_time_of_completed_tasks)}')

            # Compare aend timestamps, whichver greater is desired value
            latest_aend_time = max(aend_time_of_completed_tasks)
            LOG.debug(f'Latest action end time of these are: {latest_aend_time}')

            response_data['value'] = latest_aend_time

            _latest_task_aend_datetime_obj = datetime.datetime.utcfromtimestamp(latest_aend_time)
            latest_task_aend_time_string = _latest_task_aend_datetime_obj.strftime(self.desired_time_format)
            response_data['value_in_human_time_utc'] = latest_task_aend_time_string
            response_data['text'] = 'Successfully obtained value from latest completed Task in this time range.'
            return response_data


class Task:

    AttrNameStatus = 'Status'
    AttrNameActionEndTime = 'AEnd'

    StatusCompleted = 'COMPLETED'
    StatusAssigned = 'PENDING'
    StatusIncomplete = 'INCOMPLETE'

    @classmethod
    def get_status(cls, task: dict) -> dict:

        attr_name_status = cls.AttrNameStatus

        data_return = {
            'value': None,
            'text': f'Could not get {attr_name_status} from this Task'
        }

        if attr_name_status not in task:
            data_return['text'] += f' (attribute: {attr_name_status} missing)'
            LOG.debug(data_return['text'])
            return data_return

        task_status = task[attr_name_status]

        _type_status = type(task_status)

        if _type_status != str:
            data_return['text'] += f' (Value of {attr_name_status} in Task must be a string,' \
                                   f' but found type: {str(_type_status)}).'
            LOG.debug(data_return['text'])
            return data_return

        status_text_zone_task_status = f'"{attr_name_status}" in this Task is: {task_status})'
        LOG.debug(status_text_zone_task_status)

        data_return['value'] = task_status
        data_return['text'] = status_text_zone_task_status

        return data_return

    @classmethod
    def get_action_end_time(cls, task: dict) -> dict:

        attr_name_action_end_time = cls.AttrNameActionEndTime

        data_return = {
            'value': None,
            'text': f'Could not get {attr_name_action_end_time} from this Task'
        }

        if attr_name_action_end_time not in task:
            data_return['text'] += f' (attribute: {attr_name_action_end_time} missing)'
            LOG.debug(data_return['text'])
            return data_return

        action_end_time = task[attr_name_action_end_time]

        _type_action_end_time = type(action_end_time)

        if _type_action_end_time != int:
            data_return['text'] += f' (Value of {attr_name_action_end_time} in Task must be integer (unix timestamp),' \
                                   f' but found type: {str(_type_action_end_time)}).'
            LOG.debug(data_return['text'])
            return data_return

        status_text_action_end_time = f'"{attr_name_action_end_time}" in this Task is: {action_end_time})'
        LOG.debug(status_text_action_end_time)

        data_return['value'] = action_end_time
        data_return['text'] = status_text_action_end_time

        return data_return
