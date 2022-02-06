from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_SMS_GATEWAY_HOST"
PROTOCOL = "SC_SMS_GATEWAY_HTTP_PROTOCOL"
PORT = "SC_SMS_GATEWAY_PORT"
apiversion = "v1"


class SCSMSGateway:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/smsgateway"
                print("SMSGATEWAY: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SMSGATEWAY: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="smsgateway"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="smsgateway"
                )

            else:
                print("SMSGATEWAY: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="smsgateway"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="smsgateway"
                )

        except Exception as e:
            print("Exception " + str(e))

    def publishSMS(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="smsgateway.publishSMS",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="smsgateway.publishSMS",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res
