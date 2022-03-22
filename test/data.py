import json

import test
from test import definitions

from test import (
    grids,
    device_management,
    workforce_management,
    sms_gateway,
    partners_solutions
)


# TODO: Below attributes should go in definitions of project root
#  and fetched from there, to keep compatibility between them
#  But where in program these attributes are used is not known


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


class SCGrids(SCService):

    Ops = grids.OP_READ_ZONE
    _DataTemplatesByOp = grids.DATA_TEMPLATE_BY_OP

    def __init__(self, client: str):

        super().__init__(client)

    def create_response_for_op(self, op: str) -> dict:

        print(f'Creating Mock response for op: {op} in {self.__class__.__name__}')

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.__class__.Ops:
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
        if self._sdk_client == definitions.SDK_CLIENT_TYPE_ASYNC:
            _response_template = test.grids.RESPONSE_TEMPLATE_GRIDS
            _response_template[test.grids.SDK_ASYNC_CLIENT_ATTR_STATUS_CODE] = self._desired_status_code
            _response_template[test.grids.SDK_ASYNC_CLIENT_ATTR_DATA] = _data_template
        else:
            _desired_json = json.dumps(_data_template)
            _response_template = MockHTTPResponse(_desired_json, self._desired_status_code)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'
        return data_return


class SCDeviceManagement(SCService):

    Ops = device_management.OPS
    _DataTemplatesByOp = device_management.DATA_TEMPLATE_BY_OP

    def __init__(self, client: str):

        super().__init__(client)

    def create_response_for_op(self, op: str) -> dict:

        print(f'Creating Mock response for op: {op} in {self.__class__.__name__}')

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.__class__.Ops:
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
        if self._sdk_client == definitions.SDK_CLIENT_TYPE_ASYNC:
            _response_template = _data_template
        else:
            _desired_json = json.dumps(_data_template)
            _response_template = MockHTTPResponse(_desired_json, self._desired_status_code)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'
        return data_return


class SCWorkforceManagement(SCService):

    Ops = workforce_management.OPS
    _DataTemplatesByOp = workforce_management.DATA_TEMPLATE_BY_OP

    def __init__(self, client: str):

        super().__init__(client)

    def create_response_for_op(self, op: str) -> dict:

        print(f'Creating Mock response for op: {op} in {self.__class__.__name__}')

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.__class__.Ops:
            print(f'Ops in this class are: {self.__class__.Ops}')
            data_return['text'] = f'Given op: {op} does not have a test response available.'
            return data_return

        _data_template = None
        # region Get Data Template for Op (if defined)
        if op in self.__class__._DataTemplatesByOp:
            _status_text = f'Data template defined for Op: {op} in {self.__class__.__name__}'
            print(_status_text)
            _data_template = self.__class__._DataTemplatesByOp[op]
        # endregion

        # region Get Response Template (updated with data) based on Client Type

        if self._sdk_client == definitions.SDK_CLIENT_TYPE_ASYNC:
            # region Get Response Template based on Op
            if op == workforce_management.OP_CREATE_INCIDENT_NO_ASSIGNEE:
                _response_template = workforce_management.RESPONSE_TEMPLATE_CREATE_INCIDENT
            elif op == workforce_management.OP_FIND_AVAILABILITY:
                _response_template = workforce_management.RESPONSE_TEMPLATE_FIND_AVAILABILITY
            else:
                _response_template = workforce_management.RESPONSE_TEMPLATE_ASSIGN_INCIDENT
            # endregion
            if _data_template is not None:
                _response_template[workforce_management.RESPONSE_ATTR_DATA] = _data_template
        else:
            if _data_template is None:
                data = None
            else:
                data = json.dumps(_data_template)

            _response_template = MockHTTPResponse(data, self._desired_status_code)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'
        return data_return


class SCMessageService(SCService):

    Ops = sms_gateway.OPS
    _DataTemplatesByOp = sms_gateway.DATA_TEMPLATE_BY_OP

    def __init__(self, client: str):

        super().__init__(client)

    def create_response_for_op(self, op: str) -> dict:

        print(f'Creating Mock response for op: {op} in {self.__class__.__name__}')

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.__class__.Ops:
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
        if self._sdk_client == definitions.SDK_CLIENT_TYPE_ASYNC:
            _response_template = _data_template
        else:
            _desired_json = json.dumps(_data_template)
            _response_template = MockHTTPResponse(_desired_json, self._desired_status_code)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'
        return data_return


class SCPartnersSolutions(SCService):

    Ops = partners_solutions.OPS

    def __init__(self, client: str):

        super().__init__(client)

    def create_response_for_op(self, op: str) -> dict:

        print(f'Creating Mock response for op: {op} in {self.__class__.__name__}')

        data_return = {
            'response': None,
            'text': 'default'
        }

        if op not in self.__class__.Ops:
            print(f'Ops in this class are: {self.ops}')
            data_return['text'] = f'Given op: {op} does not have a test response available.'
            return data_return

        _data_template = partners_solutions.RESPONSE_DATA_TEMPLATE

        # region Get Response Template (updated with data) based on Client Type
        if self._sdk_client == definitions.SDK_CLIENT_TYPE_ASYNC:
            _response_template = _data_template
        else:
            _desired_json = json.dumps(_data_template)
            _response_template = MockHTTPResponse(_desired_json, self._desired_status_code)
        # endregion

        data_return['response'] = _response_template
        data_return['text'] = 'Created Response Template'
        return data_return
