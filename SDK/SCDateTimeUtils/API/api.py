from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os
from urllib.request import urlopen

HOST = "SC_DATETIMEUTILS_HOST"
PROTOCOL = "SC_DATETIMEUTILS_HTTP_PROTOCOL"
PORT = "SC_DATETIMEUTILS_PORT"


class SCDatetimeutils:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:

            url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            apiversion = data_json["modules"]["datetime"]["version"]
            base = data_json["base"]

            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = f"{base}/datetime"
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
                    service="datetime",
                )
                self.Sync_client.initializeForService(
                    prefix,
                    uri,
                    apiversion=apiversion,
                    port=port,
                    service="datetime",
                )
            else:
                print("SCDATETIMEUTILS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="datetime"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="datetime"
                )

        except Exception as e:
            print("Exception " + str(e))

    def getDateTimeForFrequency(self, org, pid, propid=None, expJson="{}", client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scdatetimeutils.getDateTimeForFrequency",
                org=org,
                pid=pid,
                propid=propid,
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scdatetimeutils.getDateTimeForFrequency",
                org=org,
                pid=pid,
                propid=propid,
                body=json.loads(expJson),
            )
        return res
