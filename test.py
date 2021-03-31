import json
from pprint import pformat

# from SDK.SCGridsServices.API import *
# from SDK.SCDashboardServices.API import *
# from SDK.SCMetricsServices.API import *
# from SDK.SCBIServices.API import *
# grids = SCGrids()
# dashboard = SCDashboard()
# metrics = SCMetrics()
# bi = SCBi()


# region Default Data for tests
TEST_ORG = 'SMARTCLEAN'
TEST_PID = 'scnoop'
TEST_PROP_ID_LOCAL = 'ff47033487244e17a6d96df2a233a1a0'
TEST_PROP_ID_REMOTE = '3b749a681d14446292b6c79b48403bbd'
CLIENT_TYPE_ASYNC = 'Async'
CLIENT_TYPE_SYNC = 'Sync'
# endregion


def test_grids_function(org: str = None, pid: str = None, local: bool = True, test_client=CLIENT_TYPE_ASYNC):

    from SDK.SCGridsServices.API import SCGrids
    grids = SCGrids()

    if org is None:
        org = TEST_ORG
    if pid is None:
        pid = TEST_PID

    if local is True:
        prop_id = TEST_PROP_ID_LOCAL
    else:
        prop_id = TEST_PROP_ID_REMOTE

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


if __name__ == '__main':
    test_grids_function()
