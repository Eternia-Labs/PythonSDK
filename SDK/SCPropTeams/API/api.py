from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_PROP_TEAMS_HOST"
PROTOCOL = "SC_PROP_TEAMS_PROTOCOL"
PORT = "SC_PROP_TEAMS_PORT"
apiversion = "v1"


class SCPropTeams:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/scteamsprop"
                print("SCPROPTEAMS: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCPROPTEAMS: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="scteamsprop"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="scteamsprop"
                )

            else:
                print("SCPROPTEAMS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="scteamsprop"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="scteamsprop"
                )

        except Exception as e:
            print("Exception " + str(e))

    def getMemberGroup(self, org, pid, propid, client=None):
        """
        Retrieving member groups for property along with member group id and name mapping.

        :param org:
        :param pid:
        :param propid:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op="scpropteams.getMemberGroup", org=org, pid=pid, propid=propid
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op="scpropteams.getMemberGroup", org=org, pid=pid, propid=propid
            )
        return res

    