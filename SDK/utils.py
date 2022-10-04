import logging

from SDK.helper.DB import *
from SDK.helper.helperFunctions import *


def register_credentials_for_property(
    property_id: str, access_key: str, secret_key: str
) -> dict:

    response_data = {"success": False, "text": "default"}

    # Check if Tenants DB exists.
    db_checked = db_checker(absolute_path_tenants_database)

    if db_checked["code"] == "failure":

        # Create Tenants table in the DB along with required parameters.
        conn.execute(
            """CREATE TABLE Tenants
            (
            PropID TEXT PRIMARY KEY NOT NULL,
            sc_access_key TEXT NOT NULL,
            sc_secret_key TEXT NOT NULL
            );"""
        )
        # endregion

    # region insert the data if property id exists or else update the data corresponding to the property id.
    conn.execute(
        """INSERT INTO Tenants (PropID,sc_access_key,sc_secret_key) VALUES(?, ?, ?) ON CONFLICT(PropID) 
        DO UPDATE SET sc_access_key=excluded.sc_access_key, sc_secret_key=excluded.sc_secret_key;""",
        (property_id, access_key, secret_key),
    )
    conn.commit()

    print("Updated credentials in tenants data for this property.")
    # endregion

    response_data["success"] = True
    response_data[
        "text"
    ] = f"Successfully registered given credentials for Property (ID: {property_id})"

    return response_data


def deregister_credentials_for_property(property_id: str, access_key: str) -> dict:

    response_data = {"success": False, "text": "default"}

    # Check if Tenants DB exists.
    db_checked = db_checker(absolute_path_tenants_database)

    if db_checked["code"] == "failure":
        return {"code": "failure", "error": db_checked["data"]}

    # Fetch access_key and secret_key for a particular property id.
    cursor = conn.execute(
        f"SELECT PropID,sc_access_key,sc_secret_key from Tenants where PropID = (?)",
        (property_id,),
    )
    data = cursor.fetchall()

    if not data:
        response_data["text"] = "Cannot find credentials in the tenants database."
        return response_data

    if access_key != data[0][1]:
        response_data[
            "text"
        ] = """Access key provided for the property is not correct. For deletion it should 
            match with the access key provided for a property while 
            registering credentials for the property."""
        return response_data    

    # Deleting credentials for a particular property id.
    conn.execute("DELETE from Tenants where PropID = (?)", (property_id,))
    conn.commit()

    response_data["success"] = True
    response_data[
        "text"
    ] = f"Successfully removed credentials for Property (ID: {property_id})"
    return response_data


def _get_std_log_level_from_input(log_level_input: str) -> int:

    input_all_caps = log_level_input.upper()

    log_level_by_input = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR
    }

    if input_all_caps in log_level_by_input:
        return log_level_by_input[input_all_caps]

    return logging.CRITICAL


def get_logger_for_module(module_name: str, log_level_input: str):

    _std_log_level = _get_std_log_level_from_input(log_level_input)

    module_logger = logging.getLogger(module_name)

    if module_logger.hasHandlers():
        module_logger.setLevel(_std_log_level)
        return module_logger

    logging.basicConfig(level=_std_log_level)

    module_logger = logging.getLogger(module_name)

    return module_logger
