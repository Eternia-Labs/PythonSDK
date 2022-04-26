import sys
import time
import json
import os
from pprint import pformat
from tornado.httpclient import HTTPClientError
from tornado.simple_httpclient import HTTPTimeoutError

import test.data
from test import (
    grids,
    sms_gateway,
    device_management,
    workforce_management,
    partners_solutions
)

LOAD_ENV_VARS = True
EXTRACT_DATA_FROM_SDK_RESPONSE = True

CLIENT_TYPE_SYNC = "Sync"
CLIENT_TYPE_ASYNC = "Async"

# region Service Names and respective Ops
# region SCGrids
SERVICE_ID_GRIDS = grids.SERVICE_ID
GRIDS_OP_GET_ZONE_INFO = grids.OP_READ_ZONE
GRIDS_OP_GET_BUILDING_INFO = grids.OP_READ_BUILDING
GRIDS_OP_GET_PROPERTY_INFO = grids.OP_READ_PROPERTY
# endregion

# region SCDeviceManagement
SERVICE_ID_DEVICE_MANAGEMENT = device_management.SERVICE_ID
DEVICE_MANAGEMENT_OP_REALSENSE_MIGRATED = device_management.OP_REALSENSE_MIGRATED
DEVICE_MANAGEMENT_OP_GET_DEVICE_SLOTS = device_management.OP_GET_DEVICE_SLOTS
# endregion

# region SCWorkforceManagement
SERVICE_ID_WORKFORCE_MANAGEMENT = workforce_management.SERVICE_ID
WORKFORCE_MGMT_OP_ASSIGN_INCIDENT = workforce_management.OP_ASSIGN_INCIDENT
WORKFORCE_MGMT_OP_FIND_AVAILABILITY = workforce_management.OP_FIND_AVAILABILITY
WORKFORCE_MGMT_OP_CREATE_INCIDENT_NO_ASSIGNEE = workforce_management.OP_CREATE_INCIDENT_NO_ASSIGNEE
WORKFORCE_MGMT_OP_GET_INCIDENT_SETTINGS = workforce_management.OP_GET_INCIDENT_SETTINGS
# endregion

# region SCSMSGateway
SERVICE_ID_SMS_GATEWAY = sms_gateway.SERVICE_ID
SMS_GATEWAY_OP_PUBLISH_SMS = sms_gateway.OP_PUBLISH_SMS
# endregion

# region SCPartnersSolutions
SERVICE_ID_PARTNERS_SOLUTIONS = partners_solutions.SERVICE_ID
OPS = partners_solutions.OPS
# endregion

# endregion


