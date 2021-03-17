import json
import requests
import os

signing_status = 'SIGNING_STATUS_PYTHONSDK'
user_name = 'USER_NAME_PYTHONSDK'
user_password = 'PASSWORD_PYTHONSDK'

name = os.getenv(user_name)
password = os.getenv(user_password)

if not os.getenv(signing_status):
	signing = "Disabled"
else:
	signing = "Enabled"

if signing == "Enabled":
	body = {"uname": name,"passwd": password}
	body = json.dumps(body)
	access_token = requests.post("https://console.smartclean.io/api/unauth/v1/login",body)
	# print(json.loads(access_token.text))
	access_token = json.loads(access_token.text)["access_token"]


class ClientV1:

	def __init__(self):

		self.url = None
		self.service = None
		self.headers = None
		self.timeout = 10
		print("Message from Sync Client:")
		print("Signing is not enabled. You can enable by setting the environment variables: 'SIGNING_STATUS_PYTHONSDK', 'USER_NAME_PYTHONSDK' and 'PASSWORD_PYTHONSDK'.")

	def initializeForService(self,prefix,uri,apiversion,port=None,service='SCGrids'):
		
		if signing == "Disabled":
			self.url = prefix + "://"+ uri + ":" + str(port) +"/" + apiversion + "/actions"
			self.headers = {"content-type":"application/json"}
		elif signing == "Enabled":
			self.url = prefix + "://"+ uri + "/" + apiversion + "/actions"
			self.headers = {"content-type":"application/json", "x-sc-identity":"external", "Authorization":access_token}
		print("setting url")
		self.service = service

	def seturl(self, url):
		self.url = url

	def geturl(self):
		return self.url

	def getApiVersion(self):
		return self.apiversion

	def makeRequest(self, httpmethod, op, propid=None, body=None, org='SMARTCLEAN', pid='scnoop'):
		
		if propid: 
			finalURI = self.geturl() + '?op='+ str(op) + '&org=' + str(org) + '&pid='+str(pid) + '&propid='+str(propid)
		else:
			finalURI = self.geturl() + '?op='+ str(op) + '&org=' + str(org) + '&pid='+str(pid)
		print(finalURI)
		if httpmethod == 'GET':
			print(httpmethod)
			body = None
			requests.get(finalURI)
		else:
			body = json.dumps(body)
			response = requests.post(finalURI, data = body, headers = self.headers, timeout = self.timeout)
		
		return response

def getClient():
	client = ClientV1()
	return client
