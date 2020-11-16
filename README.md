# PythonSDK

## Setup steps

1. Clone repo
2. Activate virtualenv and cd to folder PythonSDK
3. Build a wheel - python3 setup.py sdist bdist_wheel
4. pip install -e /path/to/the/root_folder/containing/setup.py  for installing a build distribution from local folder


##### Usage:

from optimus.services.SCML import *  
import json 

config_json = json.dumps(configjson)

se = SCMLExperiments()  

se.getExperiment(PID,EXPID)  
se.createExperiment(pid,config_json)