# region Tests inside these functions have been included in the respective Service test function
def test_get_property_info(
    org: str = None, pid: str = None, prop_id: str = None, test_client=CLIENT_TYPE_ASYNC
):

    print("Starting test for a function in Grids service..")

    if org is None:
        org = os.environ["TEST_ORG"]

    if pid is None:
        pid = os.environ["TEST_PID"]

    if prop_id is None:
        prop_id = os.environ["TEST_PROP_ID"]

    from SDK.SCGridsServices.API import SCGrids

    print("SCGrids imported from respective service directory.")
    grids = SCGrids()
    print("SCGrids instantiated.")

    read_prop_resp = grids.readProperty(org, pid, prop_id, test_client)

    print("Read property request complete. Response is:")
    print(read_prop_resp)

    print(
        f"{test_client} client was used for this request. Response will be parsed accordingly."
    )

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = read_prop_resp
        print("Obtained response")
    else:
        status_code = read_prop_resp.status_code
        print(f"Status code in this response is: {status_code}")
        response_content = read_prop_resp.json()
        print("Obtained .json() from response.")
    # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return

    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content["data"]
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_get_building_info(
    org: str = None, pid: str = None, test_client=CLIENT_TYPE_ASYNC
):

    print("Starting test for get_building_info...")

    if org is None:
        org = os.environ["TEST_ORG"]

    if pid is None:
        pid = os.environ["TEST_PID"]

    from SDK.SCGridsServices.API import SCGrids

    print("SCGrids imported from respective service directory.")
    grids = SCGrids()
    print("SCGrids instantiated.")

    read_building_resp = grids.readBuilding(org, pid, test_client)

    print("Read building request complete. Response is:")
    print(read_building_resp)

    print(
        f"{test_client} client was used for this request. Response will be parsed accordingly."
    )

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = read_building_resp
        print("Obtained response")
    else:
        status_code = read_building_resp.status_code
        print(f"Status code in this response is: {status_code}")
        response_content = read_building_resp.json()
        print("Obtained .json() from response.")
    # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return

    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content["data"]
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_get_zone_info(
    org: str = None, pid: str = None, zone_id: str = None, test_client=CLIENT_TYPE_ASYNC
):

    print("Starting test for Get Zone Info...")

    if org is None:
        org = os.environ["TEST_ORG"]

    if pid is None:
        pid = os.environ["TEST_PID"]

    if zone_id is None:
        zone_id = os.environ["TEST_ZONE_ID"]

    from SDK.SCGridsServices.API import SCGrids

    print("SCGrids imported from respective service directory.")
    grids = SCGrids()
    print("SCGrids instantiated.")

    request_body = {"InsID": zone_id}

    read_zone_resp = grids.read_zone(org, pid, json.dumps(request_body), test_client)

    print("Read zone request complete. Response is:")
    print(read_zone_resp)

    print(
        f"{test_client} client was used for this request. Response will be parsed accordingly."
    )

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = read_zone_resp
        print("Obtained response")
    else:
        status_code = read_zone_resp.status_code
        print(f"Status code in this response is: {status_code}")
        response_content = read_zone_resp.json()
        print("Obtained .json() from response.")
    # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return

    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content["data"]
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_create_incident_without_assignee(
    org: str = None,
    pid: str = None,
    prop_id: str = None,
    zone_id: str = None,
    test_client=CLIENT_TYPE_ASYNC,
):

    print("Starting test for Create Incident No Assignee...")

    if org is None:
        org = os.environ["TEST_ORG"]

    if pid is None:
        pid = os.environ["TEST_PID"]

    if prop_id is None:
        prop_id = os.environ["TEST_PROP_ID"]

    if zone_id is None:
        zone_id = os.environ["TEST_ZONE_ID"]

    from SDK.SCWorkforceManagementServices.API import SCWorkforcemanagement

    print("SCWorkforcemanagement imported from respective service directory.")
    scworkforcemanagement = SCWorkforcemanagement()
    print("SCWorkforcemanagement instantiated.")

    test_zone_details = {
        "zone_id": zone_id,
        "zone_category_id": f"Test Cat ID for ZoneID: {zone_id}",
        "zone_name": f"Test Name for ZoneID: {zone_id}",
    }

    request_body = {"Incident": _create_data_for_incident(test_zone_details)}

    create_incident_resp = scworkforcemanagement.createIncidentWithoutAssignee(
        org, prop_id, pid, json.dumps(request_body), test_client
    )

    print("Create incident request complete. Response is:")
    print(create_incident_resp)

    print(
        f"{test_client} client was used for this request. Response will be parsed accordingly."
    )

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = create_incident_resp
        print("Obtained response")
    else:
        status_code = create_incident_resp.status_code
        print(f"Status code in this response is: {status_code}")
        response_content = create_incident_resp.json()
        print("Obtained .json() from response.")
    # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return

    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content["data"]
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_get_incident_settings(
    org: str = None,
    pid: str = None,
    prop_id: str = None,
    test_client=CLIENT_TYPE_ASYNC,
):

    print("Starting test for get incident settings...")

    if org is None:
        org = os.environ["TEST_ORG"]

    if pid is None:
        pid = os.environ["TEST_PID"]

    if prop_id is None:
        prop_id = os.environ["TEST_PROP_ID"]

    from SDK.SCWorkforceManagementServices.API import SCWorkforcemanagement

    print("SCWorkforcemanagement imported from respective service directory.")
    scworkforcemanagement = SCWorkforcemanagement()
    print("SCWorkforcemanagement instantiated.")

    get_incident_settings_resp = scworkforcemanagement.get_incident_settings(
        org, pid, prop_id, test_client
    )

    print("Get incident settings request complete. Response is:")
    print(get_incident_settings_resp)

    print(
        f"{test_client} client was used for this request. Response will be parsed accordingly."
    )

    # region Parse response based on type of client
    if test_client == CLIENT_TYPE_ASYNC:
        response_content = get_incident_settings_resp
        print("Obtained response")
    else:
        status_code = get_incident_settings_resp.status_code
        print(f"Status code in this response is: {status_code}")
        response_content = get_incident_settings_resp.json()
        print("Obtained .json() from response.")
    # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return

    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content["data"]
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_find_availability_for_incident(
    org: str = None,
    pid: str = None,
    prop_id: str = None,
    zone_id: str = None,
    test_client=CLIENT_TYPE_ASYNC,
    return_mock: bool = True,
):

    print("Starting test to Find availability for Incident...")

    if org is None:
        org = os.environ["TEST_ORG"]

    if pid is None:
        pid = os.environ["TEST_PID"]

    if prop_id is None:
        prop_id = os.environ["TEST_PROP_ID"]

    if zone_id is None:
        zone_id = os.environ["TEST_ZONE_ID"]

    from SDK.SCWorkforceManagementServices.API import SCWorkforcemanagement

    print("SCWorkforcemanagement imported from respective service directory.")
    scworkforcemanagement = SCWorkforcemanagement()
    print("SCWorkforcemanagement instantiated.")

    if return_mock is True:
        response_content = WORKFORCE_FIND_AVAILABILITY_RESPONSE_2
    else:
        curr_unix_time = int(time.time())
        end_unix_time = (
            curr_unix_time + 900
        )  # Adding 15 minutes to current for due time.

        request_body = {"EndTime": end_unix_time, "ZoneID": [zone_id]}

        response = scworkforcemanagement.find_availability_for_incident(
            org, prop_id, pid, json.dumps(request_body), test_client
        )

        print("Find availability request complete. Response is:")
        print(response)

        print(
            f"{test_client} client was used for this request. Response will be parsed accordingly."
        )

        # region Parse response based on type of client
        if test_client == CLIENT_TYPE_ASYNC:
            response_content = response
            print("Obtained response")
        else:
            status_code = response.status_code
            print(f"Status code in this response is: {status_code}")
            response_content = response.json()
            print("Obtained .json() from response.")
        # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return

    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content["data"]
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))


