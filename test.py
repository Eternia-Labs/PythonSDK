import os
import json
from pprint import pformat

# from SDK.SCGridsServices.API import *
# print('Warning: Everything imported from Grids service directory...')
# from SDK.SCDashboardServices.API import *
# from SDK.SCMetricsServices.API import *
# from SDK.SCBIServices.API import *
# grids = SCGrids()
# dashboard = SCDashboard()
# metrics = SCMetrics()
# bi = SCBi()

LOAD_ENV_VARS = True

# region Default Data for tests
TEST_ORG = 'SMARTCLEAN'
TEST_PID = 'scnoop'
TEST_PROP_ID_LOCAL = 'ff47033487244e17a6d96df2a233a1a0'
TEST_PROP_ID_REMOTE = '3b749a681d14446292b6c79b48403bbd'
CLIENT_TYPE_ASYNC = 'Async'
CLIENT_TYPE_SYNC = 'Sync'
# endregion


def test_grids_function(org: str = None, pid: str = None, local: bool = True, test_client=CLIENT_TYPE_ASYNC):

    print('Starting test for a function in Grids service..')

    if org is None:
        org = TEST_ORG
    if pid is None:
        pid = TEST_PID

    if local is True:
        prop_id = TEST_PROP_ID_LOCAL
    else:
        prop_id = TEST_PROP_ID_REMOTE

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
        print('Response is:')
        print(pformat(response_content))
    else:
        status_code = read_prop_resp.status_code
        print(f'Status code in this response is: {status_code}')
        response_content = read_prop_resp.json()
        print('Obtained .json() from response. response.json() is:')
        print(pformat(response_content))
    # endregion


def _test_get_reporting_services_for_principal():
    from SDK.SCBIServices.API import SCBi
    bi = SCBi()
    request_body = {}
    response = bi.getReportingServicesForPrincipalOrg(
        TEST_ORG, TEST_PID, expJson=json.dumps(request_body), client='Sync')
    response_content = response.json()
    print(pformat(response_content))


def load_env_vars(dotenv_filepath: str = None):

    if dotenv_filepath is not None:
        # print('Loading env variables from dotenv file')
        # root_dir = os.path.dirname(os.path.abspath(__file__))
        # filepath = f'{root_dir}/env-dev.env'
        raise Exception('Currently not loading vars from dotenv file (TODO later)')

    os.environ['USER_NAME_PYTHONSDK'] = 'scbot'
    print('USER_NAME_PYTHONSDK set in environment.')
    os.environ['PASSWORD_PYTHONSDK'] = 'dummy-password'
    print('PASSWORD_PYTHONSDK set in environment.')


def run_test():

    if LOAD_ENV_VARS is True:
        load_env_vars()
    test_grids_function()


if __name__ == '__main__':

    run_test()
