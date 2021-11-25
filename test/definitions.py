from test import grids
from test import device_management

SDK_CLIENT_TYPE_ASYNC = 'Async'
SDK_CLIENT_TYPE_SYNC = 'Sync'

VALID_CLIENT_TYPES = {
    SDK_CLIENT_TYPE_SYNC,
    SDK_CLIENT_TYPE_ASYNC
}

# region Service Names and respective Ops

# region Definitions for Service: grids
SERVICE_ID_GRIDS = grids.SERVICE_ID
GRIDS_OP_GET_ZONE_INFO = grids.OP_READ_ZONE
GRIDS_OP_GET_BUILDING_INFO = grids.OP_READ_BUILDING
GRIDS_OP_GET_PROPERTY_INFO = grids.OP_READ_PROPERTY
# endregion

# region Definitions for Service: device management
SERVICE_ID_DEVICE_MANAGEMENT = device_management.SERVICE_ID
DEVICE_MANAGEMENT_OP_REALSENSE_MIGRATED = device_management.OP_REALSENSE_MIGRATED
DEVICE_MANAGEMENT_OP_GET_DEVICE_SLOTS = device_management.OP_GET_DEVICE_SLOTS
# endregion

# region Definitions for Service: workforce management
SERVICE_ID_WORKFORCE_MANAGEMENT = 'SCWorkforcemanagement'
WORKFORCE_MGMT_OP_ASSIGN_INCIDENT = 'assignIncident'
WORKFORCE_MGMT_OP_FIND_AVAILABILITY = 'findAvailability'
WORKFORCE_MGMT_OP_CREATE_INCIDENT_NO_ASSIGNEE = 'createIncidentWithoutAssignee'
# endregion

# Definitions for Messaging service? (awaiting details)
SEND_SMS_OP = 'sendSMS'
# endregion
