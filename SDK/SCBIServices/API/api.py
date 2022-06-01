from SDK.ClientSync import clientsync
from SDK.ClientAsync import clientasync
import json
import tornado.ioloop
import os
from urllib.request import urlopen

HOST = "SC_BI_HOST"
PROTOCOL = "SC_BI_HTTP_PROTOCOL"
PORT = "SC_BI_PORT"


class SCBi:
    def __init__(self):
        self.Async_client = clientasync.getClient()
        self.Sync_client = clientsync.getClient()
        self.initialize()

    def initialize(self):
        try:
            url = "https://www.smartclean.io/matrix/utils/modules/moduleversions.json"
            response = urlopen(url)
            data_json = json.loads(response.read())
            apiversion = data_json["modules"]["scbi"]["version"]
            base = data_json["base"]

            if os.getenv(HOST):
                uri = os.getenv(HOST)
            else:
                uri = f"{base}/scbi"
                print("SCBI: Host is not set")

            if os.getenv(PROTOCOL):
                prefix = os.getenv(PROTOCOL)
            else:
                prefix = "https"
                print("SCBI: protocol env variable is not set")

            if os.getenv(PORT):
                port = os.getenv(PORT)
                print(prefix, uri, port)
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, port, service="scbi"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, port, service="scbi"
                )
            else:
                print("SCBI: Port is not set")
                self.Async_client.initializeForService(
                    prefix, uri, apiversion, service="scbi"
                )
                self.Sync_client.initializeForService(
                    prefix, uri, apiversion, service="scbi"
                )
        except Exception as e:
            print("Exception " + str(e))

    def getReportingServicesForPrincipalOrg(
        self, org, pid, propid=None, expJson="{}", client=None
    ):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.getReportingServicesForPrincipalOrg",
                body=json.loads(expJson),
                org=org,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.getReportingServicesForPrincipalOrg",
                body=json.loads(expJson),
                org=org,
                propid=propid,
            )
        return res

    def getReportingServicesForPrincipalBuilding(
        self, org, pid, propid=None, expJson="{}", client=None
    ):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.getReportingServicesForPrincipalBuilding",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.getReportingServicesForPrincipalBuilding",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def getReportingServicesForPrincipalProperty(
        self, org, pid, propid, expJson, client=None
    ):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.getReportingServicesForPrincipalProperty",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.getReportingServicesForPrincipalProperty",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def pdfReportGenerationFailure(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.pdfReportGenerationFailure",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.pdfReportGenerationFailure",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def pdfReportGenerationSuccess(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.pdfReportGenerationSuccess",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.pdfReportGenerationSuccess",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def pdfGenerationTaskStarted(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.pdfGenerationTaskStarted",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.pdfGenerationTaskStarted",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def kpiJobFailure(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.kpiJobFailure",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.kpiJobFailure",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def kpiJobSuccess(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.kpiJobSuccess",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.kpiJobSuccess",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res

    def kpiJobStarted(self, org, pid, propid, expJson, client=None):
        if client == "Sync":
            res = self.Sync_client.makeRequest(
                httpmethod="POST",
                op="scbi.kpiJobStarted",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        else:
            res = self.Async_client.makeRequest(
                httpmethod="POST",
                op="scbi.kpiJobStarted",
                body=json.loads(expJson),
                org=org,
                pid=pid,
                propid=propid,
            )
        return res
