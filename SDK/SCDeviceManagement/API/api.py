from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_DEVICE_MANAGEMENT_HOST"
PROTOCOL = "SC_DEVICE_MANAGEMENT_HTTP_PROTOCOL"
PORT = "SC_DEVICE_MANAGEMENT_PORT"
apiversion = "v4"


class SCDeviceManagement:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/scdevicemanagement"
                print("SCDEVICEMANAGEMENT: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCDEVICEMANAGEMENT: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion=apiversion, port=port, service="SCDeviceManagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion=apiversion, port=port, service="SCDeviceManagement"
                )
            else:
                print("SCDEVICEMANAGEMENT: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCDeviceManagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCDeviceManagement"
                )

        except Exception as e:
            print("Exception " + str(e))

    def realSenseMigrated(self, org, pid, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scdevicemanagement.realSenseMigrated",
                org=org,
                pid=pid
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scdevicemanagement.realSenseMigrated",
                org=org,
                pid=pid
            )
        return res

    def getDeviceSlots(self, org, pid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scdevicemanagement.getDeviceSlots",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scdevicemanagement.getDeviceSlots",
                org=org,
                pid=pid,
                body=json.loads(expJson),
            )
        return res
