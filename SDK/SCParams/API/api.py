import os
import json
from urllib.request import urlopen

from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync

HOST = "SC_PARAMS_HOST"
PROTOCOL = "SC_PARAMS_HTTP_PROTOCOL"
PORT = "SC_PARAMS_PORT"

MODULE_NAME = 'scparams'

# TODO: Note: This op name tentative (currently invalid for the real service)
OP_NAME_SET_ATTRIBUTES_ASYNC = 'setAttributesAsync'

MODULE_API_VERSION = 'v2'

DEFAULT_BASE_URI = 'console.smartclean.io/api'

SCPARAMS_ATTR_NAME_SERVICE = 'service'
SCPARAMS_ATTR_NAME_ATTRIBUTE = 'attribute'
SCPARAMS_ATTR_NAME_NS = 'ns'
SCPARAMS_ATTR_NAME_PRINCIPAL = 'principal'
SCPARAMS_ATTR_NAME_VALUE = 'value'

SCPARAMS_ATTR_NAMES = {
    SCPARAMS_ATTR_NAME_SERVICE,
    SCPARAMS_ATTR_NAME_ATTRIBUTE,
    SCPARAMS_ATTR_NAME_NS,
    SCPARAMS_ATTR_NAME_PRINCIPAL,
    SCPARAMS_ATTR_NAME_VALUE
}


# TODO: Future enhancement / proposal:
# Add function or example to show:
# How to create request body for set attributes async


# Below is an example data object for SCParams Set / Update params requests
"""
SCPARAMS_CREATE_PARAM_RECORD = {
    SCPARAMS_ATTR_NAME_SERVICE: 'sg.smartclean.vcs',
    SCPARAMS_ATTR_NAME_ATTRIBUTE: 'TestProjectParameter',
    SCPARAMS_ATTR_NAME_NS: 'Project',
    SCPARAMS_ATTR_NAME_PRINCIPAL: 'TestPropertyId',
    SCPARAMS_ATTR_NAME_VALUE: 'ValueOfTestProjectParameter'
}
"""


class SCParams:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = f"{DEFAULT_BASE_URI}/{MODULE_NAME}"
                print(f"{MODULE_NAME}: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print(f"{MODULE_NAME}: protocol env variable is not set")

            # Below block of comments is for obtaining module version from remote (when required to do so)
            """
            # url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            # response = urlopen(url)
            # data_json = json.loads(response.read())
            # apiversion = data_json["modules"]["scparams"]["version"]
            """

            apiversion = MODULE_API_VERSION

            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service=MODULE_NAME
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service=MODULE_NAME
                )
            else:
                print(f"{MODULE_NAME}: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service=MODULE_NAME
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service=MODULE_NAME
                )
        except Exception as e:
            print("Exception " + str(e))


    @classmethod
    def _validate_scparams_record(cls, scparams_record: dict) -> dict:

        data_return = {
            'success': False,
            'text': 'default'
        }

        # Ensure given record is not empty
        if not scparams_record:
            data_return['text'] = 'Given SCParams record is empty'
            return data_return

        # Ensure given record is a dictionary
        _type_scparams_record = type(scparams_record)
        if _type_scparams_record != dict:
            data_return['text'] = f'Given SCParams record has type: {str(_type_scparams_record)} (Expected dictionary)'
            return data_return

        # Ensure all required attributes are present
        keys_in_given_record = set(scparams_record.keys())
        keys_missing_in_given_record = SCPARAMS_ATTR_NAMES.difference(keys_in_given_record)
        if keys_missing_in_given_record:
            if len(keys_missing_in_given_record) == 1:
                data_return['text'] = f'Following required attribute missing from given SCParams record: ' \
                                      f'{keys_missing_in_given_record.pop()}'
            else:
                data_return['text'] = f'Following required attributes missing from given SCParams record ' \
                                      f'{keys_missing_in_given_record}'
            return data_return

        # Ensure none of the attributes is None
        values_in_given_record = set(scparams_record.values())
        if None in values_in_given_record:
            keys_with_none_value = {key for key, value in scparams_record.items() if value is None}
            if len(keys_with_none_value) == 1:
                data_return['text'] = f'Following attribute in given SCParams record is None: ' \
                                      f'{keys_with_none_value.pop()}'
            else:
                data_return['text'] = f'Following attributes in given SCParams record are None: {keys_with_none_value}'

        # TODO: Enhancement: Validate each attribute (each can be a function on its own)
        data_return['success'] = True
        data_return['text'] = 'Validated given SCParams record'
        return data_return

    def set_attributes_async(self, org: str, pid: str, prop_id: str, scparams_records: list, client=None):

        data_return = {
            'code': 'failure',
            'error': 'default',
            'data': None
        }

        if not scparams_records:
            data_return['error'] = 'Given value of scparams_records is empty'
            return data_return

        # region Ensure scparams_records is a list
        _type_scparams_records = type(scparams_records)
        if _type_scparams_records != list:
            data_return['error'] = f'Given value of scparams_records has type: {str(_type_scparams_records)} ' \
                                   f'(Expected list)'
            return data_return
        # endregion

        valid_scparams_records = []
        no_of_scparams_records = len(scparams_records)
        if no_of_scparams_records == 1:
            scparams_record = scparams_records[0]
            validate_scparams_record_resp = self.__class__._validate_scparams_record(scparams_record)
            validate_scparams_record_text = validate_scparams_record_resp['text']

            if validate_scparams_record_resp['success'] is False:

                invalid_record_data = {
                    'record': scparams_record,
                    'reason': validate_scparams_record_text
                }

                data_return['error'] = f'Given value of scparams_records is invalid'
                data_return['invalid_records'] = [invalid_record_data]
                data_return['no_of_invalid_records'] = 1

                return data_return
            valid_scparams_records.append(scparams_record)
            print(validate_scparams_record_text)
        else:
            invalid_records_data = []
            for scparams_record in scparams_records:
                validate_scparams_record_resp = self.__class__._validate_scparams_record(scparams_records[0])
                validate_scparams_record_text = validate_scparams_record_resp['text']

                if validate_scparams_record_resp['success'] is False:
                    invalid_record_data = {
                        'record': scparams_record,
                        'reason': validate_scparams_record_text
                    }

                    invalid_records_data.append(invalid_record_data)
                else:
                    valid_scparams_records.append(scparams_record)
                    print(validate_scparams_record_text)

            if invalid_records_data:
                data_return['no_of_invalid_records'] = len(invalid_records_data)
                data_return['invalid_records'] = invalid_records_data

        _args_for_function = {
            'httpmethod': 'POST',
            'op': OP_NAME_SET_ATTRIBUTES_ASYNC,
            'propid': prop_id,
            'org': org,
            'pid': pid,
            'body': json.dumps(valid_scparams_records)
        }

        if client == "Sync":
            res = self.Sync_client.makeRequest(**_args_for_function)
        else:
            res = self.Async_client.makeRequest(**_args_for_function)
        return res
