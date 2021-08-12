from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_METRICS_HOST"
PROTOCOL = "SC_METRICS_HTTP_PROTOCOL"
PORT = "SC_METRICS_PORT"
apiversion = "v4"


class SCMetrics:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/scmetrics"
                print("SCMETRICS: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCMETRICS: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion=apiversion, port=port, service="SCMetrics"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion=apiversion, port=port, service="SCMetrics"
                )
            else:
                print("SCMETRICS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCMetrics"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCMetrics"
                )

        except Exception as e:
            print("Exception " + str(e))

    def getModuleMetrics(self, org, pid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        return res

    def getModuleTSMetrics(self, org, pid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleTSMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleTSMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        return res
