from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os
from urllib.request import urlopen

HOST = "SC_METRICS_HOST"
PROTOCOL = "SC_METRICS_HTTP_PROTOCOL"
PORT = "SC_METRICS_PORT"


class SCMetrics:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:

            url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            apiversion = data_json["modules"]["scmetrics"]["version"]
            base = data_json["base"]

            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = f"{base}/scmetrics"
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
                    prefix, uri, apiversion=apiversion, port=port, service="scmetrics"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion=apiversion, port=port, service="scmetrics"
                )
            else:
                print("SCMETRICS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="scmetrics"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="scmetrics"
                )

        except Exception as e:
            print("Exception " + str(e))

    def getModuleMetrics(self, org, pid, propid=None, expJson="{}", client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
                propid=propid,
            )
        return res

    def getModuleTSMetrics(self, org, pid, propid=None, expJson="{}", client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleTSMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scmetrics.getModuleTSMetrics",
                org=org,
                pid=pid,
                body=json.loads(expJson),
                propid=propid,
            )
        return res
