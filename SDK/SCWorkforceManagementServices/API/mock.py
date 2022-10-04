import json
import datetime


# This will use the default test scenario to create mock data (unless updated)
def get_tasks_for_zone_in_time_range(zone_id: str, start_time: int, end_time: int, task_complete_time: int, client: str):

    _msg_time_dt_start = datetime.datetime.utcfromtimestamp(start_time)
    message_time_str_start = _msg_time_dt_start.strftime('%Y-%m-%d %H:%M:%S(+0000)')

    _msg_time_dt_end = datetime.datetime.utcfromtimestamp(end_time)
    message_time_str_end = _msg_time_dt_end.strftime('%Y-%m-%d %H:%M:%S(+0000)')

    data = create_tasks_end_with_complete(start_time, end_time, task_complete_time)

    if client == 'Async':
        return {
            'code': 'SUCCESS',
            'message': f"Successfully retrieved requested items in time range[UTC] {message_time_str_start} to "
                       f"{message_time_str_end} for ZONE: {zone_id}.",
            'data': data
        }
    else:
        data_json_str = json.dumps(data)
        return MockHTTPResponse(data_json_str, 200)



# region Utils for Task

# Scenarios for mocking the task states.
# Eg scenarios:
# 1. only_unpublished_tasks
# 2. only_incomplete_tasks
# 3. at_least_1_started_task
# 4. at_least_1_completed_task (with aend)
# No other scenarios need to be tested as those are not possible by virtue of the system design.
#  Eg of impossible scenario: 1 task with status "PENDING" - not possible as the alert block duration feature
#  will not even let the program control come to this check (this means if a work order created in past X mins,
#  then dont create this work order)

def create_tasks_end_with_complete(start_time: int, end_time: int, task_complete_time: int) -> list:

    return [
        _get_mock_task('UNPUBLISHED'),
        _get_mock_task('ASSIGNED'),
        _get_mock_task('STARTED'),
        _get_mock_task('COMPLETED', task_complete_time)
    ]


def create_tasks_end_with_incomplete():

    return [
        _get_mock_task('UNPUBLISHED'),
        _get_mock_task('ASSIGNED'),
        _get_mock_task('STARTED'),
        _get_mock_task('INCOMPLETE')
    ]


def create_tasks_end_with_started():

    return [
        _get_mock_task('UNPUBLISHED'),
        _get_mock_task('ASSIGNED'),
        _get_mock_task('STARTED')
    ]


def create_tasks_end_with_assigned():

    return [
        _get_mock_task('UNPUBLISHED'),
        _get_mock_task('ASSIGNED')
    ]


def _get_mock_task(status: str, aend_time: int = None) -> dict:

    return {
        "PropID": "<Property ID>",
        "SeatId": "<Seat ID>",
        "ShiftId": "<Shift ID>",
        "Status": status,
        "taskCount": 1,
        "ZoneName": "<Zone Name>",
        "Delayed": False,
        "ZoneCatId": "<Zone Category ID>",
        "ATTR": "attr#<Building ID>#<Property ID>#<Shift ID>#<Task ID>",
        "AEnd": aend_time,
        "Start": 1656923219,
        "TaskId": "<Task ID>",
        "By": "<Incident Type / Source>",
        "End": 1656924119,
        "Type": "<TASK / INCIDENT>",
        "Zone": "<Zone ID>",
        "ID": "<Building ID>",
        "Name": "<Incident Name>",
        "Priority": "<Incident Priority>"
    }
# endregion


# region Data Template for each Op
_DATA_TEMPLATE_FIND_AVAILABILITY = {
    "Seat1": [
        {
            "ShiftID": "6bdbe62e-4ab1-4750-8318-503a10175fb4",
            "ZoneName": None,
            "SameZone": False,
            "Status": "PUBLISHED",
            "StartTime": 1621306800,
            "ZoneID": None,
        }
    ],
    "Seat2": [
        {
            "ShiftID": "6e2991d7-7405-4ab3-9f45-4c96575be064",
            "ZoneName": "Meeting Room",
            "SameZone": True,
            "Status": "PUBLISHED",
            "StartTime": 1621299600,
            "ZoneID": "ZoneId1",
        },
        {
            "ShiftID": "6e2991d7-7405-4ab3-9f45-4c96575be064",
            "ZoneName": "Meeting Room",
            "SameZone": True,
            "Status": "PUBLISHED",
            "StartTime": 1621317600,
            "ZoneID": "ZoneId1",
        },
    ],
}

