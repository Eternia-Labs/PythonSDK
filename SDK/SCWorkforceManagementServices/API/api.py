import datetime
import os
import time
import json
from pprint import pformat
from urllib.request import urlopen

import mock
from SDK import utils
from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync


_LOG_LEVEL = os.getenv('LOG_LEVEL', 'debug')
LOG = utils.get_logger_for_module(__name__, 'debug')
HOST = "SC_WORKFORCEMANAGEMENT_HOST"
PROTOCOL = "SC_WORKFORCEMANAGEMENT_HTTP_PROTOCOL"
PORT = "SC_WORKFORCEMANAGEMENT_PORT"
MOCK_RESPONSES = os.getenv('MOCK_RESPONSES', '0')
# region Names of ops in service
OP_ASSIGN_INCIDENT = 'scteams.assignIncident'
OP_CREATE_INCIDENT_NO_ASSIGNEE = 'scteams.createIncidentWithoutAssignee'
OP_FIND_AVAILABILITY_FOR_INCIDENT = 'scteams.findAvailabilityForIncident-v2'
OP_GET_INCIDENT_SETTINGS = 'scteams.getIncidentsSettings'
OP_GET_TASKS_FOR_ZONE_IN_TIME_RANGE = 'scteams.getLastNTasks'
OP_GET_TASK_GROUP_IN_TIME_RANGE = 'scteams.getTaskGroupInTRangeForID'
OP_GET_SHIFT_LATENESS_METRICS_FOR_BUILDING = 'scteams.getShiftLatenessMetricsForBuilding'

OPS = {
    OP_ASSIGN_INCIDENT,
    OP_CREATE_INCIDENT_NO_ASSIGNEE,
    OP_FIND_AVAILABILITY_FOR_INCIDENT,
    OP_GET_INCIDENT_SETTINGS,
    OP_GET_TASKS_FOR_ZONE_IN_TIME_RANGE,
    OP_GET_TASK_GROUP_IN_TIME_RANGE,
    OP_GET_SHIFT_LATENESS_METRICS_FOR_BUILDING
}
# endregion

HTTP_METHOD_POST = 'POST'


# TODO:
#  1. Add doc string for each function (init and initialize remaining)
#  2. Standardize the response format and indicate the type in function signature.


