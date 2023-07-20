from marshmallow import Schema, fields, validate

class RoleSchema(Schema):
    id = fields.String(dump_only=True)
    role = fields.String(required=True)
    class Meta:
            strict = True