def test_assign_incident(test_client=CLIENT_TYPE_ASYNC, return_mock: bool = True):

    print('Starting test to Assign Incident...')

    if return_mock is True:
        response_content = WORKFORCE_ASSIGN_INCIDENT_RESPONSE
    else:
        org = os.environ['TEST_ORG']
        pid = os.environ['TEST_PID']
        prop_id = os.environ['TEST_PROP_ID']

        zone_id = os.environ['TEST_ZONE_ID']

        from SDK.SCWorkforceManagementServices.API import SCWorkforcemanagement
        print('SCWorkforcemanagement imported from respective service directory.')
        scworkforcemanagement = SCWorkforcemanagement()
        print('SCWorkforcemanagement instantiated.')

        seat_id = os.environ['TEST_SEAT_ID']
        shift_id = os.environ['TEST_SHIFT_ID']
        incident_id = os.environ['TEST_INCIDENT_ID']

        zone_id_for_assign_incident = '8a6ef71079e54af2884563e93c4ad800'

        request_body = {
            "SeatId": seat_id,
            "ShiftID": shift_id,
            "zoneId": zone_id_for_assign_incident,
            "IncidentID": incident_id
        }

        response = scworkforcemanagement.assign_shift_to_incident(org, prop_id, pid, json.dumps(request_body),
                                                                  test_client)

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

    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content['data']
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))
# endregion


def _create_data_for_incident(zone_details: dict):

    test_task_details = {"Name": "Test Task in Incident", "Comments": "No Comments"}

    zone_cat_id = zone_details["zone_category_id"]
    zone_name = zone_details["zone_name"]
    zone_id = zone_details["zone_id"]

    curr_unix_time = int(time.time())
    end_unix_time = curr_unix_time + 900

    test_source_type = "Test Type"

    incident_data = {
        "Start": curr_unix_time,
        "End": end_unix_time,
        "Name": "Test Incident",
        "Priority": "H",
        "By": test_source_type,
        "Subject": "Test Incident Subject",
        "AutoAssigned": True,
        "Tasks": [test_task_details],
        "ZoneCatId": zone_cat_id,
        "Zone": zone_id,
        "ZoneName": zone_name,
    }

    return incident_data


def load_env_vars(load_from_dotenv_file: bool = False, dotenv_filepath: str = None):

    from dotenv import load_dotenv
    if load_from_dotenv_file is True:
        print("Loading variables from standard environment file into environment...")
        if dotenv_filepath is None:
            root_dir = os.path.dirname(os.path.abspath(__file__))
            print(f"Root directory is:")
            print(root_dir)
            filepath = f"{root_dir}/env-dev.env"
            print("env file path is:")
            print(filepath)
        else:
            raise Exception("Currently not loading vars from dotenv file (TODO later)")

        load_dotenv(filepath)
        print("Loaded vars from above .env file in current environment.")
    else:
        print('Setting env vars manually.')
        os.environ['TEST_ORG'] = 'TestOrgId'
        os.environ['TEST_PID'] = 'TestPID'
        os.environ['SC_DEVICE_MANAGEMENT_HOST'] = ''
        os.environ['SC_DEVICE_MANAGEMENT_HTTP_PROTOCOL'] = ''
        os.environ['SC_DEVICE_MANAGEMENT_PORT'] = ''


