import json

import test

# TODO: Below attributes should go in definitions of project root
#  and fetched from there, to keep compatibility between them
#  But where in program these attributes are used is not known
_SDK_ASYNC_CLIENT_ATTR_STATUS_CODE = 'status'
_SDK_ASYNC_CLIENT_ATTR_MESSAGE = 'message'
_SDK_ASYNC_CLIENT_ATTR_DATA = 'data'

_SDK_ASYNC_CLIENT_MESSAGE_VALUE_SUCCESS = 'Success'

_SDK_ASYNC_CLIENT_RESPONSE_TEMPLATE = {
    _SDK_ASYNC_CLIENT_ATTR_STATUS_CODE: 200,
    _SDK_ASYNC_CLIENT_ATTR_MESSAGE: "Success",
    _SDK_ASYNC_CLIENT_ATTR_DATA: {}
}


class MockHTTPResponse:

    def __init__(self, json_data: str, status_code: int):

        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


# TODO: Take care of todo differences below.


class SCService:

    def __init__(self, client: str):

        self._sdk_client = client
        self._desired_status_code = 200

        self.ops = set()

    def create_response_for_op(self, op: str) -> dict:
        pass

# TODO: Grids returns response in certain format

class MatrixGrids(SCService):
    Op1 = test.grids.OP_READ_ZONE
    Op2 = test.grids.OP_READ_BUILDING

    _DataTemplatesByOp = test.grids.DATA_TEMPLATE_BY_OP

    def __init__(self, client: str):

        super().__init__(client)

        self.ops = {
            self.__class__.Op1,
            self.__class__.Op2
        }

    def create_response_for_op(self, op: str) -> dict:

        print(f'Creating Mock response for op: {op} in {self.__class__.__name__}')

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.ops:
            print(f'Ops in this class are: {self.ops}')
            data_return['text'] = f'Given op: {op} does not have a test response available.'
            return data_return

        # region Get Data Template for Op
        if op not in self.__class__._DataTemplatesByOp:
            _status_text = f'No Data Template defined for Op: {op} in {self.__class__.__name__}'
            print(_status_text)
            data_return['text'] = _status_text
            return data_return
        _data_template = self.__class__._DataTemplatesByOp[op]
        # endregion

        # region Get Response Template (updated with data) based on Client Type
        if self._sdk_client == test.SDK_CLIENT_TYPE_ASYNC:
            _response_template = _SDK_ASYNC_CLIENT_RESPONSE_TEMPLATE
            _response_template[_SDK_ASYNC_CLIENT_ATTR_STATUS_CODE] = self._desired_status_code
            _response_template[_SDK_ASYNC_CLIENT_ATTR_DATA] = _data_template
        else:
            _desired_json = json.dumps(_data_template)
            _response_template = MockHTTPResponse(_desired_json, self._desired_status_code)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'
        return data_return


# TODO: Device management returns the data directly without any formatting
#  i.e. desired data is at root level

class MatrixDeviceManagement(SCService):

    Op1 = test.device_management.OP_REALSENSE_MIGRATED
    Op2 = test.device_management.OP_GET_DEVICE_SLOTS

    _DataTemplatesByOp = test.device_management.DATA_TEMPLATE_BY_OP

    def __init__(self, client: str):

        super().__init__(client)

        self.ops = {
            self.__class__.Op1,
            self.__class__.Op2
        }

    def create_response_for_op(self, op: str) -> dict:

        print(f'Creating Mock response for op: {op} in {self.__class__.__name__}')

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.ops:
            print(f'Ops in this class are: {self.ops}')
            data_return['text'] = f'Given op: {op} does not have a test response available.'
            return data_return

        # region Get Data Template for Op
        if op not in self.__class__._DataTemplatesByOp:
            _status_text = f'No Data Template defined for Op: {op} in {self.__class__.__name__}'
            print(_status_text)
            data_return['text'] = _status_text
            return data_return
        _data_template = self.__class__._DataTemplatesByOp[op]
        # endregion

        # region Get Response Template (updated with data) based on Client Type
        if self._sdk_client == test.SDK_CLIENT_TYPE_ASYNC:
            _response_template = _SDK_ASYNC_CLIENT_RESPONSE_TEMPLATE
            _response_template[_SDK_ASYNC_CLIENT_ATTR_STATUS_CODE] = self._desired_status_code
            _response_template[_SDK_ASYNC_CLIENT_ATTR_DATA] = _data_template
        else:
            _desired_json = json.dumps(_data_template)
            _response_template = MockHTTPResponse(_desired_json, self._desired_status_code)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'
        return data_return
