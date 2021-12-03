SERVICE_ID = 'SCSMSGateway'

OP_PUBLISH_SMS = 'publishSMS'
OPS = {
 OP_PUBLISH_SMS
}

_DATA_TEMPLATE_PUBLISH_SMS = {
 'data': [{'id': '277656409-1',
           'mobile': 'null',
           'status': 'SUBMITTED'
           }],
 'message': 'message Submitted successfully',
 'msgid': '7276277656409943',
 'status': 'OK'
}

DATA_TEMPLATE_BY_OP = {
 OP_PUBLISH_SMS: _DATA_TEMPLATE_PUBLISH_SMS
}