def test_op_in_service(service: str, op: str, org: str = None, pid: str = None, return_mock: bool = True):

    if LOAD_ENV_VARS is True:
        load_env_vars(load_from_dotenv_file=True)

    if org is None:
        org = os.environ['TEST_ORG']

    if pid is None:
        pid = os.environ['TEST_PID']

    prop_id = os.environ['TEST_PROP_ID']
    access_key_for_prop = os.environ['SC_ACCESS_KEY']
    secret_key_for_prop = os.environ['SC_SECRET_KEY']

    from SDK import utils
    response = utils.register_credentials_for_property(prop_id, access_key_for_prop, secret_key_for_prop)
    print(f'Register credentials response is:\n{pformat(response)}')

    if response['success'] is False:
        raise Exception('Register credentials failed.')

    client = CLIENT_TYPE_ASYNC

    if service == device_management.SERVICE_ID:
        response = test_device_management_api(op, org, prop_id, pid, client, return_mock)
    elif service == grids.SERVICE_ID:
        response = test_grids_api(op, org, pid, client, return_mock)
    elif service == workforce_management.SERVICE_ID:
        response = test_workforce_apis(op, org, pid, prop_id, client, return_mock)
    elif service == sms_gateway.SERVICE_ID:
        response = test_sms_gateway_apis(op, org, prop_id, pid, client, return_mock)
    elif service == partners_solutions.SERVICE_ID:
        response = test_partners_solutions_op(op, org, prop_id, client, return_mock)
    else:
        raise Exception('Test Requests for service not yet added')

    utils.deregister_credentials_for_property(property_id=prop_id)

    handle_response(response)


def test_sdk_utils():

    from test import sdk_utils
    sdk_utils.test_utils()


def handle_response(test_response: dict):
    # eg1 = {'code': 'failure', 'error': '[Errno 61] Connection refused'}
    # eg2 = {
    #  'code': 'failure',
    #  'error': 'No such property with the provided propid exists in the '
    #           'sc-tenants.yml file.'}
    # eg3 = {'code': 'failure', 'error': '[Errno 54] Connection reset by peer'}
    # eg4 = {'code': 'failure',
    #        'error': {'code': 'INVALID_BUILDING',
    #                  'message': 'The building id you specified is incorrect or not a '
    #                             'part of the property you are accessing.'}}

    # eg5= {
    #     'code': 'failure',
    #     'error': {'code': 'MISSING_TIME',
    #               'message': 'HMAC auth requires you to supply the time in header '
    #                          'x-sc-time.'}
    # }

    if 'error' in test_response and test_response['error']:
        print(f'Error in response is:{test_response["error"]}')

    if 'message' in test_response and test_response['message']:
        print(f'message in response is:\n{test_response["message"]}')

    if 'code' in test_response and test_response['code']:
        if test_response['code'] == 'failure':
            print(f'Code in response is: {test_response["code"]}', file=sys.stderr)
        else:
            print(f'Code in response is: {test_response["code"]}')


TEST_DEVICE_ALIAS_ID = 'TestDeviceAlias'
TEST_CLIENT = CLIENT_TYPE_ASYNC

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
            "0": [{"End": "0000", "Start": "0000"}],
            "1": [{"End": "1700", "Start": "0900"}],
            "2": [{"End": "2000", "Start": "0900"}],
            "3": [{"End": "1700", "Start": "0800"}],
            "4": [{"End": "1700", "Start": "0900"}],
            "5": [{"End": "1700", "Start": "1700"}],
            "6": [{"End": "1800", "Start": "0700"}],
        },
        "IsBuildingOperatingHours": True,
    },
}

TEST_READ_BUILDING_RESPONSE = {
    "status": 200,
    "message": "Success",
    "data": {},
}

TEST_READ_PROPERTY_RESPONSE = {
    "status": 200,
    "message": "Success",
    "data": {},
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
            "T": 0,
        }
    ],
    "Type": "INCIDENT",
    "Zone": "8a6ef71079e54af2884563e93c4ad800",
    "ZoneCatId": "MEETING_ROOMS",
    "ZoneName": "Meeting Room",
}


