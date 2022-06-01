import os
import sqlite3

_absolute_path_sdk_directory = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
print(f"Path to SDK directory is:\n{_absolute_path_sdk_directory}")
absolute_path_tenants_database = f"{_absolute_path_sdk_directory}/Tenants.db"
print(f"Path to sc-tenants database is:\n{absolute_path_tenants_database}")

"""Creating connection for the sqlite DB."""
conn = sqlite3.connect(absolute_path_tenants_database)
