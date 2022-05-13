import os
import sys
from pprint import pformat
import logger.logs

SYSTEM_BASE_URL = "localhost"
PRODUCT_ROOT_DIR = None
LOG = None


def check_system_base_url(log, request_base_url: str):
    """
    This function is executed for every request received.
    Checks if K8s Service URL is provided. If not, will set the SYSTEM_URL to the Base URL at which request received.
    """

    global SYSTEM_BASE_URL

    env_var_name_k8s_service_url = "KUBERNETES_SERVICE_URL"
    k8s_service_url = os.getenv(env_var_name_k8s_service_url)

    if k8s_service_url is None:
        log.debug(f'env: "{env_var_name_k8s_service_url}" is NOT set.')
        log.debug(f'Setting "SYSTEM_URL" to given Request Base URL:')
        log.info(request_base_url)
        SYSTEM_BASE_URL = request_base_url
    else:
        log.debug(f'env: "{env_var_name_k8s_service_url}" is set to:')
        log.debug(k8s_service_url)
        SYSTEM_BASE_URL = k8s_service_url


def init_app_logger():

    print("In settings.init_app_logger...")

    global LOG

    if LOG is None:
        print("App logger not yet initialized. Creating now...")
        log_obj = logger.logs.initialize_logger()
        LOG = log_obj
        print("App logger has been initialized and available in settings.")


def set_product_root_dir():
    """
    Get the directory above current file, and set it as the global variable.
    """

    global PRODUCT_ROOT_DIR
    if PRODUCT_ROOT_DIR is None:
        print("settings.PRODUCT_ROOT_DIR was not set.")
        PRODUCT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        print("Root directory is:")
        print(PRODUCT_ROOT_DIR)
