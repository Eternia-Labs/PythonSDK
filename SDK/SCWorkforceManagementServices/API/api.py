from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os
from urllib.request import urlopen

HOST = "SC_WORKFORCEMANAGEMENT_HOST"
PROTOCOL = "SC_WORKFORCEMANAGEMENT_HTTP_PROTOCOL"
PORT = "SC_WORKFORCEMANAGEMENT_PORT"

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

            url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            apiversion = data_json["modules"]["scworkforcemanagement"]["version"]

            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="scworkforcemanagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="scworkforcemanagement"
                )
            else:
                print("SCWORKFORCEMANAGEMENT: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="scworkforcemanagement"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="scworkforcemanagement"
                )
        except Exception as e:
            print("Exception " + str(e))

    def createIncidentWithoutAssignee(self, org, pid, propid, expJson, client=None):
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

    def getTaskGroupInTRangeForID(self, org, pid, propid=None, expJson= '{}', client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scteams.getTaskGroupInTRangeForID",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scteams.getTaskGroupInTRangeForID",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
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
        self, org, pid, propid, expJson, client=None
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
            "propid": propid,
            "org": org,
            "pid": pid,
            "body": json.loads(expJson),
        }

        res = _client_obj.makeRequest(**request_kwargs)
        return res

    # TODO: Infer return type from downstream operation & put in signature (replace "-> any" with "-> <type>")
    def assign_shift_to_incident(
        self, org, pid, propid, expJson, client=None
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
        _op = "scteams.assignIncident"

        request_kwargs = {
            "httpmethod": _method,
            "op": _op,
            "propid": propid,
            "org": org,
            "pid": pid,
            "body": json.loads(expJson),
        }

        res = _client_obj.makeRequest(**request_kwargs)
        return res

    def get_incident_settings(self, org, pid, propid, client=None):

        op = 'scteams.getIncidentsSettings'

        _args_for_function = {
            'httpmethod': 'POST',
            'op': op,
            'propid': propid,
            'org': org,
            'pid': pid
        }

        if client == "Sync":
            res = self.Sync_client.makeRequest(**_args_for_function)
        else:
            res = self.Async_client.makeRequest(**_args_for_function)

        return res
