from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_TASKS_HOST"
PROTOCOL = "SC_TASKS_HTTP_PROTOCOL"
PORT = "SC_TASKS_PORT"
apiversion = "v1"


class SCTasks:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/scbi"
                print("SCTASKS: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCTASKS: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, port, apiversion, service="SCTasks"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, port, apiversion, service="SCTasks"
                )
            else:
                print("SCTASKS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCTasks"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCTasks"
                )
        except Exception as e:
            print("Exception " + str(e))

    def taskOperationsFailure(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="sctasks.taskOperationsFailure",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="sctasks.taskOperationsFailure",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def taskOperationsSuccess(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="sctasks.taskOperationsSuccess",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="sctasks.taskOperationsSuccess",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def taskOperationsStarted(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="sctasks.taskOperationsStarted",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="sctasks.taskOperationsStarted",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res
