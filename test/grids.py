SERVICE_ID = 'SCGrids'
OP_READ_ZONE = 'readZone'
OP_READ_BUILDING = 'readBuilding'
OP_READ_PROPERTY = 'readProperty'
OPS = {
    OP_READ_ZONE,
    OP_READ_BUILDING,
    OP_READ_PROPERTY
}

# region Data Template for each Op
_DATA_TEMPLATE_READ_ZONE = {
    "OrgId": str(),
    "PropId": str(),
    "PID": str(),
    "LID": str(),
    "InsID": str(),
    "BeaconID": "N.A.",
    "ZoneCategoryID": str(),
    "Name": str(),
    "Area": 200,
    "FloorType": str(),
    "Status": 'Active',
    "OperatingHours": dict(),
    "IsBuildingOperatingHours": False,
}

_DATA_TEMPLATE_READ_BUILDING = {}

_DATA_TEMPLATE_READ_PROPERTY = {}
# endregion

DATA_TEMPLATE_BY_OP = {
    OP_READ_ZONE: _DATA_TEMPLATE_READ_ZONE,
    OP_READ_BUILDING: _DATA_TEMPLATE_READ_BUILDING,
    OP_READ_PROPERTY: _DATA_TEMPLATE_READ_PROPERTY
}

TEST_ZONE_CATEGORY_MEETING_ROOMS = 'MEETING_ROOMS'

TEST_OPERATING_HOURS_SET_1 = {
    "0": [
        {"End": "0000", "Start": "0000"}
    ],
    "1": [
        {"End": "1700", "Start": "0900"}
    ],
    "2": [
        {"End": "2000", "Start": "0900"}
    ],
    "3": [
        {"End": "1700", "Start": "0800"}
    ],
    "4": [
        {"End": "1700", "Start": "0900"}
    ],
    "5": [
        {"End": "1700", "Start": "1700"}
    ],
    "6": [
        {"End": "1800", "Start": "0700"}
    ]
}

SDK_ASYNC_CLIENT_ATTR_STATUS_CODE = 'status'
SDK_ASYNC_CLIENT_ATTR_MESSAGE = 'message'
SDK_ASYNC_CLIENT_ATTR_DATA = 'data'

RESPONSE_TEMPLATE_GRIDS = {
    SDK_ASYNC_CLIENT_ATTR_STATUS_CODE: 200,
    SDK_ASYNC_CLIENT_ATTR_MESSAGE: "Success",
    SDK_ASYNC_CLIENT_ATTR_DATA: {}
}
