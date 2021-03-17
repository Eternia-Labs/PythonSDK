from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = 'SC_BI_HOST'
PROTOCOL = 'SC_BI_HTTP_PROTOCOL'
PORT = 'SC_BI_PORT'
apiversion = 'v2'

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
                uri="console.smartclean.io/api/scbi"
                print("SCBI: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = 'https'
                print("SCBI: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix,uri,port)
                self.Async_client.initializeForService(prefix,uri,port,apiversion,service='SCBi')
                self.Sync_client.initializeForService(prefix,uri,port,apiversion,service='SCBi')
            else:
                print("SCBI: Port is not set")
                self.Async_client.initializeForService(prefix,uri,apiversion,service='SCBi')
                self.Sync_client.initializeForService(prefix,uri,apiversion,service='SCBi')
        except Exception as e:
            print("Exception "+ str(e))

    def getReportingServicesForPrincipalOrg(self,org,pid,expJson,client=None):
        if client == 'Sync':
            res = self.Sync_client.makeRequest(httpmethod='POST',op='scbi.getReportingServicesForPrincipalOrg', body=json.loads(expJson),org=org)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scbi.getReportingServicesForPrincipalOrg', body=json.loads(expJson),org=org)
        return res
    
    def getReportingServicesForPrincipalBuilding(self,org,pid,expJson,client=None):
        if client == 'Sync':
            res = self.Sync_client.makeRequest(httpmethod='POST',op='scbi.getReportingServicesForPrincipalBuilding', body=json.loads(expJson),org=org, pid=pid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scbi.getReportingServicesForPrincipalBuilding', body=json.loads(expJson),org=org, pid=pid)
        return res

    


