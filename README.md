# PythonSDK

## Setup steps

1. Clone repo
2. Activate virtualenv and cd to folder PythonSDK
3. Build a wheel - python3 setup.py sdist bdist_wheel
4. pip install -e /path/to/the/root_folder/containing/setup.py  for installing a build distribution from local folder


##### Usage:

from SCTasks.services.Tasks import * 
import json 

jsondata = json.dumps(json_data)

tasks = SCTasks() 

tasks.addCustomTaskBuilding(PID,jsondata) 
tasks.listTaskCategories()

##### Sample:

from SCTasks.services.Tasks import * 
import json 

json_data = {
    "category": "My General Cleaning",
    "task": "test",
    "asset" : "Corners/Crevices",
    "measure" : 22,
    "measureName" : "Square Feet",json
    "skills" :  ["Cleaning"],
    "timeInMinutes" : 8
}

jsondata = json.dumps(json_data)
tasks = SCTasks() 

tasks.addCustomTaskBuilding('test',jsondata)


