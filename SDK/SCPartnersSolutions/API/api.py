from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_PARTNERS_SOLUTIONS_HOST"
PROTOCOL = "SC_PARTNERS_SOLUTIONS_HTTP_PROTOCOL"
PORT = "SC_PARTNERS_SOLUTIONS_PORT"
apiversion = "v1"
SERVICE_ID_IN_URL = "solution"


class SCPartnersSolutions:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/scpartnerssolutions"
                print("SCPARTNERSSOLUTIONS: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCPARTNERSSOLUTIONS: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix,
                    uri,
                    apiversion=apiversion,
                    port=port,
                    service="SCPartnersSolutions",
                )
                self.Sync_client.initializeForService(
                    prefix,
                    uri,
                    apiversion=apiversion,
                    port=port,
                    service="SCPartnersSolutions",
                )
            else:
                print("SCPARTNERSSOLUTIONS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCPartnersSolutions"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCPartnersSolutions"
                )

        except Exception as e:
            print("Exception " + str(e))

    def getSolutionForProperty(
        self, org: str, prop_id: str, solution_id: str, client=None
    ):

        op = f"{SERVICE_ID_IN_URL}.getSolutionForProperty"
        body = {"solutionId": solution_id}
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        return res

    def listAllSolutionsForProperty(self, org: str, prop_id: str, client=None):

        op = f"{SERVICE_ID_IN_URL}.listAllSolutionsForProperty"
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id
            )
        return res

    def addSolutionToProperty(
        self, org: str, prop_id: str, solution_id: str, client=None
    ):

        op = f"{SERVICE_ID_IN_URL}.addSolutionToProperty"
        body = {"solutionId": solution_id}

        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        return res

    def approveSolutionForProperty(
        self, org: str, prop_id: str, solution_id: str, client=None
    ):

        op = f"{SERVICE_ID_IN_URL}.approveSolutionForProperty"
        body = {"solutionId": solution_id}

        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        return res

    def denySolutionForProperty(
        self, org: str, prop_id: str, solution_id: str, client=None
    ):

        op = f"{SERVICE_ID_IN_URL}.denySolutionForProperty"
        body = {"solutionId": solution_id}

        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op=op, org=org, propid=prop_id, body=body
            )
        return res