class SCWorkforcemanagement:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/scworkforcemanagement"
                print("SCWORKFORCEMANAGEMENT: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCWORKFORCEMANAGEMENT: protocol env variable is not set")

            url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            apiversion = data_json["modules"]["scworkforcemanagement"]["version"]

            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="scworkforcemanagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="scworkforcemanagement"
                )
            else:
                print("SCWORKFORCEMANAGEMENT: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="scworkforcemanagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="scworkforcemanagement"
                )
        except Exception as e:
            print("Exception " + str(e))

    def createIncidentWithoutAssignee(self, org: str, pid: str, propid: str, expJson: str, client=None):
        """
        Creates an Incident for a Zone (without any assignee)

        :param org: Organisation ID
        :param pid: Building / Project ID
        :param propid: Property ID
        :param expJson: Expected request body (as a JSON string)
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        op = OP_CREATE_INCIDENT_NO_ASSIGNEE
        mock_response = MOCK_RESPONSES
        print(f"Preparing request for op: {op}...")

        _function_args = locals()
        print(f"Options given are: \n{pformat(_function_args)}")

        if mock_response == '1':
            return {
                'code': 'failure',
                'message': f'Mock response not available for op: {op}'
            }

        request_kwargs = {
            "httpmethod": HTTP_METHOD_POST,
            "op": op,
            "org": org,
            "propid": propid,
            "pid": pid,
            "body": json.loads(expJson),
        }

        print(f'Options for request client ({client}) created as:\n{pformat(request_kwargs)}')

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        return _client_obj.makeRequest(**request_kwargs)

    def getTaskGroupInTRangeForID(self, org: str, pid: str, propid: str = None, expJson: str = "{}", client=None):
        """
        Get task group in time range for ID

        :param org: Organisation ID
        :param pid: Building / Project ID
        :param propid: Property ID
        :param expJson: Expected request body (as a JSON string)
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        op = OP_GET_TASK_GROUP_IN_TIME_RANGE
        mock_response = MOCK_RESPONSES
        print(f"Preparing request for op: {op}...")

        _function_args = locals()
        print(f"Options given are: \n{pformat(_function_args)}")

        if mock_response == '1':
            return {
                'code': 'failure',
                'message': f'Mock response not available for op: {op}'
            }

        request_kwargs = {
            "httpmethod": HTTP_METHOD_POST,
            "op": op,
            "org": org,
            "propid": propid,
            "pid": pid,
            "body": json.loads(expJson),
        }

        print(f'Options for request client ({client}) created as:\n{pformat(request_kwargs)}')

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        return _client_obj.makeRequest(**request_kwargs)

    def getShiftLatenessMetricsForBuilding(self, org: str, pid: str, propid: str, expJson: str, client=None):
        """

        Get shift lateness metrics for building

        :param org: Organisation ID
        :param pid: Building / Project ID
        :param propid: Property ID
        :param expJson: Expected request body (as a JSON string)
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        op = OP_GET_SHIFT_LATENESS_METRICS_FOR_BUILDING
        mock_response = MOCK_RESPONSES
        print(f"Preparing request for op: {op}...")

        _function_args = locals()
        print(f"Options given are: \n{pformat(_function_args)}")

        if mock_response == '1':
            return {
                'code': 'failure',
                'message': f'Mock response not available for op: {op}'
            }

        request_kwargs = {
            "httpmethod": HTTP_METHOD_POST,
            "op": op,
            "org": org,
            "propid": propid,
            "pid": pid,
            "body": json.loads(expJson),
        }

        print(f'Options for request client ({client}) created as:\n{pformat(request_kwargs)}')

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        return _client_obj.makeRequest(**request_kwargs)

    def find_availability_for_incident(self, org: str, pid: str, propid: str, expJson: str, client=None) -> any:
        """
        This returns availability response for incident

        :param org: Organisation ID
        :param pid: Building / Project ID
        :param propid: Property ID
        :param expJson: Expected request body (as a JSON string)
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        op = OP_FIND_AVAILABILITY_FOR_INCIDENT
        mock_response = MOCK_RESPONSES
        print(f"Preparing request for op: {op}...")

        _function_args = locals()
        print(f"Options given are: \n{pformat(_function_args)}")

        if mock_response == '1':
            return {
                'code': 'failure',
                'message': f'Mock response not available for op: {op}'
            }

        request_kwargs = {
            "httpmethod": HTTP_METHOD_POST,
            "op": op,
            "org": org,
            "propid": propid,
            "pid": pid,
            "body": json.loads(expJson),
        }

        print(f'Options for request client ({client}) created as:\n{pformat(request_kwargs)}')

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        return _client_obj.makeRequest(**request_kwargs)

    def assign_shift_to_incident(self, org: str, pid: str, propid: str, expJson: str, client=None) -> any:
        """
        This assigns an Incident for a Zone to an assignee.

        Incident identified by "IncidentID" inside expJson (Expected request body, serialized to a JSON string)
        Zone identified by "zoneId" inside expJson
        Assignee identified by "ShiftID" and "SeatId" inside expJson

        :param org: Organisation ID
        :param pid: Project ID
        :param propid: Property ID
        :param expJson: Expected request body (as a JSON string)
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        op = OP_ASSIGN_INCIDENT
        mock_response = MOCK_RESPONSES
        print(f"Preparing request for op: {op}...")

        _function_args = locals()
        print(f"Options given are: \n{pformat(_function_args)}")

        if mock_response == '1':
            return {
                'code': 'failure',
                'message': f'Mock response not available for op: {op}'
            }

        request_kwargs = {
            "httpmethod": HTTP_METHOD_POST,
            "op": op,
            "org": org,
            "propid": propid,
            "pid": pid,
            "body": json.loads(expJson),
        }

        print(f'Options for request client ({client}) created as:\n{pformat(request_kwargs)}')

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        return _client_obj.makeRequest(**request_kwargs)

    def get_incident_settings(self, org: str, pid: str, propid: str, client=None):
        """
        Get incident settings for Building (pid)

        :param org: Organisation ID
        :param pid: Project ID
        :param propid: Property ID
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        op = OP_GET_INCIDENT_SETTINGS
        mock_response = MOCK_RESPONSES
        print(f"Preparing request for op: {op}...")

        _function_args = locals()
        print(f"Options given are: \n{pformat(_function_args)}")

        if mock_response == '1':
            return {
                'code': 'failure',
                'message': f'Mock response not available for op: {op}'
            }

        request_kwargs = {
            "httpmethod": HTTP_METHOD_POST,
            "op": op,
            "org": org,
            "propid": propid,
            "pid": pid
        }

        print(f'Options for request client ({client}) created as:\n{pformat(request_kwargs)}')

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        return _client_obj.makeRequest(**request_kwargs)

    def get_atmost_10_tasks_for_zone_in_time_range(self, org, pid, propid, zone_id: str, unix_time_start: int, unix_time_end: int, client=None):
        """
        Get at most 10 Tasks for Zone in the given time range.

        :param org: (str) Organization ID
        :param pid: (str) Project (Building) ID
        :param propid: (str) Property ID
        :param zone_id: (str) Zone ID
        :param unix_time_end: (int) Start time of the query (unix timestamp)
        :param unix_time_start: (int) End time of the query (unix timestamp)
        :param client: (str) "Sync" or "Async" (default)
        :return: Response of request via SDK
        """

        op = OP_GET_TASKS_FOR_ZONE_IN_TIME_RANGE
        mock_response = MOCK_RESPONSES
        print(f"Preparing request for op: {op}...")

        _function_args = locals()
        print(f"Options given are: \n{pformat(_function_args)}")

        if mock_response == '1':
            return mock.get_tasks_for_zone_in_time_range(
                zone_id,
                unix_time_start,
                unix_time_end,
                task_complete_time=unix_time_end - 5,
                client=client
            )

        request_body = {
            "TasksFor": "ZONE",
            "zoneId": zone_id,
            "StartTime": unix_time_start,
            "EndTime": unix_time_end,
            "Limit": 10
        }

        request_kwargs = {
            "httpmethod": "POST",
            "op": op,
            "propid": propid,
            "org": org,
            "pid": pid,
            "body": json.dumps(request_body),
        }

        print(f'Options for request client ({client}) created as:\n{pformat(request_kwargs)}')

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        return _client_obj.makeRequest(**request_kwargs)


