from SDK.SCGridsServices.API import * 
from SDK.SCDashboardServices.API import *
from SDK.SCMetricsServices.API import *
from SDK.SCBIServices.API import *


grids = SCGrids()
dashboard = SCDashboard()
metrics = SCMetrics()
bi = SCBi()


org = 'SMARTCLEAN'
PropId = '3b749a681d14446292b6c79b48403bbd'

Property = grids.readProperty(org=org,pid = 'scnoop',propid = PropId,client='Sync')
print(Property.json())
# print(Property.status_code)





# response = bi.getReportingServicesForPrincipalOrg(org='SMARTCLEAN',pid='scnoop',expJson = json.dumps(request_body), client='Sync')
# print(response)