# region Find availability for incident Sample Response
# Test Response. Includes 2 Seat IDs. Seat 1 has Shift without task assigned,
# Seat 2 has task assigned, but shows 2 objects TODO: (why?)
# is it because it may have 2 tasks assigned to the same Shift?
# Datetime: 18 May 2021, 10:05 AM SGT
WORKFORCE_FIND_AVAILABILITY_RESPONSE_2 = {
    "message": "Available entries for given Zone",
    "data": {
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
    },
    "code": "SUCCESS",
}
# endregion


# region Assign Incident sample success response (forged manually)
# Created on 01 June 2021, 2:03 SGT
WORKFORCE_ASSIGN_INCIDENT_RESPONSE = {
    "message": "Incident has been successfully assigned to <seat_id>",
    "code": "SUCCESS"
}
# endregion


# region Sample response for Device Management
MOCK_RESPONSE_DEVICE_MGMT_REAL_SENSE_MIGRATED = {
    'ID': 'TestPID',
    'Migrated': False
}


MOCK_RESPONSE_DEVICE_MGMT_GET_DEVICE_SLOTS = {
    'Slots': [
        {'ATTR': 'attr#devices#info#ID',
         'Alias': 'TestAliasId',
         'Commissioned': 0,
         'Conn': 'BLE',
         'CreatedBy': 'smartclean',
         'CreatedOn': 1635494680,
         'DeviceNotAssociated': 0,
         'Devid': '55954A2B11',
         'Display': 'Paper Towel',
         'FirmwareVersion': '2',
         'ID': 'SCDevices#ID',
         'LID': '7911afb00468475da10ae8a57bdfe80b',
         'NS': 'DEVICE_INFO_GENERAL',
         'Org': 'LHN',
         'PID': 'TestPID',
         'Params': {'DeviceParams': {'MAX': 110, 'OFFSET': 5}},
         'ParamsNotConfigured': 1,
         'ParamsOnDeviceNotConfigured': 0,
         'PartnerId': 'SMARTCLEAN',
         'PropId': 'TestPropId',
         'ProviderOrg': 'SMARTCLEAN',
         'RequiresHealthCheck': 1,
         'RequiresOnDeviceConfiguration': 0,
         'RequiresParamsConfiguration': 1,
         'SRN': 'null',
         'TZ': 'Asia/Singapore',
         'Type': 'SMARTCLEAN#DevType',
         'Unhealthy': 0,
         'UpdatedBy': 'smartclean',
         'UpdatedOn': 1635496487,
         'ZoneId': 'ZoneID'}
    ],
    'code': 'SUCCESS',
    'message': 'Successfully fetched given slots'
}
# endregion


MOCK_RESPONSE_SEND_SMS = {
    "code": "SUCCESS",
    "message": "Successfully sent SMS to phone numbers"
}


# region Test desired Op in desired Service
def test_device_management_api(op: str, org: str, prop_id: str, pid: str, client: str, return_mock: bool = True):

    # Supply args to mocker to update the mock data

    if return_mock is True:
        response_mocker = test.data.SCDeviceManagement(client)
        _create_mock_resp = response_mocker.create_response_for_op(op)
        mock_response = _create_mock_resp['response']
        mock_response_status = _create_mock_resp['text']

        if mock_response is None:
            raise Exception(f'Failed to create mock response ({mock_response_status})')
        response = mock_response
    else:

        from SDK.SCDeviceManagement.API import SCDeviceManagement
        print("SCDevicemanagement imported from respective service directory.")
        scdevicemanagement = SCDeviceManagement()
        print("SCDeviceManagement instantiated.")

        test_client = CLIENT_TYPE_ASYNC

        if op == 'realSenseMigrated':
            response = scdevicemanagement.realSenseMigrated(
                org, pid, prop_id, test_client)

            print(f'{op} request complete. Response is:')
            print(response)
        else:

            request_body = {
                "Alias": ['cdf4ecd4fba24eb9834d65bdf6cff36f']
            }

            response = scdevicemanagement.getDeviceSlots(
                org, pid, prop_id, json.dumps(request_body), test_client
            )

            print("getDeviceSlots request. Response is:")
            print(response)

        print(
            f"{test_client} client was used for this request. Response will be parsed accordingly."
        )

        # region Parse response based on type of client
        # if test_client == CLIENT_TYPE_ASYNC:
        #     response_content = response
        #     print("Obtained response")
        # else:
        #     status_code = response.status_code
        #     print(f"Status code in this response is: {status_code}")
        #     response_content = response.json()
        #     print("Obtained .json() from response.")
        # endregion

    print("Type of response content is:")
    type_response = type(response)
    print(type_response)

    # if type_response is HTTPClientError or type_response is HTTPTimeoutError:
    #     _status_text = "Error in HTTP Request by sc-python-sdk"
    #     _err_text = response_content.message
    #     _status_code = response_content.code
    #     return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
    #     print(return_text)
    #     return
    # Example of error response:
    # Error in HTTP Request by sc-python-sdk: code: 400| message: Bad Request
    print("Keys in Response content is:")
    print(list(response.keys()))

    print('Response content is:')
    print(pformat(response))

    return response


