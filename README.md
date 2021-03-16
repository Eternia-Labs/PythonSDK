# PythonSDK

## Setup steps

1. Clone repo
2. Activate virtualenv and cd to folder PythonSDK
3. Build a wheel - python3 setup.py sdist bdist_wheel
4. pip install -e /path/to/the/root_folder/containing/setup.py  for installing a build distribution from local folder


#### Usage:

from SCGrids.services.Tasks import * 
import json

tasks = SCGrids()


tasks.listZonesByLevel(ORG,PID,jsondata) 


#### Sample:

from SCGrids.services.Tasks import * 
import json

tasks = SCGrids()

json_data = {
    "LID": "{{lid}}"
}

jsondata = json.dumps(json_data)
 
tasks.listZonesByLevel('SMARTCLEAN','test',jsondata)

#### For using the Sync Client:

Property = grids.readProperty(org=org,pid = 'scnoop',propid = PropId,client='Sync')

##### For json data:
print(Property.json())

#### For using the Async Client:

Property = grids.readProperty(org=org,pid = 'scnoop',propid = PropId,client='Async')

(or)

Property = grids.readProperty(org=org,pid = 'scnoop',propid = PropId)

##### For json data:
print(Property)

#### For using it locally:

##### Set the environment variables for the corresponding service:

###### SC_DASHBOARD
HOST = 'SC_DASHBOARD_HOST'
PROTOCOL = 'SC_DASHBOARD_HTTP_PROTOCOL'
PORT = 'SC_DASHBOARD_PORT'

###### SC_GRIDS
HOST = 'SC_GRIDS_HOST'
PROTOCOL = 'SC_GRIDS_HTTP_PROTOCOL'
PORT = 'SC_GRIDS_PORT'

###### SC_BI
HOST = 'SC_BI_HOST'
PROTOCOL = 'SC_BI_HTTP_PROTOCOL'
PORT = 'SC_BI_PORT'

###### SC_METRICS
HOST = 'SC_METRICS_HOST'
PROTOCOL = 'SC_METRICS_HTTP_PROTOCOL'
PORT = 'SC_METRICS_PORT'

###### PROTOCOL is http or https.

#### For not using it locally:

###### Simply run the code and use it. Authentication for now is added but it will be removed in future and will be left on user to provide it.


