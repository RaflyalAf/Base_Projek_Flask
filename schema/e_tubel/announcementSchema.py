from marshmallow import Schema, fields
class AnnouncementSchema(Schema):
    announce_id=fields.Integer(dump_only=True)
    announce_body=fields.String(required=True)
    
    class Meta:
        strict=True