import os
from pprint import pformat

import yaml


def register_credentials_for_property(property_id: str, access_key: str, secret_key: str) -> dict:

    response_data = {
        'success': False,
        'text': 'default'
    }

    # region Create absolute path to sc-tenants file
    _absolute_path_sdk_directory = os.path.dirname(os.path.abspath(__file__))
    print(f'Path to SDK directory is:\n{_absolute_path_sdk_directory}')
    absolute_path_tenants_file = f'{_absolute_path_sdk_directory}/sc-tenants.yml'
    print(f'Path to sc-tenants file is:\n{absolute_path_tenants_file}')
    # endregion

    # region Read data from the file, or create template data if file not found
    if os.path.isfile(absolute_path_tenants_file):
        # Read data from the desired file
        with open(absolute_path_tenants_file, mode='r') as _file_stream:
            sc_tenants_data = yaml.safe_load(_file_stream)
            print('Loaded data from sc-tenants file')
    else:
        # Start with desired template data
        sc_tenants_data = {'tenants': {}}
    # endregion

    # region update the data
    sc_tenants_data['tenants'][property_id] = {
        'sc_access_key': access_key,
        'sc_secret_key': secret_key
    }
    print('Updated credentials in tenants data for this property')
    # endregion

    # region write back the updated data to the same file
    with open(absolute_path_tenants_file, mode='w') as _file_stream:
        yaml.safe_dump(sc_tenants_data, _file_stream)
        print('Written updated credentials to the sc-tenants file.')
    # endregion

    response_data['success'] = True
    response_data['text'] = f'Successfully registered given credentials for Property (ID: {property_id})'
    return response_data


def deregister_credentials_for_property(property_id: str) -> dict:

    response_data = {
        'success': False,
        'text': 'default'
    }

    # region Create absolute path to sc-tenants file
    _absolute_path_sdk_directory = os.path.dirname(os.path.abspath(__file__))
    print(f'Path to SDK directory is:\n{_absolute_path_sdk_directory}')
    absolute_path_tenants_file = f'{_absolute_path_sdk_directory}/sc-tenants.yml'
    print(f'Path to sc-tenants file is:\n{absolute_path_tenants_file}')
    # endregion

    # Fails if desired file not found
    if not os.path.isfile(absolute_path_tenants_file):
        response_data['text'] = f'Desired file missing at path:\n{absolute_path_tenants_file}'
        return response_data

    # region Read the file, update the data and write back to the file
    with open(absolute_path_tenants_file, mode='r') as _file_stream:
        sc_tenants_data = yaml.safe_load(_file_stream)
        print('Loaded data from sc-tenants file')

    try:
        sc_tenants_data['tenants'].pop(property_id)
    except KeyError:
        response_data['text'] = f'No credentials found for Property (ID: {property_id})'
        return response_data

    print('Removed credentials in tenants data for this property')

    with open(absolute_path_tenants_file, mode='w') as _file_stream:
        yaml.safe_dump(sc_tenants_data, _file_stream)
        print('Written updated credentials to the sc-tenants file.')
    # endregion

    response_data['success'] = True
    response_data['text'] = f'Successfully removed credentials for Property (ID: {property_id})'
    return response_data


if __name__ == '__main__':
    property_id = 'test_property_id'
    access_key = 'test_access_key'
    secret_key = 'test_secret_key'

    response = register_credentials_for_property(property_id, access_key, secret_key)
    print(f'Response is:\n{pformat(response)}')
