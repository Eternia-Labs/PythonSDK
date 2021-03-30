from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = 'SC_WORKFORCEMANAGEMENT_HOST'
PROTOCOL = 'SC_WORKFORCEMANAGEMENT_HTTP_PROTOCOL'
PORT = 'SC_WORKFORCEMANAGEMENT_PORT'
apiversion = 'v1'

class SCBi:
    def __init__(self): 
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()
        
    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri="console.smartclean.io/api/scworkforcemanagement"
                print("SCWORKFORCEMANAGEMENT: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = 'https'
                print("SCWORKFORCEMANAGEMENT: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix,uri,port)
                self.Async_client.initializeForService(prefix,uri,port,apiversion,service='SCWorkforceManagement')
                self.Sync_client.initializeForService(prefix,uri,port,apiversion,service='SCWorkforceManagement')
            else:
                print("SCWORKFORCEMANAGEMENT: Port is not set")
                self.Async_client.initializeForService(prefix,uri,apiversion,service='SCWorkforceManagement')
                self.Sync_client.initializeForService(prefix,uri,apiversion,service='SCWorkforceManagement')
        except Exception as e:
            print("Exception "+ str(e))

    def createIncidentWithoutAssignee(self,org,pid,expJson,client=None):
        if client == 'Sync':
            res = self.Sync_client.makeRequest(httpmethod='POST', op='scteams.createIncidentWithoutAssignee', body=json.loads(expJson), org=org, pid=pid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST', op='scteams.createIncidentWithoutAssignee', body=json.loads(expJson), org=org, pid=pid)
        return res
    
    
    


