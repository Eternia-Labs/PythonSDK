from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
class Client:

	def __init__(self):
		self.session = AsyncHTTPClient()
		self.timeout = 5
		self.url = "http://127.0.0.1:5000"
		self.service = None
		self.apiversion = None

	def seturl(self, url):
		self.url = url

	def geturl(self):
		return self.url

	def GetHTTPClient(self):
		return self.session

	def GetContext(self):
		return self.service

	def GetAPIVersion(self):
		return self.apiversion

	def makeRequest(self, httpmethod,op,pid, body=None,org='scnoop'):
		headers = None
		import json
		if httpmethod == 'GET':
			print(httpmethod)
			body = None
		else:
			body = json.dumps(body)
			headers = {"content-type":"application/json"}
		#print(body)
		finalURI = self.geturl() + '/v2/actions?op='+ op + '&org=' + org + '&pid='+str(pid)
		req = HTTPRequest(finalURI,method = httpmethod, body = body,request_timeout = self.timeout,headers=headers)
		#print("REQUEST",req.__dict__)
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
	client = Client()
	return client