_DATA_TEMPLATE_CREATE_INCIDENT_NO_ASSIGNEE = {}

_DATA_TEMPLATE_GET_INCIDENT_SETTINGS = {
    "IncidentSettings": {
        "AUTO_ASSIGN_INCIDENTS": {
            "BooleanValue": True,
            "Description": "If this setting is true, when an incident is raised for a zone, the system will try to auto assign the incident to an available shift and do a round robin balancing of number of incidents between such availabilities. Set this to false if you want all the allocated shifts for the zone to receive notification about an incident, followed by a single person's acknowledgement and incident resolution subsequently.",
            "Type": "Boolean"
        },
        "INCIDENT_HIGH_TIMEOUT": {
            "LongValue": 900,
            "Description": "Allowed elapsed time in seconds from due time by which an incident must be acted on (started or completed) for high priority incidents.",
            "Type": "Long"
        },
        "INCIDENT_LOW_TIMEOUT": {
            "LongValue": 3600,
            "Description": "Allowed elapsed time in seconds from due time by which an incident must be acted on (started or completed) for low priority incidents.",
            "Type": "Long"
        },
        "INCIDENT_NORMAL_TIMEOUT": {
            "LongValue": 1800,
            "Description": "Allowed elapsed time in seconds from due time by which an incident must be acted on (started or completed) for normal priority incidents.",
            "Type": "Long"
        },
        "INCIDENT_MEDIUM_TIMEOUT": {
            "LongValue": 1200,
            "Description": "Allowed elapsed time in seconds from due time by which an incident must be acted on (started or completed) for medium priority incidents.",
            "Type": "Long"
        }
    },
    "ATTR": "attr#incidents#<pid>",
    "ID": "<pid>"
}

_DATA_TEMPLATE_GET_LAST_TASK_FOR_ZONE_IN_TIME_RANGE = [
    {
        "PropID": "<Property ID>",
        "SeatId": "<Seat ID>",
        "ShiftId": "<Shift ID>",
        "Status": "<STARTED / INCOMPLETE>",
        "taskCount": 1,
        "ZoneName": "<Zone Name>",
        "Delayed": False,
        "ZoneCatId": "<Zone Category ID>",
        "ATTR": "attr#<Building ID>#<Property ID>#<Shift ID>#<Task ID>",
        "AEnd": 1656928526,
        "Start": 1656923219,
        "TaskId": "<Task ID>",
        "By": "<Incident Type / Source>",
        "End": 1656924119,
        "Type": "<TASK / INCIDENT>",
        "Zone": "<Zone ID>",
        "ID": "<Building ID>",
        "Name": "<Incident Name>",
        "Priority": "<Incident Priority>"
    }
]

_DATA_TEMPLATE_GET_TASKS_FOR_ZONE_IN_TIME_RANGE = [
    {
        "PropID": "<Property ID>",
        "SeatId": "<Seat ID>",
        "ShiftId": "<Shift ID>",
        "Status": "<STARTED / INCOMPLETE>",
        "taskCount": 1,
        "ZoneName": "<Zone Name>",
        "Delayed": False,
        "ZoneCatId": "<Zone Category ID>",
        "ATTR": "attr#<Building ID>#<Property ID>#<Shift ID>#<Task ID>",
        "AEnd": 1656928526,
        "Start": 1656923219,
        "TaskId": "<Task ID>",
        "By": "<Incident Type / Source>",
        "End": 1656924119,
        "Type": "<TASK / INCIDENT>",
        "Zone": "<Zone ID>",
        "ID": "<Building ID>",
        "Name": "<Incident Name>",
        "Priority": "<Incident Priority>"
    }
]
# endregion