def test_grids_api(op: str, org: str, pid: str, client: str, return_mock: bool = True):

    # SUpply args to mocker to update the mock data

    if return_mock is True:
        response_mocker = test.data.SCGrids(client)
        _create_mock_resp = response_mocker.create_response_for_op(op)
        mock_response = _create_mock_resp['response']
        mock_response_status = _create_mock_resp['text']

        if mock_response is None:
            raise Exception(f'Failed to create mock response ({mock_response_status})')
        response_content = mock_response

    else:

        from SDK.SCGridsServices.API import SCGrids
        print('SCGrids imported from respective service directory.')
        grids = SCGrids()
        print('SCGrids instantiated.')

        test_client = TEST_CLIENT

        if op == GRIDS_OP_GET_ZONE_INFO:
            zone_id = os.environ["TEST_ZONE_ID"]
            request_body = {"InsID": zone_id}
            response = grids.read_zone(org, pid, json.dumps(request_body), test_client)

            print(f'{op} request complete. Response is:')
            print(response)
        elif op == GRIDS_OP_GET_PROPERTY_INFO:
            prop_id = os.environ['TEST_PROP_ID']
            response = grids.readProperty(org, pid, prop_id, test_client)
        else:
            response = grids.readBuilding(org, pid, test_client)

        print(
            f"{test_client} client was used for this request. Response will be parsed accordingly."
        )

        # region Parse response based on type of client
        if test_client == CLIENT_TYPE_ASYNC:
            response_content = response
            print("Obtained response")
        else:
            status_code = response.status_code
            print(f"Status code in this response is: {status_code}")
            response_content = response.json()
            print("Obtained .json() from response.")
        # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return
    # Example of error response:
    # Error in HTTP Request by sc-python-sdk: code: 400| message: Bad Request
    print("Keys in Response content is:")
    print(list(response_content.keys()))

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content["data"]
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))

    return response_content


def test_workforce_apis(op: str, org: str, pid: str, prop_id: str, client: str, return_mock: bool = True):

    if org is None:
        org = os.environ["TEST_ORG"]

    if pid is None:
        pid = os.environ["TEST_PID"]

    if client is None:
        client = CLIENT_TYPE_ASYNC

    if return_mock is True:
        response_mocker = test.data.SCWorkforceManagement(client)
        _create_mock_resp = response_mocker.create_response_for_op(op)
        mock_response = _create_mock_resp['response']
        mock_response_status = _create_mock_resp['text']

        if mock_response is None:
            raise Exception(f'Failed to create mock response ({mock_response_status})')
        response_content = mock_response
    else:

        from SDK.SCWorkforceManagementServices.API import SCWorkforcemanagement
        print("SCWorkforcemanagement imported from respective service directory.")
        scworkforcemanagement = SCWorkforcemanagement()
        print("SCWorkforcemanagement instantiated.")

        test_client = TEST_CLIENT

        zone_id = os.environ["TEST_ZONE_ID"]
        # prop_id = os.environ['TEST_PROP_ID']
        if op == WORKFORCE_MGMT_OP_FIND_AVAILABILITY:
            curr_unix_time = int(time.time())
            end_unix_time = (
                    curr_unix_time + 900
            )  # Adding 15 minutes to current for due time.

            request_body = {
                "EndTime": end_unix_time,
                "ZoneID": [zone_id]
            }

            response = scworkforcemanagement.find_availability_for_incident(
                org, prop_id, pid, json.dumps(request_body), test_client
            )

            print(f'{op} request complete. Response is:')
            print(response)
        elif op == WORKFORCE_MGMT_OP_CREATE_INCIDENT_NO_ASSIGNEE:
            test_zone_details = {
                "zone_id": zone_id,
                "zone_category_id": f"Test Cat ID for ZoneID: {zone_id}",
                "zone_name": f"Test Name for ZoneID: {zone_id}",
            }

            request_body = {
                "Incident": _create_data_for_incident(test_zone_details)
            }

            response = scworkforcemanagement.createIncidentWithoutAssignee(
                org, prop_id, pid, json.dumps(request_body), test_client
            )
        elif op == WORKFORCE_MGMT_OP_GET_INCIDENT_SETTINGS:

            response = scworkforcemanagement.get_incident_settings(
                org, pid, prop_id, test_client)
        else:
            seat_id = os.environ['TEST_SEAT_ID']
            shift_id = os.environ['TEST_SHIFT_ID']
            incident_id = os.environ['TEST_INCIDENT_ID']

            request_body = {
                "SeatId": seat_id,
                "ShiftID": shift_id,
                "zoneId": zone_id,
                "IncidentID": incident_id
            }

            response = scworkforcemanagement.assign_shift_to_incident(
                org, prop_id, pid, json.dumps(request_body), test_client)

        print(
            f"{test_client} client was used for this request. Response will be parsed accordingly."
        )

        # region Parse response based on type of client
        if test_client == CLIENT_TYPE_ASYNC:
            response_content = response
            print("Obtained response")
        else:
            status_code = response.status_code
            print(f"Status code in this response is: {status_code}")
            response_content = response.json()
            print("Obtained .json() from response.")
        # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return
    # Example of error response:
    # Error in HTTP Request by sc-python-sdk: code: 400| message: Bad Request
    print("Keys in Response content is:")
    print(list(response_content.keys()))

    print('Response content is:')
    print(pformat(response_content))

    return response_content


