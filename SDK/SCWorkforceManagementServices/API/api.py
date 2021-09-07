from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os

HOST = "SC_WORKFORCEMANAGEMENT_HOST"
PROTOCOL = "SC_WORKFORCEMANAGEMENT_HTTP_PROTOCOL"
PORT = "SC_WORKFORCEMANAGEMENT_PORT"
apiversion = "v1"


class SCWorkforcemanagement:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = "console.smartclean.io/api/scworkforcemanagement"
                print("SCWORKFORCEMANAGEMENT: Host is not set")
            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCWORKFORCEMANAGEMENT: protocol env variable is not set")
            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, port, apiversion, service="SCWorkforceManagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, port, apiversion, service="SCWorkforceManagement"
                )
            else:
                print("SCWORKFORCEMANAGEMENT: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="SCWorkforceManagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="SCWorkforceManagement"
                )
        except Exception as e:
            print("Exception " + str(e))

    def createIncidentWithoutAssignee(self, org, propid, pid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scteams.createIncidentWithoutAssignee",
                propid=propid,
                body=json.loads(expJson),
                org=org,
                pid=pid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scteams.createIncidentWithoutAssignee",
                propid=propid,
                body=json.loads(expJson),
                org=org,
                pid=pid,
            )
        return res

    def getTaskGroupInTRangeForID(self, org, pid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scteams.getTaskGroupInTRangeForID",
                body=json.loads(expJson),
                org=org,
                pid=pid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scteams.getTaskGroupInTRangeForID",
                body=json.loads(expJson),
                org=org,
                pid=pid,
            )
        return res

    def getShiftLatenessMetricsForBuilding(
        self, org, pid, propid, expJson, client=None
    ):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scteams.getShiftLatenessMetricsForBuilding",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scteams.getShiftLatenessMetricsForBuilding",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    # TODO: Infer return type from downstream operation & put in signature (replace "-> any" with "-> <type>")
    def find_availability_for_incident(
        self, org: str, prop_id: str, pid: str, exp_json: str, client=None
    ) -> any:
        """
        This returns availability response for incident

        :param org: Organisation ID
        :param prop_id: Property ID
        :param pid: Project ID
        :param exp_json: Expected request body (as a JSON string)
        :param client: HTTP Client type to use ("Async" or "Sync")
        :return: Response to HTTP Request
        """

        if client == "Sync":
            _client_obj = self.Sync_client
        else:
            _client_obj = self.Async_client

        _method = "POST"
        _op = "scteams.findAvailabilityForIncident-v2"

        request_kwargs = {
            "httpmethod": _method,
            "op": _op,
            "propid": prop_id,
            "org": org,
            "pid": pid,
            "body": json.loads(exp_json),
        }

        res = _client_obj.makeRequest(**request_kwargs)
        return res
