SERVICE_ID = 'SCWorkforcemanagement'
OP_ASSIGN_INCIDENT = 'assignIncident'
OP_FIND_AVAILABILITY = 'findAvailability'
OP_CREATE_INCIDENT_NO_ASSIGNEE = 'createIncidentWithoutAssignee'
OP_GET_INCIDENT_SETTINGS = 'getIncidentsSettings'
OP_GET_LAST_TASK_FOR_ZONE_IN_TIME_RANGE = 'getLastTaskForZoneInTimeRange'

OPS = {
    OP_ASSIGN_INCIDENT,
    OP_FIND_AVAILABILITY,
    OP_CREATE_INCIDENT_NO_ASSIGNEE,
    OP_GET_INCIDENT_SETTINGS,
    OP_GET_LAST_TASK_FOR_ZONE_IN_TIME_RANGE
}

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
# endregion

DATA_TEMPLATE_BY_OP = {
    OP_FIND_AVAILABILITY: _DATA_TEMPLATE_FIND_AVAILABILITY,
    OP_GET_INCIDENT_SETTINGS: _DATA_TEMPLATE_GET_INCIDENT_SETTINGS,
    OP_GET_LAST_TASK_FOR_ZONE_IN_TIME_RANGE: _DATA_TEMPLATE_GET_LAST_TASK_FOR_ZONE_IN_TIME_RANGE
}

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

RESPONSE_TEMPLATE_GET_LAST_TASK_FOR_ZONE_IN_TIME_RANGE = {
    RESPONSE_ATTR_CODE: RESPONSE_MESSAGE_VALUE_SUCCESS,
    RESPONSE_ATTR_MESSAGE: "Successfully retrieved requested items in time range[UTC] YYYY-MM-DD HH:MM:SS(+0000)"
                           " to YYYY-MM-DD HH:MM:SS(+0000) for ZONE: <Zone ID>.",
    RESPONSE_ATTR_DATA: []
}
