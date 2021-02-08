from SCTasks.Client import client
import json
import tornado.ioloop
import os

HOST = 'SC_TASKS_HOST'
PROTOCOL = 'HTTP_PROTOCOL'
PORT = 'PORT'

class SCTasks:
    def __init__(self): 
        self.Client = client.getClient()
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
                port = os.getenv(PORT)
                self.Client.initializeForService(prefix,uri,port,service='SCTasks')
            else:
                print("Port is not set")
                self.Client.initializeForService(prefix,uri,'5001',service='SCTasks')
        except Exception as e:
            print("Exception "+ str(e))
        

    def addCustomTaskBuilding(self,pid,expJson):
        res =  self.Client.makeRequest(httpmethod='POST',op='sctasks.addCustomTaskForBuilding',pid=pid,body=json.loads(expJson))
        return res
       

    def addCustomTaskProperty(self,propid,expJson):
        res =  self.Client.makeRequest(httpmethod='POST',op='sctasks.addCustomTaskForProperty',propid=propid,body=json.loads(expJson))
        return res
        

    def queryTasks(self,pid,expJson):
        res = self.Client.makeRequest('POST','sctasks.queryTaskCatalog',pid=pid,body=json.loads(expJson))
        return res

    def createTaskGroup(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.createTaskGroup',pid=pid,body=json.loads(expJson))
        return res

    def queryTaskGroup(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.queryTaskGroupCatalog',pid=pid,body=json.loads(expJson))       
        return res
    
    def getTasksRelatedToTaskgrp(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.getTasksRelatedToTaskGrp',pid=pid,body=json.loads(expJson))       
        return res
    
    def getTaskGroups(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.getTaskGroups',pid=pid,body=json.loads(expJson))       
        return res

    def addTasksInTaskGroup(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.addTasksinTaskGroup',pid=pid,body=json.loads(expJson))       
        return res

    def deleteTasksinTaskGroup(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.deleteTasksinTaskGroup',pid=pid,body=json.loads(expJson))       
        return res
    
    def queryTaskCatalogPaginated(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.queryTaskCatalogPaginated',pid=pid,body=json.loads(expJson))       
        return res
    
    def queryTaskgroupCatalogPaginated(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.queryTaskGroupCatalogPaginated',pid=pid,body=json.loads(expJson))       
        return res

    def listTaskCategories(self):
        res =  self.Client.makeRequest('POST','sctasks.listTaskCategories')       
        return res
    
    def listAssets(self):
        res =  self.Client.makeRequest('POST','sctasks.listAssets')       
        return res

    def createTaskgroupToZoneCatAssoc(self,propid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.taskGroupsToZoneCatAssoc',propid=propid,body=json.loads(expJson))       
        return res

    def getTaskgroupForZoneCategory(self,propid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.getTaskGroupForZoneCategory',propid=propid,body=json.loads(expJson))       
        return res

    def createTaskgroupToZoneAssoc(self,pid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.taskGroupsToZoneAssoc',pid=pid,body=json.loads(expJson))       
        return res

    def getTaskGroupForZone(self,pid,propid,expJson):
        res =  self.Client.makeRequest('POST','sctasks.getTaskGroupForZone',pid=pid,propid=propid,body=json.loads(expJson))       
        return res


