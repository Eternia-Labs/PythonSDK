from optimus.Client import client
import json
import tornado.ioloop
import os

HOST = 'SCML_EXPERIMENTS_HOST'
PROTOCOL = 'HTTP_PROTOCOL'
PORT = 'PORT'

class SCMLExperiments:
    def __init__(self): 
        self.scmlClient = client.getClient()
        self.initialize()
        

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri="127.0.0.1"
                print("Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = 'http'
                print("protocol env variable is not set")
            if os.getenv(PORT):
                print("port is not set")
                port = os.getenv(PORT)
            else:
                port = 5000
            self.scmlClient.initializeForService(prefix,uri,port,'SCMLExperiments')
        except Exception:
            raise Exception()
        

    def getExperiment(self,pid,expid):
        json_data = {"expid":str(expid)}
        res =  self.scmlClient.makeRequest(httpmethod='POST',op='scmlexperiments.getExperiment',pid=pid,body=json_data)
        return res
       

    def listExperiments(self,pid):
        res = self.scmlClient.makeRequest('GET',op='scmlexperiments.listExperiments',pid=pid) 
        return res
        

    def getLatestRun(self,pid,expid):
        json_data = {"expid":str(expid)}
        res = self.scmlClient.makeRequest('POST','scmlexperiments.getLatestRun',pid=pid,body=json_data)
        return res

    def getRunForExperiment(self,pid,expid,run):
        json_data = {"expid":str(expid),"run":str(run)}
        res =  self.scmlClient.makeRequest('POST','scmlexperiments.getRunForExperiment',pid=pid,body=json_data)
        return res

    def getLastNRuns(self,pid,expid,N):
        json_data = {"expid":str(expid),"N":str(N)}
        res =  self.scmlClient.makeRequest('POST','scmlexperiments.getLastNRuns',pid=pid,body=json_data)       
        return res
    

    def getQueryConfig(self,pid,expid):
        obj = self.getExperiment(pid,expid)
        return obj['config']['query']
    
    def getAlgorithmConfig(self,pid,expid):
        obj = self.getExperiment(pid,expid)
        return obj['config']['algorithm']

    def getPredictionConfig(self,pid,expid):
        obj = self.getExperiment(pid,expid)
        return obj['config']['prediction']
    
    def getExperimentState(self,pid,expid):
        obj = self.getExperiment(pid,expid)
        return obj['State']

    def getExperimentIds(self,pid):
        res = self.getExperiments(pid)
        ids = []
        for item in res:
            ids.append(item['ExperimentId'])
        return ids

