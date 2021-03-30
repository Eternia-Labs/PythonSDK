from SDK.SCGridsServices.API import * 
from SDK.SCDashboardServices.API import *
from SDK.SCMetricsServices.API import *
from SDK.SCBIServices.API import *


grids = SCGrids()
dashboard = SCDashboard()
metrics = SCMetrics()
bi = SCBi()


org = 'SMARTCLEAN'
## For not testing locally. 
PropId = '3b749a681d14446292b6c79b48403bbd' 
## For testing locally.
# PropId = 'ff47033487244e17a6d96df2a233a1a0' 

Property = grids.readProperty(org=org,pid = 'scnoop',propid = PropId)
## For Sync
print(Property.json()) 
## For Async
print(Property) 



# response = bi.getReportingServicesForPrincipalOrg(org='SMARTCLEAN',pid='scnoop',expJson = json.dumps(request_body), client='Sync')
# print(response)