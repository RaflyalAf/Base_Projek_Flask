from marshmallow import Schema,fields

class EmailNotificationSchema(Schema):
    email_notif_id=fields.Integer(dump_only=True)
    email_notif_from=fields.String(required=True)
    email_notif_to=fields.String(required=True)
    email_notif_body=fields.String(required=True)
    email_notif_isRead=fields.Boolean(dump_only=True)
    
    class Meta:
        strict=True