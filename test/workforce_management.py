SERVICE_ID = "SCWorkforcemanagement"
OP_ASSIGN_INCIDENT = "assignIncident"
OP_FIND_AVAILABILITY = "findAvailability"
OP_CREATE_INCIDENT_NO_ASSIGNEE = "createIncidentWithoutAssignee"

OPS = {OP_ASSIGN_INCIDENT, OP_FIND_AVAILABILITY, OP_CREATE_INCIDENT_NO_ASSIGNEE}

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
# endregion

DATA_TEMPLATE_BY_OP = {OP_FIND_AVAILABILITY: _DATA_TEMPLATE_FIND_AVAILABILITY}

RESPONSE_ATTR_CODE = "code"
RESPONSE_ATTR_MESSAGE = "message"
RESPONSE_ATTR_DATA = "data"

RESPONSE_MESSAGE_VALUE_SUCCESS = "SUCCESS"

RESPONSE_TEMPLATE_FIND_AVAILABILITY = {
    RESPONSE_ATTR_CODE: RESPONSE_MESSAGE_VALUE_SUCCESS,
    RESPONSE_ATTR_MESSAGE: "Available entries for given Zone",
    RESPONSE_ATTR_DATA: {},
}

RESPONSE_TEMPLATE_ASSIGN_INCIDENT = {
    RESPONSE_ATTR_MESSAGE: "Incident has been successfully assigned to <seat_id>",
    RESPONSE_ATTR_CODE: "SUCCESS",
}

RESPONSE_TEMPLATE_CREATE_INCIDENT = {
    RESPONSE_ATTR_MESSAGE: "not yet known",
    RESPONSE_ATTR_CODE: "SUCCESS",
}