class Util:
    SCWorkforcemanagement = SCWorkforcemanagement()

    @classmethod
    def get_time_last_task_completed_for_zone(cls, org: str, propid: str, pid: str, zone_id: str, duration_seconds: int = 900, unix_time_end: int = None, client: str = None):
        """
        Gets time of last Task completed for Zone

        :param org:
        :param propid:
        :param pid:
        :param zone_id:
        :param duration_seconds:
        :param unix_time_end:
        :return:
        """

        function_name = f'time of last task completed for Zone: {zone_id} in PID: {pid}'
        print(f'Getting {function_name}...')

        function_arguments = locals()
        print(f'Options in function are:\n{pformat(function_name)}')

        response_data = {
            'value': None,
            'text': f'Failed to get {function_name}'
        }

        if unix_time_end is None:
            print('end_time not given. Will use current timestamp as the end time')
            unix_time_end = int(time.time())

        unix_time_start = unix_time_end - duration_seconds
        print(f'{unix_time_start} is timestamp {duration_seconds} before end time: {unix_time_end}')

        _datetime_obj_time_end = datetime.datetime.utcfromtimestamp(unix_time_end)
        time_string_end = _datetime_obj_time_end.strftime('%Y-%m-%d %H:%M:%S(+0000)')
        _datetime_obj_time_start = datetime.datetime.utcfromtimestamp(unix_time_start)
        time_string_start = _datetime_obj_time_start.strftime('%Y-%m-%d %H:%M:%S(+0000)')

        time_range_text = f'{time_string_start} to {time_string_end}'
        print(f'Time range (in UTC) for getting Tasks for Zone is:\n{time_range_text}')

        if client is None:
            print('client not given. Using default client: Async')
            client = 'Async'

        tasks_for_zone = cls.SCWorkforcemanagement.get_atmost_10_tasks_for_zone_in_time_range(
            org, pid, propid, zone_id, unix_time_start, unix_time_end, client
        )

        if not tasks_for_zone:
            response_data['text'] += f' (No Tasks found in time range: {time_range_text})'
            return response_data

        no_of_tasks = len(tasks_for_zone)

        if no_of_tasks == 1:
            task = tasks_for_zone[0]
        else:
            ...

        # Process the tasks for Zone based on how handled in workordermgmt
        # Iterate over,
        # find latest completed task and get its AEnd
        # Custom logic required to check which is the latest completed task (if more than 1 completed found)

    @classmethod
    def get_last_clean_time_for_building(cls):
        ...


