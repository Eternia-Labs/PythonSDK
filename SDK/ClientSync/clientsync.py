from tornado.httpclient import HTTPRequest
import json
import requests
import os

signing_status = "SIGNING_STATUS_PYTHONSDK"
user_name = "USER_NAME_PYTHONSDK"
user_password = "PASSWORD_PYTHONSDK"

name = os.getenv(user_name)
password = os.getenv(user_password)

if not os.getenv(signing_status):
    signing = "Disabled"
else:
    signing = os.getenv(signing_status)

if signing == "Enabled":
    body = {"uname": name, "passwd": password}
    body = json.dumps(body)
    access_token = requests.post(
        "https://console.smartclean.io/api/unauth/v1/login", body
    )
    access_token = json.loads(access_token.text)["access_token"]


class ClientV1:
    def __init__(self):

        self.name = os.getenv("USER_NAME_PYTHONSDK")
        self.password = os.getenv("PASSWORD_PYTHONSDK")
        self.timeout = 10
        self.session = None
        self.url = None
        self.service = None
        self.headers = None
        self.flag = 0
        print("Message from Sync Client:")
        print(
            "Signing is not enabled. You can enable by setting the environment variables: 'SIGNING_STATUS_PYTHONSDK', 'USER_NAME_PYTHONSDK' and 'PASSWORD_PYTHONSDK'."
        )

    def getAccessToken(self):
        try:
            body = {"uname": self.name, "passwd": self.password}
            body = json.dumps(body)
            request = requests.post(
                "https://console.smartclean.io/api/unauth/v1/login", body
            )

            if request.status_code != 200:
                return None

        except Exception as e:
            return {"code": "Failure", "Error": f"{e}"}
        else:
            return "Successful", request

    def requestNewToken(makeRequest):
        def wrapper(self, *args, **kwargs):
            response = makeRequest(self, *args, **kwargs)

            if type(response) == dict:
                return response

            elif response.status_code == 401:
                response_access = self.getAccessToken()
                refresh_token = json.loads(response_access[1].text)

                if "refresh_token" not in refresh_token:
                    return {
                        "code": "Failure",
                        "data": "Request for refresh token failed.",
                    }

                refresh_token = refresh_token["refresh_token"]
                body = {"rtoken": f"{refresh_token}"}

                body = json.dumps(body)
                request = requests.post(
                    "https://console.smartclean.io/api/unauth/v1/login", body
                )

                if request.status_code != 200:
                    response = self.getAccessToken()
                    if response == None:
                        response = {"code": "Failure", "Error": "All retries failed."}
                        return response
                    else:
                        self.access_token = response[1].json()["access_token"]
                        response = makeRequest(self, *args, **kwargs)
                        return response

                elif type(response) == dict:
                    return response

                else:
                    self.access_token = request.json()["access_token"]
                    response = makeRequest(self, *args, **kwargs)
                    return response
            else:
                return response

        return wrapper

    def initializeForService(
        self, prefix, uri, apiversion, port=None, service="SCGrids"
    ):

        if signing == "Disabled" and port != None:
            self.url = (
                prefix + "://" + uri + ":" + str(port) + "/" + apiversion + "/actions"
            )
            self.headers = {"content-type": "application/json"}
        elif signing == "Disabled" and port == None:
            self.url = prefix + "://" + uri + "/" + apiversion + "/actions"
            self.headers = {"content-type": "application/json"}
        elif signing == "Enabled":
            self.url = prefix + "://" + uri + "/" + apiversion + "/actions"
            print(self.url)
        self.service = service

    def seturl(self, url):
        self.url = url

    def geturl(self):
        return self.url

    def GetHTTPClient(self):
        return self.session

    def getApiVersion(self):
        return self.apiversion

    @requestNewToken
    def makeRequest(
        self, httpmethod, op, propid=None, body=None, org="SMARTCLEAN", pid="scnoop"
    ):
        if self.flag == 0:
            self.access_token = access_token
            self.flag = 1

        if signing == "Enabled":
            self.headers = {
                "content-type": "application/json",
                "x-sc-identity": "external",
                "Authorization": self.access_token,
            }

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

        print(finalURI)

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

        return response

    # def __del__(self):
    # 	print("Deleting client")
    # 	self.session.close()


def getClient():
    client = ClientV1()
    return client
