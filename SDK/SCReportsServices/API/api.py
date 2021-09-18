from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_REPORTS_HOST"
PROTOCOL = "SC_REPORTS_HTTP_PROTOCOL"
PORT = "SC_REPORTS_PORT"
apiversion = "v1"


class SCReports:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/screports"
                print("SCREPORTS: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCREPORTS: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="SCReports"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="SCReports"
                )
            else:
                print("SCREPORTS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCReports"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCReports"
                )
        except Exception as e:
            print("Exception " + str(e))

    def getDataForAttendanceKPIs(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="screports.getDataForAttendanceKPIs",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="screports.getDataForAttendanceKPIs",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res
