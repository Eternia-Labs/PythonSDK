# PythonSDK

# How to install and use it?

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

#### HMAC Signed Async Requests (Signing Enabled)
1. Ensure pycurl (version: 7.43.0.6) is installed with the global option (with-openssl)
- If not, run the following command in the project environment:
`pip install pycurl==7.43.0.6 --global-option="--with-openssl"`
2. Ensure CurlAsyncHTTPClient is used for the tornado AsyncHTTPClient 
- In SDK/ClientAsync/clientasync.py, the following line must be available and not commented:
`AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")`
- Note When Signing is disabled this may cause some problems (so this is strictly for usage with Signing enabled)
3. Ensure credentials (Access Key and Secret Key) are registered for desired Property
- Refer to below section: "Register credentials for a property"

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

#### For using the Async Client:

Property = grids.readProperty(org=org,pid = 'scnoop',propid = PropId,client='Async')

(or)

Property = grids.readProperty(org=org,pid = 'scnoop',propid = PropId)

##### Set the environment variables for using the SDK.

Signing is "Enabled" by default. But it can be set manually too. 

SIGNING_STATUS_PYTHONSDK="Enabled"

# How to register and deregister credentials corresponding to properties?

## Register credentials for a property

Registration of credentials for a property is done so that you can access the details pertaining to that property if credentials get validated.

### Usage

from SDK.utils import *

response = register_credentials_for_property(property_id=<property_id>, access_key=<access_key>, secret_key=<secret_key>)

property_id, access_key and secret_key need to be placed in the corresponding placeholders.

## Deregister credentials for a property

Deregistration of credentials for a property is done so that you can delete the credentials pertaining to a property which may no longer be in use.

### Usage

from SDK.utils import *

response = deregister_credentials_for_property(property_id=<property_id>)

property_id need to be placed in the corresponding placeholder.



