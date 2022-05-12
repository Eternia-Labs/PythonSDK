SERVICE_ID = "SCDeviceManagement"

OP_REALSENSE_MIGRATED = "realSenseMigrated"
OP_GET_DEVICE_SLOTS = "getDeviceSlots"
OPS = {OP_REALSENSE_MIGRATED, OP_GET_DEVICE_SLOTS}

_DATA_TEMPLATE_REALSENSE_MIGRATED = {"ID": "TestPID", "Migrated": False}

_DATA_TEMPLATE_GET_DEVICE_SLOTS = {
    "Slots": [
        {
            "ATTR": "attr#devices#info#ID",
            "Alias": "TestAliasId",
            "Commissioned": 0,
            "Conn": "BLE",
            "CreatedBy": "smartclean",
            "CreatedOn": 1635494680,
            "DeviceNotAssociated": 0,
            "Devid": "55954A2B11",
            "Display": "Paper Towel",
            "FirmwareVersion": "2",
            "ID": "SCDevices#ID",
            "LID": "7911afb00468475da10ae8a57bdfe80b",
            "NS": "DEVICE_INFO_GENERAL",
            "Org": "LHN",
            "PID": "TestPID",
            "Params": {"DeviceParams": {"MAX": 110, "OFFSET": 5}},
            "ParamsNotConfigured": 1,
            "ParamsOnDeviceNotConfigured": 0,
            "PartnerId": "SMARTCLEAN",
            "PropId": "TestPropId",
            "ProviderOrg": "SMARTCLEAN",
            "RequiresHealthCheck": 1,
            "RequiresOnDeviceConfiguration": 0,
            "RequiresParamsConfiguration": 1,
            "SRN": "null",
            "TZ": "Asia/Singapore",
            "Type": "SMARTCLEAN#DevType",
            "Unhealthy": 0,
            "UpdatedBy": "smartclean",
            "UpdatedOn": 1635496487,
            "ZoneId": "ZoneID",
        }
    ],
    "code": "SUCCESS",
    "message": "Successfully fetched given slots",
}

DATA_TEMPLATE_BY_OP = {
    OP_REALSENSE_MIGRATED: _DATA_TEMPLATE_REALSENSE_MIGRATED,
    OP_GET_DEVICE_SLOTS: _DATA_TEMPLATE_GET_DEVICE_SLOTS,
}
