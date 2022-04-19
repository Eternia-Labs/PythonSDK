from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPClientError
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
import asyncio
import json
import requests
import os
import hmac, hashlib, time
import yaml, jmespath

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

signing_status = "SIGNING_STATUS_PYTHONSDK"

if not os.getenv(signing_status):
    signing = "Enabled"
else:
    signing = os.getenv(signing_status)


def credential_checker(filtered_credentials: dict):

    print(filtered_credentials)

    if (
        "sc_access_key" not in filtered_credentials
        or "sc_secret_key" not in filtered_credentials
    ):
        return {
            "code": "failure",
            "error": f"Either 'sc_access_key' or 'sc_secret_key' is not provided in the sc-tenants.yml file.",
        }
    elif (
        not filtered_credentials["sc_access_key"]
        or not filtered_credentials["sc_secret_key"]
    ):
        return {
            "code": "failure",
            "error": f"Either 'sc_access_key' or 'sc_secret_key' value is not provided in the sc-tenants.yml file.",
        }

    return {"code": "success", "data": f"All values are provided."}


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
        # print(
        #     "Signing is not enabled. You can enable by setting the environment variables: 'SIGNING_STATUS_PYTHONSDK', 'USER_NAME_PYTHONSDK' and 'PASSWORD_PYTHONSDK'."
        # )

    def initializeForService(
        self, prefix, uri, apiversion, port=None, service="scgrids"
    ):

        if signing == "Disabled" and port != None:
            print(
                "Signing is not enabled. You can enable by setting the environment variables: 'SIGNING_STATUS_PYTHONSDK', 'USER_NAME_PYTHONSDK' and 'PASSWORD_PYTHONSDK'."
            )
            self.url = (
                prefix + "://" + uri + ":" + str(port) + "/" + apiversion + "/actions"
            )
            self.headers = {"content-type": "application/json"}
        elif signing == "Disabled" and port == None:
            print(
                "Signing is not enabled. You can enable by setting the environment variables: 'SIGNING_STATUS_PYTHONSDK', 'USER_NAME_PYTHONSDK' and 'PASSWORD_PYTHONSDK'."
            )
            self.url = prefix + "://" + uri + "/" + apiversion + "/actions"
            self.headers = {"content-type": "application/json"}
        elif signing == "Enabled":
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
            print(httpmethod)
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

        if signing == "Enabled" and propid!=None:

            self.etime = str(int(time.time()))

            # dirname = os.path.dirname(__file__).split("/")[0]
            # dirname = os.path.join(dirname, "sc-tenants.yml")
            # a_yaml_file = open(dirname)
            # parsed_yaml_file = yaml.load(a_yaml_file)
            # parsed_yaml_file = yaml.safe_load(a_yaml_file)

            # region Create absolute path to sc-tenants file
            _absolute_path_sdk_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            print(f'Path to SDK directory is:\n{_absolute_path_sdk_directory}')
            absolute_path_tenants_file = f'{_absolute_path_sdk_directory}/sc-tenants.yml'
            print(f'Path to sc-tenants file is:\n{absolute_path_tenants_file}')
            # endregion

            if not os.path.isfile(absolute_path_tenants_file):
                return {"code": "failure", "error": "sc-tenants file not found."}

            with open(absolute_path_tenants_file, mode='r') as _file_stream:
                parsed_yaml_file = yaml.safe_load(_file_stream)
                print('Loaded data from sc-tenants file')

            if propid not in parsed_yaml_file["tenants"]:
                return {"code": "failure", "error": "No such property with the provided propid exists in the sc-tenants.yml file."}

            filtered_credentials = parsed_yaml_file["tenants"][propid]

            checker = credential_checker(filtered_credentials)

            if checker["code"] == "failure":
                return {"code": "failure", "error": checker["error"]}

            self.access_key = filtered_credentials["sc_access_key"]
            self.secret_key = filtered_credentials["sc_secret_key"]
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
            print(self.headers)

        elif signing == "Enabled" and propid==None:
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
                return {"code": "failure", "error": _err_text}
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