def _check_to_block_incident_due_to_task(task: dict, current_unix_time: int, seconds_to_block: int) -> dict:

    status_text_check_negative = 'No need to block incident due to this Task for Zone'
    status_text_check_positive = 'Block incident due to this Task for Zone'

    data_return = {
        'status': False,
        'text': status_text_check_negative
    }

    LOG.debug(f'Checking whether to {status_text_check_positive}...')

    # region 1. Extract "Status" from Task (Check negative if not found)
    attr_name_status = 'Status'

    if attr_name_status not in task:
        data_return['text'] += f' ({attr_name_status} missing)'
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

    # endregion

    # region 2. Ignore If Status is not STARTED or not COMPLETED - Check negative
    status_values_to_consider = {
        'STARTED',
        'COMPLETED'
    }
    if task_status not in status_values_to_consider:
        data_return['text'] += f' ("{attr_name_status} in this Task is neither of: {status_values_to_consider}")'
        LOG.debug(data_return['text'])
        return data_return

    LOG.debug(status_text_zone_task_status)

    # endregion

    # region 3(a) If Status is STARTED (Check positive)
    if task_status == 'STARTED':
        data_return['status'] = True
        data_return['text'] = f'{status_text_check_positive} ({status_text_zone_task_status})\n' \
                              f'Rule: Block Alerts for Zone when previous Task for Zone has status STARTED.'
        LOG.debug(data_return['text'])
        return data_return
    # endregion

    # region 3(b) If Status is COMPLETED (Check time elapsed since Task completed)

    # region 3(b)(i) Get time elapsed since Task completed

    # region Extract action end time from Task (Check negative if invalid)
    attr_name_action_end_time = 'AEnd'

    if attr_name_action_end_time not in task:
        data_return['text'] += f' ("{attr_name_action_end_time}" missing in Task)'
        LOG.debug(data_return['text'])
        return data_return

    task_action_end_time = task[attr_name_action_end_time]

    _type_action_end_time = type(task_action_end_time)

    if _type_action_end_time != int:
        data_return['text'] += f' (Value of {attr_name_action_end_time} in Task must be' \
                               f' integer. Found type: {str(_type_action_end_time)})'
        LOG.debug(data_return['text'])
        return data_return

    status_text_task_action_end_time = f'"{attr_name_action_end_time}" in this Task' \
                                       f' is: {task_action_end_time}'

    LOG.debug(status_text_task_action_end_time)
    # endregion

    seconds_since_task_completed = current_unix_time - task_action_end_time

    status_text_time_since_task_complete = f'Task completed {seconds_since_task_completed} seconds before'
    LOG.debug(status_text_time_since_task_complete)
    # endregion

    # region 3(b)(ii) Negative if time since Task completed more than given duration, Positive otherwise
    if seconds_since_task_completed > seconds_to_block:
        data_return['text'] += f' ({status_text_time_since_task_complete}. Duration to' \
                               f' block incidents after Task complete,' \
                               f' {seconds_to_block} seconds already over)'
        LOG.debug(data_return['text'])
        return data_return
    else:
        data_return['status'] = True
        data_return['text'] = f'{status_text_check_positive} ({status_text_time_since_task_complete}.' \
                              f'\nRule: Block incident for {seconds_to_block}' \
                              f' seconds after Task for Zone is completed.'
        LOG.debug(data_return['text'])
        return data_return
    # endregion

    # endregion
