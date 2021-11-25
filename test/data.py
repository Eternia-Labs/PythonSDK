import json

import test
from test import settings


GRIDS_OP_GET_ZONE_INFO = test.GRIDS_OP_GET_ZONE_INFO
GRIDS_OP_GET_BUILDING_INFO = test.GRIDS_OP_GET_BUILDING_INFO


_SDK_ASYNC_CLIENT_ATTR_STATUS_CODE = 'status'
_SDK_ASYNC_CLIENT_ATTR_MESSAGE = 'message'
_SDK_ASYNC_CLIENT_ATTR_DATA = 'data'

_SDK_ASYNC_CLIENT_MESSAGE_VALUE_SUCCESS = 'Success'

_SDK_ASYNC_CLIENT_RESPONSE_TEMPLATE = {
    _SDK_ASYNC_CLIENT_ATTR_STATUS_CODE: 200,
    _SDK_ASYNC_CLIENT_ATTR_MESSAGE: "Success",
    _SDK_ASYNC_CLIENT_ATTR_DATA: {}
}

_TEST_ZONE_CATEGORY_MEETING_ROOMS = 'MEETING_ROOMS'

_TEST_OPERATING_HOURS_SET_1 = {
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


class MockHTTPResponse:

    def __init__(self, json_data: str, status_code: int):

        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class MatrixGrids:

    def __init__(self, client: str):

        self.sdk_client = client
        self._data_template_read_zone = _DATA_TEMPLATE_READ_ZONE
        self._data_template_read_building = _DATA_TEMPLATE_READ_BUILDING
        self.ops = {
            GRIDS_OP_GET_ZONE_INFO,
            GRIDS_OP_GET_BUILDING_INFO
        }

    def create_response_for_op(self, op: str) -> dict:

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.ops:
            data_return['text'] = f'Given op: {op} does not have a test response available.'
            return data_return

        # region Get Data Template for Op
        if op == GRIDS_OP_GET_ZONE_INFO:
            _data_template = _DATA_TEMPLATE_READ_ZONE
        else:
            _data_template = _DATA_TEMPLATE_READ_BUILDING
        # endregion

        _desired_status_code = 200

        # region Get Response Template (updated with data) based on Client Type
        if self.sdk_client == settings.SDK_CLIENT_TYPE_ASYNC:
            _response_template = _SDK_ASYNC_CLIENT_RESPONSE_TEMPLATE
            _response_template[_SDK_ASYNC_CLIENT_ATTR_STATUS_CODE] = _desired_status_code
            _response_template[_SDK_ASYNC_CLIENT_ATTR_DATA] = _data_template
        else:
            _desired_json = json.dumps(_data_template)
            _response_template = MockHTTPResponse(_desired_json, status_code=200)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'


class MatrixDeviceManagement:

    def create_async_response_get_realsense_migrated(self):
        ...


    def create_async_response_get_device_slots(self):
        ...