# DATA_TEMPLATE_BY_OP = {
#     API.OP_FIND_AVAILABILITY_FOR_INCIDENT: _DATA_TEMPLATE_FIND_AVAILABILITY,
#     API.OP_GET_INCIDENT_SETTINGS: _DATA_TEMPLATE_GET_INCIDENT_SETTINGS,
#     API.OP_GET_TASKS_FOR_ZONE_IN_TIME_RANGE: _DATA_TEMPLATE_GET_LAST_TASK_FOR_ZONE_IN_TIME_RANGE,
# }

RESPONSE_ATTR_CODE = 'code'
RESPONSE_ATTR_MESSAGE = 'message'
RESPONSE_ATTR_DATA = 'data'

RESPONSE_MESSAGE_VALUE_SUCCESS = 'SUCCESS'

RESPONSE_TEMPLATE_FIND_AVAILABILITY = {
    RESPONSE_ATTR_CODE: RESPONSE_MESSAGE_VALUE_SUCCESS,
    RESPONSE_ATTR_MESSAGE: 'Available entries for given Zone',
    RESPONSE_ATTR_DATA: {}
}

RESPONSE_TEMPLATE_ASSIGN_INCIDENT = {
    RESPONSE_ATTR_MESSAGE: "Incident has been successfully assigned to <seat_id>",
    RESPONSE_ATTR_CODE: "SUCCESS"
}

RESPONSE_TEMPLATE_CREATE_INCIDENT = {
    RESPONSE_ATTR_MESSAGE: "not yet known",
    RESPONSE_ATTR_CODE: "SUCCESS"
}

RESPONSE_TEMPLATE_GET_INCIDENT_SETTINGS = {
    RESPONSE_ATTR_CODE: RESPONSE_MESSAGE_VALUE_SUCCESS,
    RESPONSE_ATTR_MESSAGE: "Settings retrieved successfully",
    RESPONSE_ATTR_DATA: {}
}

RESPONSE_TEMPLATE_GET_TASKS_FOR_ZONE_IN_TIME_RANGE = {
    RESPONSE_ATTR_CODE: RESPONSE_MESSAGE_VALUE_SUCCESS,
    RESPONSE_ATTR_MESSAGE: "Successfully retrieved requested items in time range[UTC] YYYY-MM-DD HH:MM:SS(+0000)"
                           " to YYYY-MM-DD HH:MM:SS(+0000) for ZONE: <Zone ID>.",
    RESPONSE_ATTR_DATA: []
}


class MockHTTPResponse:

    def __init__(self, json_data: str, status_code: int):

        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


# def create_response_for_op(op: str, client: str = 'Async') -> dict:
#
#     print(f'Creating Mock response for op: {op}')
#
#     data_return = {
#         'response': None,
#         'text': 'default'
#     }
#
#     _data_template = None
#     # region Get Data Template for Op (if defined)
#     if op in DATA_TEMPLATE_BY_OP:
#         _status_text = f'Data template defined for op: {op}'
#         print(_status_text)
#         _data_template = DATA_TEMPLATE_BY_OP[op]
#     # endregion
#
#     # region Get Response Template (updated with data) based on Client Type
#
#     if client == 'Async':
#         # region Get Response Template based on Op
#         if op == API.OP_CREATE_INCIDENT_NO_ASSIGNEE:
#             _response_template = RESPONSE_TEMPLATE_CREATE_INCIDENT
#         elif op == API.OP_FIND_AVAILABILITY_FOR_INCIDENT:
#             _response_template = RESPONSE_TEMPLATE_FIND_AVAILABILITY
#         elif op == API.OP_GET_INCIDENT_SETTINGS:
#             _response_template = RESPONSE_TEMPLATE_GET_INCIDENT_SETTINGS
#         else:
#             _response_template = RESPONSE_TEMPLATE_GET_TASKS_FOR_ZONE_IN_TIME_RANGE
#         # endregion
#         if _data_template is not None:
#             _response_template[RESPONSE_ATTR_DATA] = _data_template
#     else:
#         if _data_template is None:
#             data = None
#         else:
#             data = json.dumps(_data_template)
#
#         _response_template = MockHTTPResponse(data, 200)
#     # endregion
#
#     data_return['response'] = _response_template
#     data_return['text'] = 'Created Response Template'
#     return data_return
