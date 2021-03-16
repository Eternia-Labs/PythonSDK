from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
import json
import requests

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")


body = '{"uname": "smartclean","passwd": "SmartClean@321#"}'
access_token = requests.post("https://console.smartclean.io/api/unauth/v1/login",body)
print(json.loads(access_token.text))
access_token = json.loads(access_token.text)["access_token"]


class ClientV1:

	def __init__(self):
		self.session = AsyncHTTPClient()
		self.timeout = 10
		self.url = None
		self.service = None
		self.headers = None
		
	def initializeForService(self,prefix,uri,apiversion,port=None,service='SCGrids'):
		print(prefix,self.url)
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

	def GetHTTPClient(self):
		return self.session

	def getApiVersion(self):
		return self.apiversion

	def makeRequest(self, httpmethod, op, propid=None, body=None, org='SMARTCLEAN', pid='scnoop'):
		
		if httpmethod == 'GET':
			print(httpmethod)
			body = None
		else:
			body = json.dumps(body)
		
		if propid: 
			finalURI = self.geturl() + '?op='+ str(op) + '&org=' + str(org) + '&pid='+str(pid) + '&propid='+str(propid)
		else:
			finalURI = self.geturl() + '?op='+ str(op) + '&org=' + str(org) + '&pid='+str(pid)
		
		req = HTTPRequest(finalURI,method = httpmethod, body = body,request_timeout = self.timeout,headers=self.headers)
		print(req.headers)
		async def toExecute():
			try:
				response = await self.session.fetch(req)
				# print(json.loads(response.body))
			except Exception as e:
				print("inside exception",str(e))
				return e
			return json.loads(response.body)
		print("making request to ---", finalURI, "----")
		io_loop = IOLoop.current()
		return io_loop.run_sync(toExecute)
	
	def __del__(self):
		print("Deleting client")
		self.session.close()

def getClient():
	client = ClientV1()
	return client
