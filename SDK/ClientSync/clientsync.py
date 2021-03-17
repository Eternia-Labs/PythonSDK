import json
import requests


body = '{"uname": "sc_shikha","passwd": "Brownie@123"}'
access_token = requests.post("https://console.smartclean.io/api/auth/login/token",body)
access_token = json.loads(access_token.text)["access_token"]

class ClientV1:

	def __init__(self):

		self.url = None
		self.service = None
		self.headers = None
		self.timeout = 10

	def initializeForService(self,prefix,uri,apiversion,port=None,service='SCGrids'):

		if port:
			self.url = prefix + "://"+ uri + ":" + str(port) +"/" + apiversion + "/actions"
			self.headers = {"content-type":"application/json"}
		else:
			self.url = prefix + "://"+ uri + "/" + apiversion + "/actions"
			self.headers = {"content-type":"application/json", "x-sc-identity":"external", "Authorization":access_token}
			# print(self.url)
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
