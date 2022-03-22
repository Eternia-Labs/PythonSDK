from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os
from urllib.request import urlopen

HOST = "SC_DASHBOARD_HOST"
PROTOCOL = "SC_DASHBOARD_HTTP_PROTOCOL"
PORT = "SC_DASHBOARD_PORT"

class SCDashboard:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:

            url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            apiversion = data_json["modules"]["widgets"]["version"]
            base = data_json["base"]

            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = f"{base}/widgets"
                print("SCDASHBOARD: Host is not set")

            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCDASHBOARD: protocol env variable is not set")
                
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="widgets"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="widgets"
                )
            else:
                print("SCDASHBOARD: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="widgets"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="widgets"
                )
        except Exception as e:
            print("Exception " + str(e))

    def getWidgetImage(self, org, pid, expJson, propid=None, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scdashboard.getWidgetImage",
                body=json.loads(expJson),
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scdashboard.getWidgetImage",
                body=json.loads(expJson),
                propid=propid,
            )
        return res