def test_sms_gateway_apis(op: str, org: str, prop_id: str, pid: str, client: str, return_mock: bool = True):

    # Supply args to mocker to update the mock data

    if return_mock is True:
        response_mocker = test.data.SCMessageService(client)
        _create_mock_resp = response_mocker.create_response_for_op(op)
        mock_response = _create_mock_resp['response']
        mock_response_status = _create_mock_resp['text']

        if mock_response is None:
            raise Exception(f'Failed to create mock response ({mock_response_status})')
        response_content = mock_response

    else:
        from SDK.SCSMSGateway.API import SCSMSGateway
        print("SCSMSGateway imported from respective service directory.")
        sc_sms_gateway = SCSMSGateway()
        print("SCSMSGateway instantiated.")

        test_client = TEST_CLIENT

        from test import sms_gateway
        if op == sms_gateway.OP_PUBLISH_SMS:
            _request_data = {
                "Country": "Asia/Kolkata",
                "Who": "+918596866725",
                "Message": "New incident reported by PT Device ID: a1e2runjnkjnd899e898ncja in location Male Washroom, Level 1. Please resolve - Pemimpin"
            }

            exp_json = json.dumps(_request_data)
            response = sc_sms_gateway.publishSMS(
                org, pid, prop_id, exp_json, test_client)

            print(f'{op} request complete. Response is:')
            print(response)
        else:
            raise Exception(f'{op} is not supported for this service')

        print(
            f"{test_client} client was used for this request. Response will be parsed accordingly."
        )

        # region Parse response based on type of client
        if test_client == CLIENT_TYPE_ASYNC:
            response_content = response
            print("Obtained response")
        else:
            status_code = response.status_code
            print(f"Status code in this response is: {status_code}")
            response_content = response.json()
            print("Obtained .json() from response.")
        # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return
    # Example of error response:
    # Error in HTTP Request by sc-python-sdk: code: 400| message: Bad Request
    print("Keys in Response content is:")
    print(list(response_content.keys()))

    print('Response content is:')
    print(pformat(response_content))
    return response_content


