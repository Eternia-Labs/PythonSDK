import time
import json
import os
from pprint import pformat
from tornado.httpclient import HTTPClientError
from tornado.simple_httpclient import HTTPTimeoutError

from dotenv import load_dotenv

LOAD_ENV_VARS = True
EXTRACT_DATA_FROM_SDK_RESPONSE = True

CLIENT_TYPE_SYNC = 'Sync'
CLIENT_TYPE_ASYNC = 'Async'

TEST_READ_ZONE_RESPONSE = {
    "status": 200,
    "message": "Success",
    "data": {
        "OrgId": "OCBC",
        "PropId": "f63385a2b32d4c0d9da70e1cd1e18f9d",
        "PID": "90005c6aa28c44228b75904ee4fbb05d",
        "LID": "8a243ff483424602b0d3c7f3016336e2",
        "InsID": "f7ae7d1adc054586bd4753388c243efc",
        "BeaconID": "N.A.",
        "ZoneCategoryID": "MEETING_ROOMS",
        "Name": "Executive Meeting Room",
        "Area": 200,
        "FloorType": "Carpet",
        "Status": "Active",
        "OperatingHours": {
            "0": [{
                "End": "0000",
                "Start": "0000"
            }],
            "1": [{
                "End": "1700",
                "Start": "0900"
            }],
            "2": [{
                "End": "2000",
                "Start": "0900"
            }],
            "3": [{
                "End": "1700",
                "Start": "0800"
            }],
            "4": [{
                "End": "1700",
                "Start": "0900"
            }],
            "5": [{
                "End": "1700",
                "Start": "1700"
            }],
            "6": [{
                "End": "1800",
                "Start": "0700"
            }]
        },
        "IsBuildingOperatingHours": True
    }
}

TEST_INCIDENT_RECORD = {
    "ATTR": "attr#90005c6aa28c44228b75904ee4fbb05d#8a6ef71079e54af2884563e93c4ad800#1621387048000",
    "AutoAssigned": 1,
    "By": "FD",
    "Delayed": 0,
    "End": 1621387948,
    "ID": "90005c6aa28c44228b75904ee4fbb05d",
    "Name": "User Feedback",
    "NS": "TS",
    "Priority": "H",
    "PropID": "f63385a2b32d4c0d9da70e1cd1e18f9d",
    "SeatId": "tbp",
    "ShiftId": "tbp",
    "SRN": "srn:sctasks:OCBC:::f63385a2b32d4c0d9da70e1cd1e18f9d/90005c6aa28c44228b75904ee4fbb05d:TS:INCIDENT/1621387048000",
    "Start": 1621387048,
    "Status": "NOT_ASSIGNED",
    "Subject": "Information",
    "taskCount": 1,
    "TaskId": "1621387048000",
    "Tasks": [
        {
            "Comments": "No Toilet Paper, No Soap",
            "Done": 0,
            "Name": "User Feedback",
            "T": 0
        }
    ],
    "Type": "INCIDENT",
    "Zone": "8a6ef71079e54af2884563e93c4ad800",
    "ZoneCatId": "MEETING_ROOMS",
    "ZoneName": "Meeting Room"
}


# TODO: Added generic signature for grids request (to be used in future when refactoring tests)
def test_grids_request(org: str, pid: str, **kwargs):
    print('TODO generic grids request')
    raise NotImplementedError


def test_get_property_info(org: str = None, pid: str = None, prop_id: str = None, test_client=CLIENT_TYPE_ASYNC):

    print('Starting test for a function in Grids service..')

    if org is None:
        org = os.environ['TEST_ORG']

    if pid is None:
        pid = os.environ['TEST_PID']

    if prop_id is None:
        prop_id = os.environ['TEST_PROP_ID']

    from SDK.SCGridsServices.API import SCGrids
    print('SCGrids imported from respective service directory.')
    grids = SCGrids()
    print('SCGrids instantiated.')

    read_prop_resp = grids.readProperty(org, pid, prop_id, test_client)

    print('Read property request complete. Response is:')
    print(read_prop_resp)

    print(f'{test_client} client was used for this request. Response will be parsed accordingly.')

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = read_prop_resp
        print('Obtained response')
    else:
        status_code = read_prop_resp.status_code
        print(f'Status code in this response is: {status_code}')
        response_content = read_prop_resp.json()
        print('Obtained .json() from response.')
    # endregion

    print('Type of response content is:')
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = 'Error in HTTP Request by sc-python-sdk'
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f'{_status_text}: code: {_status_code}| message: {_err_text}'
        print(return_text)
        return

    print('Response content is:')
    print(pformat(response_content))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content['data']
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


