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


def deregister_credentials_for_property(property_id: str) -> dict:

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

    # Deleting credentials for a particular property id.
    conn.execute("DELETE from Tenants where PropID = (?)", (property_id,))
    conn.commit()

    response_data["success"] = True
    response_data[
        "text"
    ] = f"Successfully removed credentials for Property (ID: {property_id})"
    return response_data
