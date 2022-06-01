from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPClientError
import asyncio
import json
import os
import hmac, hashlib, time

from SDK.helper.DB import *
from SDK.helper.helperFunctions import *

signing_status = "SIGNING_STATUS_PYTHONSDK"

if not os.getenv(signing_status):
    signing = "Enabled"
else:
    signing = os.getenv(signing_status)

if signing == "Enabled":
    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")


class ClientV1:
    def __init__(self):
        self.session = None
        self.timeout = 10
        self.url = None
        self.service = None
        self.headers = None
        self.secret_key = None
        self.access_key = None
        print("Message from Async Client:")

    def initializeForService(
        self, prefix, uri, apiversion, port=None, service="scgrids"
    ):

        if signing == "Disabled" and port != None:
            print(
                "Signing is Disabled. You can enable signing by unsetting the environment variable: 'SIGNING_STATUS_PYTHONSDK'."
            )
            self.url = (
                prefix + "://" + uri + ":" + str(port) + "/" + apiversion + "/actions"
            )
            self.headers = {"content-type": "application/json"}
        elif signing == "Disabled" and port == None:
            print(
                "Signing is Disabled. You can enable signing by unsetting the environment variable: 'SIGNING_STATUS_PYTHONSDK'."
            )
            self.url = prefix + "://" + uri + "/" + apiversion + "/actions"
            self.headers = {"content-type": "application/json"}
        elif signing == "Enabled":
            print(
                "Signing is Enabled. You can disable signing by setting the environment variable: 'SIGNING_STATUS_PYTHONSDK' as 'Disabled'."
            )
            self.url = prefix + "://" + uri + "/" + apiversion + "/actions"

        print("setting url")
        self.service = service

    def seturl(self, url):
        self.url = url

    def geturl(self):
        return self.url

    def GetHTTPClient(self):
        return self.session

    def getApiVersion(self):
        return self.apiversion

    def makeRequest(
        self, httpmethod, op, propid=None, body=None, org="SMARTCLEAN", pid="scnoop"
    ):

        if httpmethod == "GET":
            body = None
        else:
            body = json.dumps(body)

        if propid:
            finalURI = (
                self.geturl()
                + "?op="
                + str(op)
                + "&org="
                + str(org)
                + "&pid="
                + str(pid)
                + "&propid="
                + str(propid)
            )
        else:
            finalURI = (
                self.geturl()
                + "?op="
                + str(op)
                + "&org="
                + str(org)
                + "&pid="
                + str(pid)
            )

        if signing == "Enabled" and propid != None:

            self.etime = str(int(time.time()))
            response_data = {"success": False, "text": "default"}

            # Check if Tenants DB exists.
            db_checked = db_checker(absolute_path_tenants_database)

            if db_checked["code"] == "failure":
                return {"code": "failure", "error": db_checked["data"]}

            # Fetch access_key and secret_key for a particular property id.
            cursor = conn.execute(
                f"SELECT PropID,sc_access_key,sc_secret_key from Tenants where PropID = (?)",
                (propid,),
            )
            data = cursor.fetchall()

            if not data:
                response_data[
                    "text"
                ] = "No such property with the provided propid exists in tenants DB."
                return response_data

            credentials = {
                "propid": data[0][0],
                "sc_access_key": data[0][1],
                "sc_secret_key": data[0][2],
            }

            # Check if details provided are of valid syntax.
            checker = credential_checker(credentials)

            if checker["code"] == "failure":
                return {"code": "failure", "error": checker["error"]}

            self.access_key = credentials["sc_access_key"]
            self.secret_key = credentials["sc_secret_key"]
            self.secret_key = bytes(self.secret_key, "utf-8")

            total_paramsStr = (
                self.service
                + "/"
                + propid
                + "/"
                + op
                + "/"
                + self.access_key
                + "/"
                + self.etime
            )
            total_params = bytes(total_paramsStr, "utf-8")
            signature = hmac.new(
                self.secret_key, total_params, hashlib.sha256
            ).hexdigest()

            self.headers = {
                "content-type": "application/json",
                "Accept": "application/json",
                "x-sc-identity": "external",
                "x-sc-time": self.etime,
                "Authorization": f"SCHMAC_V1;{self.access_key};{signature}",
            }

        elif signing == "Enabled" and propid == None:
            return {"code": "failure", "error": "Missing propid in the request."}

        req = HTTPRequest(
            finalURI,
            method=httpmethod,
            body=body,
            request_timeout=self.timeout,
            headers=self.headers,
        )

        async def toExecute():

            try:
                # if self.session is None:
                print("self.session is currently None")
                self.session = AsyncHTTPClient()
                print("self.session now set to AsyncHTTPClient()")
                response = await self.session.fetch(req)
                # print(json.loads(response.body))
            except HTTPClientError as e:
                _err_text = str(e)
                print("inside exception HTTPClientError", _err_text)

                if not e.response:
                    print(
                        "HTTPResponse object not available in HTTPClientError object."
                    )
                    return {"code": "failure", "error": _err_text}

                response_headers = e.response.headers
                print(f"Response headers are:\n{response_headers}")

                http_response_object = e.response

                if not http_response_object.body:
                    print("No data in body of this HTTPResponse object")
                    return {"code": "failure", "error": _err_text}

                decoded_response_body = http_response_object.body.decode("utf-8")

                if (
                    "Content-Type" in response_headers
                    and response_headers["Content-Type"] == "application/json"
                ):
                    response_data = json.loads(decoded_response_body)
                else:
                    response_data = decoded_response_body

                print(f"Data in body of response is:\n{response_data}")

                return {"code": "failure", "error": response_data}

            except Exception as e:
                print("inside exception", str(e))
                return {"code": "failure", "error": f"{e}"}

            return json.loads(response.body)

        print("making request to ---", finalURI, "----")
        return asyncio.run(toExecute())

    # def __del__(self):
    # 	print("Deleting client")
    # 	self.session.close()


def getClient():
    client = ClientV1()
    return client
