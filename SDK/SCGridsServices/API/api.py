from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os
from urllib.request import urlopen

HOST = "SC_GRIDS_HOST"
PROTOCOL = "SC_GRIDS_HTTP_PROTOCOL"
PORT = "SC_GRIDS_PORT"

# TODO:
#  1. Infer return type from downstream operation & put in signature (replace "-> any" with "-> <type>")

class SCGrids:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            apiversion = data_json["modules"]["scgrids"]["version"]
            base = data_json["base"]

            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = f"{base}/scgrids"
                print("SCGRIDS: Host is not set")

            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCGRIDS: protocol env variable is not set")

            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="scgrids"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="scgrids"
                )

            else:
                print("SCGRIDS: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="scgrids"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="scgrids"
                )

        except Exception as e:
            print("Exception " + str(e))
            
    def listProperties(self, org, pid, propid=None, client=None):
        """
        Gets list of all Properties

        :param org:
        :param pid:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op="scgrids.listProperties", org=org, pid=pid, propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op="scgrids.listProperties", org=org, pid=pid, propid=propid,
            )
        return res

    # region Requests for Property (propid is required in query params)
    def readProperty(self, org, pid, propid, client=None):
        """
        Get details of Property

        :param org:
        :param pid:
        :param propid:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scgrids.readProperty",
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scgrids.readProperty",
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def listBuilding(self, org, pid, propid, client=None):
        """
        Get list of Buildings in Property

        :param org:
        :param pid:
        :param propid:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scgrids.listBuildingsByProperty",
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scgrids.listBuildingsByProperty",
                org=org,
                pid=pid,
                propid=propid,
            )
        return res
    # endregion

    # region Requests for Building (pid is required in query params)
    def readBuilding(self, org, pid, propid=None, client=None):
        """
        Get details of Building

        :param org:
        :param pid:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op="scgrids.readBuilding", org=org, pid=pid, propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op="scgrids.readBuilding", org=org, pid=pid, propid=propid,
            )
        return res

    def listLevelsByBuilding(self, org, pid, propid=None, client=None):
        """
        Get list of all Levels in Building

        :param org:
        :param pid:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op="scgrids.listLevelsByBuilding", org=org, pid=pid, propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op="scgrids.listLevelsByBuilding", org=org, pid=pid, propid=propid,
            )
        return res

    def buildingZoneMap(self, org, pid, propid=None, expJson= '{}', client=None):
        """
        Get Zone map in Building

        :param org:
        :param pid:
        :param expJson:
        :param client:
        :return:
        """

        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scgrids.buildingZoneMap",
                org=org,
                pid=pid,
                propid=propid,
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scgrids.buildingZoneMap",
                org=org,
                pid=pid,
                propid=propid,
                body=json.loads(expJson),
            )
        return res

    def listBuildingMetrics(self, org, pid, propid=None, client=None):
        """
        Gets all metrics (eg count of members) for Building

        :param org:
        :param pid:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST", op="scgrids.listBuildingMetrics", org=org, pid=pid, propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST", op="scgrids.listBuildingMetrics", org=org, pid=pid, propid=propid,
            )
        return res
    # endregion

    # region Requests for Level (LID is required in data)
    def listZonesByLevel(self, org, pid, propid=None, expJson= '{}', client=None):
        """
        Gets list of all Zones in Level

        :param org:
        :param pid:
        :param expJson:
        :param client:
        :return:
        """
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scgrids.listZonesByLevel",
                org=org,
                pid=pid,
                propid=propid,
                body=json.loads(expJson),
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scgrids.listZonesByLevel",
                org=org,
                pid=pid,
                propid=propid,
                body=json.loads(expJson),
            )
        return res
    # endregion

    # region Requests for Zone (InsID is required in data)
    def read_zone(self, org: str, pid: str, propid=None, expJson= '{}', client=None) -> any:
        """
        Gets details of Zone

        :param org: Organisation ID
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
        _op = "scgrids.readZone"

        request_kwargs = {
            "httpmethod": _method,
            "op": _op,
            "org": org,
            "pid": pid,
            "propid": propid,
            "body": json.loads(expJson),
        }

        res = _client_obj.makeRequest(**request_kwargs)
        return res
    # endregion
