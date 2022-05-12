import os

# Checking if the credentials
def credential_checker(filtered_credentials: dict):

    if (
        "sc_access_key" not in filtered_credentials
        or "sc_secret_key" not in filtered_credentials
    ):
        return {
            "code": "failure",
            "error": f"Either 'sc_access_key' or 'sc_secret_key' is not provided in the sc-tenants.yml file.",
        }
    elif (
        not filtered_credentials["sc_access_key"]
        or not filtered_credentials["sc_secret_key"]
    ):
        return {
            "code": "failure",
            "error": f"Either 'sc_access_key' or 'sc_secret_key' value is not provided in the sc-tenants.yml file.",
        }

    return {"code": "success", "data": f"All values are provided."}


def db_checker(absolute_path_tenants_database: str):

    code = "failure"
    response = (
        "Desired tenants database is not present. Please atleast register one property."
    )

    if os.path.isfile(absolute_path_tenants_database):
        if os.path.getsize(absolute_path_tenants_database) > 100:
            with open(absolute_path_tenants_database, "r", encoding="ISO-8859-1") as f:
                header = f.read(100)
                if header.startswith("SQLite format 3"):
                    print("SQLite3 database has been detected.")
                    code = "success"
                    response = "Desired tenants database is present."

    return {"code": code, "data": response}
