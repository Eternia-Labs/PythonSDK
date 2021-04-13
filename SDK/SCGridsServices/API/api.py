from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = 'SC_GRIDS_HOST'
PROTOCOL = 'SC_GRIDS_HTTP_PROTOCOL'
PORT = 'SC_GRIDS_PORT'
apiversion = 'v1'

class SCGrids:
    def __init__(self): 
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()
        
    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri="console.smartclean.io/api/scgrids"
                print("SCGRIDS: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = 'https'
                print("SCGRIDS: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix,uri,port)
                self.Async_client.initializeForService(prefix,uri,apiversion,port,service='SCGrids')
                self.Sync_client.initializeForService(prefix,uri,apiversion,port,service='SCGrids')
               
            else:
                print("SCGRIDS: Port is not set")
                self.Async_client.initializeForService(prefix,uri,apiversion,service='SCGrids')
                self.Sync_client.initializeForService(prefix,uri,apiversion,service='SCGrids')
                
        except Exception as e:
            print("Exception "+ str(e))

    def listProperties(self,org,pid,client=None):
        if client == 'Sync':
            res = self.Sync_client.makeRequest(httpmethod='POST',op='scgrids.listProperties',org=org, pid=pid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scgrids.listProperties',org=org, pid=pid)
        return res

    def listBuilding(self,org,pid,propid,client=None):
        if client == 'Sync':
            res = self.Sync_client.makeRequest(httpmethod='POST',op='scgrids.listBuildingsByProperty',org=org, pid=pid ,propid=propid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scgrids.listBuildingsByProperty',org=org, pid=pid ,propid=propid)
        return res

    def readProperty(self,org,pid,propid,client=None):
        if client == 'Sync':
            res =  self.Sync_client.makeRequest(httpmethod='POST',op='scgrids.readProperty',org=org,pid=pid,propid=propid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scgrids.readProperty',org=org,pid=pid,propid=propid)
        return res
       
    def readBuilding(self,org,pid,client=None):
        if client == 'Sync':
            res =  self.Sync_client.makeRequest(httpmethod='POST',op='scgrids.readBuilding',org=org, pid =pid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scgrids.readBuilding',org=org, pid =pid)
        return res

    # TODO: Infer return type from downstream operation & put in signature (replace "-> any" with "-> <type>")
    def read_zone(self, org: str, pid: str, exp_json: str, client=None) -> any:
        """
        This gets the Zone given by it's ID for a Building

        :param org: Organisation ID
        :param pid: Project ID
        :param exp_json: Expected request body (as a JSON string)
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        if client == 'Sync':
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        _method = 'POST'
        _op = 'scgrids.readZone'

        request_kwargs = {
            'httpmethod': _method,
            'op': _op,
            'org': org,
            'pid': pid,
            'body': json.loads(exp_json)
        }

        res = _client_obj.makeRequest(**request_kwargs)
        return res
        
    def listBuildingMetrics(self,org,pid,client=None):
        if client == 'Sync':
            res =  self.Sync_client.makeRequest(httpmethod='POST',op='scgrids.listBuildingMetrics',org=org, pid =pid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scgrids.listBuildingMetrics',org=org, pid =pid)
        return res

    def listZonesByLevel(self,org,pid,expJson,client=None):
        if client == 'Sync':
            res =  self.Sync_client.makeRequest(httpmethod='POST',op='scgrids.listZonesByLevel',org=org, pid =pid, body=json.loads(expJson))
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scgrids.listZonesByLevel',org=org, pid =pid, body=json.loads(expJson))
        return res

    def listLevelsByBuilding(self,org,pid,client=None):
        if client == 'Sync':
            res =  self.Sync_client.makeRequest(httpmethod='POST',op='scgrids.listLevelsByBuilding',org=org, pid=pid)
        else:
            res = self.Async_client.makeRequest(httpmethod='POST',op='scgrids.listLevelsByBuilding',org=org, pid=pid)
        return res

