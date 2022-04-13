import time
from pprint import pformat

from SDK import utils


def test_util_register_creds_for_property():

    print('\nTesting util: register_credentials_for_property')

    property_id = 'test_property_id2'
    access_key = 'test_access_key10'
    secret_key = 'test_secret_key20'

    response = utils.register_credentials_for_property(property_id, access_key, secret_key)
    print(f'Test Response is:\n{pformat(response)}')


def test_util_deregister_creds_for_property():

    print('\nTesting util: deregister_credentials_for_property')

    from SDK import utils
    property_id = 'test_property_id2'

    response = utils.deregister_credentials_for_property(property_id)
    print(f'Test Response is:\n{pformat(response)}')


def test_utils():

    test_util_register_creds_for_property()

    print('Wait 2 seconds before next test...')
    time.sleep(2)

    test_util_deregister_creds_for_property()


if __name__ == '__main__':
    test_utils()
