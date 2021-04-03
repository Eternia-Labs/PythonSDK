import os
from pprint import pformat

from dotenv import load_dotenv

LOAD_ENV_VARS = True
EXTRACT_DATA_FROM_SDK_RESPONSE = True

CLIENT_TYPE_SYNC = 'Sync'
CLIENT_TYPE_ASYNC = 'Async'


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
        print('Response is:')
        print(pformat(response_content))
    else:
        status_code = read_prop_resp.status_code
        print(f'Status code in this response is: {status_code}')
        response_content = read_prop_resp.json()
        print('Obtained .json() from response. response.json() is:')
        print(pformat(response_content))
    # endregion

    if EXTRACT_DATA_FROM_SDK_RESPONSE is True:
        desired_data = response_content['data']
        print('Extracted "data" from response. Data is:')
        print(pformat(desired_data))
    else:
        print('Response content is:')
        print(pformat(response_content))


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
    test_get_property_info()


if __name__ == '__main__':
    run_test()