# TODO: Check below function is compatible with test-python-sdk
def test_get_building_info(org: str = None, pid: str = None, test_client=CLIENT_TYPE_ASYNC):

    print('Starting test for get_building_info...')

    if org is None:
        org = os.environ['TEST_ORG']

    if pid is None:
        pid = os.environ['TEST_PID']

    from SDK.SCGridsServices.API import SCGrids
    print('SCGrids imported from respective service directory.')
    grids = SCGrids()
    print('SCGrids instantiated.')

    read_building_resp = grids.readBuilding(org, pid, test_client)

    print('Read building request complete. Response is:')
    print(read_building_resp)

    print(f'{test_client} client was used for this request. Response will be parsed accordingly.')

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = read_building_resp
        print('Obtained response')
    else:
        status_code = read_building_resp.status_code
        print(f'Status code in this response is: {status_code}')
        response_content = read_building_resp.json()
        print('Obtained .json() from response.')
    # endregion

    print('Type of response content is:')
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = 'Error in HTTP Request by sc-python-sdk'
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f'{_status_text}: code: {_status_code}| message: {_err_text}'
        print(return_text)
        return

    print('Response content is:')
    print(pformat(response_content))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content['data']
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_get_zone_info(org: str = None, pid: str = None, zone_id: str = None, test_client=CLIENT_TYPE_ASYNC):

    print('Starting test for Get Zone Info...')

    if org is None:
        org = os.environ['TEST_ORG']

    if pid is None:
        pid = os.environ['TEST_PID']

    if zone_id is None:
        zone_id = os.environ['TEST_ZONE_ID']

    from SDK.SCGridsServices.API import SCGrids
    print('SCGrids imported from respective service directory.')
    grids = SCGrids()
    print('SCGrids instantiated.')

    request_body = {
        'InsID': zone_id
    }

    read_zone_resp = grids.read_zone(org, pid, json.dumps(request_body), test_client)

    print('Read zone request complete. Response is:')
    print(read_zone_resp)

    print(f'{test_client} client was used for this request. Response will be parsed accordingly.')

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = read_zone_resp
        print('Obtained response')
    else:
        status_code = read_zone_resp.status_code
        print(f'Status code in this response is: {status_code}')
        response_content = read_zone_resp.json()
        print('Obtained .json() from response.')
    # endregion

    print('Type of response content is:')
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = 'Error in HTTP Request by sc-python-sdk'
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f'{_status_text}: code: {_status_code}| message: {_err_text}'
        print(return_text)
        return

    print('Response content is:')
    print(pformat(response_content))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content['data']
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_create_incident_without_assignee(org: str = None, pid: str = None, prop_id: str = None, zone_id: str = None,
                                          test_client=CLIENT_TYPE_ASYNC):

    print('Starting test for Create Incident No Assignee...')

    if org is None:
        org = os.environ['TEST_ORG']

    if pid is None:
        pid = os.environ['TEST_PID']

    if prop_id is None:
        prop_id = os.environ['TEST_PROP_ID']

    if zone_id is None:
        zone_id = os.environ['TEST_ZONE_ID']

    from SDK.SCWorkforceManagementServices.API import SCWorkforcemanagement
    print('SCWorkforcemanagement imported from respective service directory.')
    scworkforcemanagement = SCWorkforcemanagement()
    print('SCWorkforcemanagement instantiated.')

    test_zone_details = {
        'zone_id': zone_id,
        'zone_category_id': f'Test Cat ID for ZoneID: {zone_id}',
        'zone_name': f'Test Name for ZoneID: {zone_id}'
    }

    request_body = {
        'Incident': _create_data_for_incident(test_zone_details)
    }

    create_incident_resp = scworkforcemanagement.createIncidentWithoutAssignee(org, prop_id, pid, json.dumps(request_body),
                                                                         test_client)

    print('Create incident request complete. Response is:')
    print(create_incident_resp)

    print(f'{test_client} client was used for this request. Response will be parsed accordingly.')

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = create_incident_resp
        print('Obtained response')
    else:
        status_code = create_incident_resp.status_code
        print(f'Status code in this response is: {status_code}')
        response_content = create_incident_resp.json()
        print('Obtained .json() from response.')
    # endregion

    print('Type of response content is:')
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = 'Error in HTTP Request by sc-python-sdk'
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f'{_status_text}: code: {_status_code}| message: {_err_text}'
        print(return_text)
        return

    print('Response content is:')
    print(pformat(response_content))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content['data']
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_find_availability_for_incident(org: str = None, pid: str = None, prop_id: str = None, zone_id: str = None,
                                        test_client=CLIENT_TYPE_ASYNC, return_mock: bool = True):

    print('Starting test to Find availability for Incident...')

    if org is None:
        org = os.environ['TEST_ORG']

    if pid is None:
        pid = os.environ['TEST_PID']

    if prop_id is None:
        prop_id = os.environ['TEST_PROP_ID']

    if zone_id is None:
        zone_id = os.environ['TEST_ZONE_ID']

    from SDK.SCWorkforceManagementServices.API import SCWorkforcemanagement
    print('SCWorkforcemanagement imported from respective service directory.')
    scworkforcemanagement = SCWorkforcemanagement()
    print('SCWorkforcemanagement instantiated.')

    if return_mock is True:
        response_content = WORKFORCE_FIND_AVAILABILITY_RESPONSE_2
    else:
        curr_unix_time = int(time.time())
        end_unix_time = curr_unix_time + 900  # Adding 15 minutes to current for due time.

        request_body = {
            "EndTime": end_unix_time,
            "ZoneID": [
                zone_id
            ]
        }

        response = scworkforcemanagement.find_availability_for_incident(org, prop_id, pid, json.dumps(request_body), test_client)

        print('Find availability request complete. Response is:')
        print(response)

        print(f'{test_client} client was used for this request. Response will be parsed accordingly.')

        # region Parse response based on type of client
        if test_client == CLIENT_TYPE_ASYNC:
            response_content = response
            print('Obtained response')
        else:
            status_code = response.status_code
            print(f'Status code in this response is: {status_code}')
            response_content = response.json()
            print('Obtained .json() from response.')
        # endregion

    print('Type of response content is:')
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = 'Error in HTTP Request by sc-python-sdk'
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f'{_status_text}: code: {_status_code}| message: {_err_text}'
        print(return_text)
        return

    print('Response content is:')
    print(pformat(response_content))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content['data']
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def _create_data_for_incident(zone_details: dict):

    test_task_details = {'Name': 'Test Task in Incident', 'Comments': 'No Comments'}

    zone_cat_id = zone_details['zone_category_id']
    zone_name = zone_details['zone_name']
    zone_id = zone_details['zone_id']

    curr_unix_time = int(time.time())
    end_unix_time = curr_unix_time + 900

    test_source_type = 'Test Type'

    incident_data = {
        'Start': curr_unix_time,
        'End': end_unix_time,
        'Name': 'Test Incident',
        'Priority': 'H',
        'By': test_source_type,
        'Subject': 'Test Incident Subject',
        'AutoAssigned': True,
        'Tasks': [test_task_details],
        'ZoneCatId': zone_cat_id,
        'Zone': zone_id,
        'ZoneName': zone_name
    }

    return incident_data


