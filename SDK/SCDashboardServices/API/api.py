from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_DASHBOARD_HOST"
PROTOCOL = "SC_DASHBOARD_HTTP_PROTOCOL"
PORT = "SC_DASHBOARD_PORT"
apiversion = "v1"


class SCDashboard:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/widgets"
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
                    prefix, uri, apiversion, port, service="SCDashboard"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="SCDashboard"
                )
            else:
                print("SCDASHBOARD: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCDashboard"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCDashboard"
                )
        except Exception as e:
            print("Exception " + str(e))

    def getWidgetImage(self, org, pid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scdashboard.getWidgetImage",
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scdashboard.getWidgetImage",
                body=json.loads(expJson),
            )
        return res
