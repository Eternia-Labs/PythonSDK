from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
import json
		
class ClientV1:

	def __init__(self):
		self.session = AsyncHTTPClient()
		self.timeout = 5
		self.url = None
		self.service = None
		self.apiversion = 'v1'
	
	def initializeForService(self,prefix,uri,port,service):
		self.url = prefix + "://"+ uri + ":" + str(port) +"/" + self.apiversion + "/actions"
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
		headers = None
		
		if httpmethod == 'GET':
			print(httpmethod)
			body = None
		else:
			body = json.dumps(body)
			headers = {"content-type":"application/json"}
		
		if propid: 
			finalURI = self.geturl() + '?op='+ str(op) + '&org=' + str(org) + '&pid='+str(pid) + '&propid='+str(propid)
		else:
			finalURI = self.geturl() + '?op='+ str(op) + '&org=' + str(org) + '&pid='+str(pid)
		
		req = HTTPRequest(finalURI,method = httpmethod, body = body,request_timeout = self.timeout,headers=headers)
		
		async def toExecute():
			try:
				response = await self.session.fetch(req)
				print(json.loads(response.body))
			except Exception as e:
				print("inside exception",str(e))
				return e, None
			return None, json.loads(response.body)
		print("making request to ---", finalURI, "----")
		io_loop = IOLoop.current()
		io_loop.run_sync(toExecute)
	
	def __del__(self):
		print("Deleting client")
		self.session.close()

def getClient():
	client = ClientV1()
	return client
