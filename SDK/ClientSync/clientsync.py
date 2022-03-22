from tornado.httpclient import HTTPRequest
import json
import requests
import os
import time
import hmac, hashlib, time
from urllib.request import urlopen
import yaml
import jmespath

signing_status = "SIGNING_STATUS_PYTHONSDK"

if not os.getenv(signing_status):
    signing = "Disabled"
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

        self.timeout = 10
        self.session = None
        self.url = None
        self.service = None
        self.headers = None
        self.access_key = None
        self.secret_key = None
        print("Message from Sync Client:")

    def initializeForService(
        self, prefix, uri, apiversion, port=None, service="SCGrids"
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

            dirname = os.path.dirname(__file__).split("/")[0]
            dirname = os.path.join(dirname, "sc-tenants.yml")
            a_yaml_file = open(dirname)
            parsed_yaml_file = yaml.load(a_yaml_file)
            if propid not in parsed_yaml_file["tenants"]:
                return {"code": "failure", "error": "No such property with the provided propid exists in the sc-tenants.yml file."}
            
            filtered_credentials = parsed_yaml_file["tenants"][propid]

            checker = credential_checker(filtered_credentials)

            if checker["code"] == "failure":
                return {"code": "failure", "error": checker["error"]}

            self.access_key = filtered_credentials["sc_access_key"]
            self.secret_key =  bytes(filtered_credentials["sc_secret_key"], "utf-8")

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
        
        elif signing == "Enabled" and propid==None:
            return {"code": "failure", "error": "Missing propid in the request."}

        try:
            if httpmethod == "GET":
                body = None
                requests.get(finalURI)
            else:
                body = json.dumps(body)
                response = requests.post(
                    finalURI, data=body, headers=self.headers, timeout=self.timeout
                )

        except Exception as e:
            return {"code": "Failure", "Error": f"{e}"}

        return response.json()

    # def __del__(self):
    # 	print("Deleting client")
    # 	self.session.close()


def getClient():
    client = ClientV1()
    return client
