# SmartClean Python SDK

## How to install and use it?

### Install required dependencies for the SDK
1. All required dependencies for this SDK must be installed in your python virtual environment.
2. These dependencies are listed inside the requirements.txt file within this repository. 
3. You may use "pip" to install these in your virtual environment. 

### Add the SDK
This can be done in either of two ways:
1. Copy the SDK folder in this repository, and paste it as a new folder inside your Python project
- For quick use, paste this in the root directory of your Python project. However, 
- It's recommended to paste this inside the virtual environment folder of your Python project
  (Refer to the section below: **Add SDK folder in your Python virtual environment**)
OR
2. Create a build (python wheel) within this repository and install the wheel in your project
- This approach is helpful, if you make any changes to the SDK and want to use this in your project instead.
  (Refer to section: )

**Important:** In either of above way to add the SDK, the dependencies (listed in requirements.txt) 
must be installed in the python environment in which the SDK will be used.

### Add the SDK (choice 1): 
Add the folder in your Python virtual environment

1. Open PythonSDK and copy the "SDK" directory inside it
2. Paste above copied directory inside your project 
   1. Recommended: Your repository should have a virtual environment first. 
   2. Suppose name of virtual environment in the Python client repository is "venv", then:
      - Paste the above copied directory inside: venv/lib/Python3.x/site-packages

### Add the SDK (choice 2):
Create a Python wheel on your system and install the wheel.

1. Clone or download this repository
2. Activate a virtual environment in the PythonSDK folder
3. Build a wheel using setuptools: `python3 setup.py sdist bdist_wheel`
   1. This creates a Python wheel (.whl file) inside a "dist" folder inside the PythonSDK repository.
4. Copy the absolute path to this wheel file and install this file in your Python project.
   1. For example using pip: `pip install pythonSDK-0.0.1-py3-none-any.whl`

### Authentication (important step before use)
All requests made using this SDK require authentication based on credentials provided for specific Properties.
- Each request requires a valid Property ID (propid)
- If credentials are not registered for the Property ID being used, then the requests will fail.

Before using any requests from the SDK, ensure the following:
1. You have the SC-HMAC credentials for the Property which you will pass to the request.
   1. You can request these from our representative (admin or tech team)
   2. The SC-HMAC credentials include an Access Key and a Secret Key
2. The credentials for the Property ID being used in the request are registered. 
   1. This only needs to be done once.
   2. Do this by calling the appropriate SDK utility function (register_credentials_for_property).
   3. This utility stores the given Access Key and Secret Key for the Property ID used in the request.
   4. For example, refer to below section: "Register credentials for a property".
   
Note: You may remove the stored credentials for a Property by calling the appropriate SDK utility function
- Refer to below section: "Deregister credentials for a property"

### Register credentials for a property (example)
Registration of credentials for a property is done so that you can access the details pertaining to that property if credentials get validated.
Example:
```python
from SDK.utils import register_credentials_for_property

response = register_credentials_for_property(property_id=<property_id>, access_key=<access_key>, secret_key=<secret_key>)
# property_id, access_key and secret_key need to be placed in the corresponding placeholders.
```

### Deregister credentials for a property (example)
Deregistration of credentials for a property is done so that you can delete the credentials pertaining to a property which may no longer be in use.

Example:
```python
from SDK.utils import deregister_credentials_for_property

response = deregister_credentials_for_property(property_id=<property_id>)
# property_id need to be placed in the corresponding placeholder.

```


### Example usage:
```python
from SDK.SCGridsServices.API import *
import json

grids = SCGrids()

Org='SMARTCLEAN'
Pid='test_pid'
PropId = 'test_propid'

json_data = {
    "LID": "{{lid}}"
}

jsondata = json.dumps(json_data)
 
zones = grids.listZonesByLevel(org=Org, pid=Pid, expJson=jsondata)

Pid = 'scnoop'

#For using the Sync Client:
Property = grids.readProperty(org=Org, pid=Pid, propid=PropId, client='Sync')
#For getting the Sync Client's data:
Property = Property.json()  
#For getting the Sync Client's status code:
Property_status_code = Property.status_code

# For using the Async Client:
Property = grids.readProperty(org=Org, pid= Pid, propid=PropId, client='Async')
# Or
Property = grids.readProperty(org=Org, pid= Pid, propid=PropId)
# Since Async Client is the default client
```

## Other Important things / common problems
### 1. Any problems installing the required dependency: pycurl?
This dependency must be installed with a custom option (see requirements.txt) 
If you install it manually (forgetting the custom option) it may cause an error on
some machines or operating systems and you may see the following error when using the SDK:

_ImportError: pycurl: libcurl link-time ssl backend (openssl) is different from compile-time ssl backend._

Solution:
Install pycurl with the required custom option: `pip install pycurl --global-option="--with-openssl"`

In case you get errors related to compiling openssl, try adding the following variables to your system path:
1. Set CPPFLAGS to your openssl/include folder
- `export CPPFLAGS=-I/usr/local/opt/openssl/include`
2. Set LDFLAGS to your openssl/lib folder
`export LDFLAGS=-L/usr/local/opt/openssl/lib`

### For assistance with any other issues or errors not documented here: 
Please create an issue in this github repository with the details
