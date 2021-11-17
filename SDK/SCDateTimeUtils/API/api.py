from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_DATETIMEUTILS_HOST"
PROTOCOL = "SC_DATETIMEUTILS_HTTP_PROTOCOL"
PORT = "SC_DATETIMEUTILS_PORT"
apiversion = "v1"


class SCDatetimeutils:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/datetime"
                print("SCDATETIMEUTILS: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCDATETIMEUTILS: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix,
                    uri,
                    apiversion=apiversion,
                    port=port,
                    service="SCDatetimeutils",
                )
                self.Sync_client.initializeForService(
                    prefix,
                    uri,
                    apiversion=apiversion,
                    port=port,
                    service="SCDatetimeutils",
                )
            else:
                print("SCDATETIMEUTILS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCDatetimeutils"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCDatetimeutils"
                )

        except Exception as e:
            print("Exception " + str(e))

    def getDateTimeForFrequency(self, org, pid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scdatetimeutils.getDateTimeForFrequency",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scdatetimeutils.getDateTimeForFrequency",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        return res