def test_partners_solutions_op(op: str, org: str, prop_id: str, client: str, return_mock: bool = True):

    # Supply args to mocker to update the mock data

    solution_id = 'testSolution1'
    # pid = 'scnoop'

    if return_mock is True:
        response_mocker = test.data.SCPartnersSolutions(client)
        _create_mock_resp = response_mocker.create_response_for_op(op)
        mock_response = _create_mock_resp['response']
        mock_response_status = _create_mock_resp['text']

        if mock_response is None:
            raise Exception(f'Failed to create mock response ({mock_response_status})')
        response_content = mock_response

        # if op == partners_solutions.OP_GET_SOLUTION_FOR_PROPERTY:
        #     data = {
        #         "ATTR": "testSolution1",
        #         "Created": "1645688949",
        #         "ID": "testProperty",
        #         "Logs": [
        #             {
        #                 "comment": "Solution added to Property",
        #                 "unixTime": "1645688949"
        #             }
        #         ],
        #         "NS": "SOLUTION_ASSOC",
        #         "Org": "scnoop",
        #         "PartnerId": "P1",
        #         "PropertyId": "testProperty",
        #         "SRN": "srn:solution:SMARTCLEAN:::testProperty:SOLUTION_ASSOC:P1",
        #         "Status": "ACTIVATION_REQUEST_SUBMITTED"
        #     }

    else:
        print('Mock is False, will request the real service !')
        from SDK.SCPartnersSolutions.API import SCPartnersSolutions
        print("SCPartnersSolutions imported from respective service directory.")
        service = SCPartnersSolutions()
        print("SCPartnersSolutions instantiated.")

        test_client = TEST_CLIENT

        from test import partners_solutions
        if op == partners_solutions.OP_ADD_SOLUTION_TO_PROPERTY:
            response = service.addSolutionToProperty(org, prop_id, solution_id, test_client)
        elif op == partners_solutions.OP_GET_SOLUTION_FOR_PROPERTY:
            response = service.getSolutionForProperty(org, prop_id, solution_id, test_client)
        elif op == partners_solutions.OP_LIST_ALL_SOLUTIONS_FOR_PROPERTY:
            response = service.listAllSolutionsForProperty(org, prop_id, test_client)
        elif op == partners_solutions.OP_APPROVE_SOLUTION_FOR_PROPERTY:
            response = service.approveSolutionForProperty(org, prop_id, solution_id, test_client)
        elif op == partners_solutions.OP_DENY_SOLUTION_FOR_PROPERTY:
            response = service.denySolutionForProperty(org, prop_id, solution_id, test_client)
        else:
            raise Exception(f'{op} is not supported for this service')

        print(f'{op} request complete. Response is:')
        print(response)

        print(
            f"{test_client} client was used for this request. Response will be parsed accordingly."
        )

        # region Parse response based on type of client
        if test_client == CLIENT_TYPE_ASYNC:
            response_content = response
            print("Obtained response")
        else:
            status_code = response.status_code
            print(f"Status code in this response is: {status_code}")
            response_content = response.json()
            print("Obtained .json() from response.")
        # endregion

    print("Type of response content is:")
    type_response = type(response_content)
    print(type_response)

    if type_response is HTTPClientError or type_response is HTTPTimeoutError:
        _status_text = "Error in HTTP Request by sc-python-sdk"
        _err_text = response_content.message
        _status_code = response_content.code
        return_text = f"{_status_text}: code: {_status_code}| message: {_err_text}"
        print(return_text)
        return
    # Example of error response:
    # Error in HTTP Request by sc-python-sdk: code: 400| message: Bad Request
    print("Keys in Response content is:")
    print(list(response_content.keys()))

    print('Response content is:')
    print(pformat(response_content))
    return response_content
# endregion


def parse_sdk_response(client_type: str, sdk_response: any):

    data_return = {
        'data': None,
        'text': 'default'
    }

    print(f'Parsing given SDK Response: {sdk_response} based on client type: {client_type}')

    # region Parse response based on type of client
    if client_type == CLIENT_TYPE_ASYNC:
        _status_text = 'Obtained desired data from SDK response'
        print(f'For {client_type} clients, desired data is what is returned by SDK')
        data_return['text'] = _status_text
        data_return['data'] = _status_text
        return data_return

    print(f'For {client_type} clients, desired data needs to be extracted via HTTP response attributes.')
    status_code = sdk_response.status_code
    _status_code_status_text = f"response.status_code is: {status_code}"
    print(_status_code_status_text)

    status_codes_for_success = {200, 201}

    if status_code not in status_codes_for_success:
        data_return['text'] = f'Cannot get desired data ({_status_code_status_text})'
        return data_return

    try:
        response_content = sdk_response.json()
    except Exception as err:
        _err_type = type(err).__name__
        _err_text = str(err)
        err_info = f'{_err_type} trying to deserialize response using JSON ({_err_text})'
        data_return['text'] = err_info
        return data_return
    print("Obtained .json() from response.")
    # endregion


if __name__ == "__main__":

    # test_sdk_utils()

    # print('\nWaiting 2 seconds before running next test')
    # time.sleep(2)

    test_op_in_service(
        service=SERVICE_ID_WORKFORCE_MANAGEMENT,
        op=WORKFORCE_MGMT_OP_GET_INCIDENT_SETTINGS,
        return_mock=True
    )
