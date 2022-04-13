# PythonSDK

## Important Step:

For installing Pycurl mentioned in the requirements.txt
(For macOS Big Sur)

export CPPFLAGS=-I/usr/local/opt/openssl/include
export LDFLAGS=-L/usr/local/opt/openssl/lib
pip install pycurl --global-option="--with-openssl"

If not installed in this way, it would throw error : ImportError: pycurl: libcurl link-time ssl backend (openssl) is different from compile-time ssl backend.


## User Tips (Manually Add SDK to client repository):

1. Open PythonSDK and copy the "SDK" directory inside it
2. Paste above copied directory inside the client repository
   Recommended: Python Client repository should have virtual environment.
   Suppose name of virtual environment in the Python client repository is "venv", then: 
    - Paste the above copied directory inside: venv/lib/Python3.x/site-packages
3. Open requirements.txt and install all the listed dependencies in virtual environment of the Python client repository



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

#### HMAC Signed Async Requests (Signing Enabled)
1. Ensure pycurl (version: 7.43.0.6) is installed with the global option (with-openssl)
- If not, run the following command in the project environment:
`pip install pycurl==7.43.0.6 --global-option="--with-openssl"`
2. Ensure CurlAsyncHTTPClient is used for the tornado AsyncHTTPClient 
- In SDK/ClientAsync/clientasync.py, the following line must be available and not commented:
`AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")`
- Note When Signing is disabled this may cause some problems (so this is strictly for usage with Signing enabled)
3. Ensure Signing is enabled
- Environment variable SIGNING_STATUS_PYTHONSDK must be set to "Enabled")
4. Ensure credentials (Access Key and Secret Key) are registered for desired Property
- By manually updating the sc-tenants.yml file. Add the Access Key and Secret Key for desired PropertyID.

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

[comment]: <> (#### For using it locally:)

##### Set the environment variables for the corresponding service:

###### SC_DASHBOARD
'SC_DASHBOARD_HOST'
'SC_DASHBOARD_HTTP_PROTOCOL'
'SC_DASHBOARD_PORT'

###### SC_GRIDS
'SC_GRIDS_HOST'
'SC_GRIDS_HTTP_PROTOCOL'
'SC_GRIDS_PORT'

###### SC_BI
'SC_BI_HOST'
'SC_BI_HTTP_PROTOCOL'
'SC_BI_PORT'

###### SC_METRICS
'SC_METRICS_HOST'
'SC_METRICS_HTTP_PROTOCOL'
'SC_METRICS_PORT'

###### SC_WORKFORCEMANAGEMENT
'SC_WORKFORCEMANAGEMENT_HOST'
'SC_WORKFORCEMANAGEMENT_HTTP_PROTOCOL'
'SC_WORKFORCEMANAGEMENT_PORT'

###### PROTOCOL is http or https.

[comment]: <> (#### For not using it locally:)

[comment]: <> (Signing is not enabled. It is "Disabled" by default. You can enable it by setting the environment variables.)

[comment]: <> ('SIGNING_STATUS_PYTHONSDK' &#40;"Enabled"&#41;)

[comment]: <> ('USER_NAME_PYTHONSDK' &#40;<user_name>&#41;)

[comment]: <> ('PASSWORD_PYTHONSDK' &#40;<password>&#41;)