def load_env_vars(dotenv_filepath: str = None):

    print('Loading variables from standard environment file into environment...')
    if dotenv_filepath is None:
        root_dir = os.path.dirname(os.path.abspath(__file__))
        print(f'Root directory is:')
        print(root_dir)
        filepath = f'{root_dir}/env-dev.env'
        print('env file path is:')
        print(filepath)
    else:
        raise Exception('Currently not loading vars from dotenv file (TODO later)')

    load_dotenv(filepath)
    print('Loaded vars from above .env file in current environment.')


def run_test():

    if LOAD_ENV_VARS is True:
        load_env_vars()
    # test_get_zone_info()
    # test_get_building_info()
    # test_create_incident_without_assignee()
    test_find_availability_for_incident(return_mock=False)


# region Find availability for incident Sample Response
# Test Response. Includes 2 Seat IDs. Seat 1 has Shift without task assigned,
# Seat 2 has task assigned, but shows 2 objects TODO: (why?)
# is it because it may have 2 tasks assigned to the same Shift?
# Datetime: 18 May 2021, 10:05 AM SGT
WORKFORCE_FIND_AVAILABILITY_RESPONSE_2 = {
    "message": "Available entries for given Zone",
    "data": {
        "OCBC_005": [
            {
                "ShiftID": "6bdbe62e-4ab1-4750-8318-503a10175fb4",
                "ZoneName": None,
                "SameZone": False,
                "Status": "PUBLISHED",
                "StartTime": 1621306800,
                "ZoneID": None
            }
        ],
        "OCBC_001": [
            {
                "ShiftID": "6e2991d7-7405-4ab3-9f45-4c96575be064",
                "ZoneName": "Meeting Room",
                "SameZone": True,
                "Status": "PUBLISHED",
                "StartTime": 1621299600,
                "ZoneID": "8a6ef71079e54af2884563e93c4ad800"
            },
            {
                "ShiftID": "6e2991d7-7405-4ab3-9f45-4c96575be064",
                "ZoneName": "Meeting Room",
                "SameZone": True,
                "Status": "PUBLISHED",
                "StartTime": 1621317600,
                "ZoneID": "8a6ef71079e54af2884563e93c4ad800"
            }
        ]
    },
    "code": "SUCCESS"
}
# endregion


if __name__ == '__main__':
    run_test()
