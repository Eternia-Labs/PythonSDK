import sys
sys.path.append('/Users/mahendren/Desktop/PythonSDK')
import Client.client
import json
import tornado.ioloop



class SCML:
    def __init__(self):
        self.scmlClient = Client.getClient()

    def getExperiment(self,pid,expid):
        json_data = {"expid":str(expid)}
        res =  self.scmlClient.makeRequestV2(httpmethod='POST',op='scmlexperiments.getExperiment',pid=pid,body=json_data)
        return res
       

    def listExperiments(self,pid):
        res = self.scmlClient.makeRequestV2('GET',op='scmlexperiments.listExperiments',pid=pid) 
        return res
        

    def getLatestRun(self,pid,expid):
        json_data = {"expid":str(expid)}
        res = self.scmlClient.makeRequestV2('POST','scmlexperiments.getLatestRun',pid=pid,body=json_data)
        return res

    def getRunForExperiment(self,pid,expid,run):
        json_data = {"expid":str(expid),"run":str(run)}
        res =  self.scmlClient.makeRequestV2('POST','scmlexperiments.getRunForExperiment',pid=pid,body=json_data)
        return res

    def getLastNRuns(self,pid,expid,N):
        json_data = {"expid":str(expid),"N":str(N)}
        res =  self.scmlClient.makeRequestV2('POST','scmlexperiments.getLastNRuns',pid=pid,body=json_data)       
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

