from marshmallow import schema, fields


class MailResponse(schema.Schema):
    name = fields.Str()
    mobile = fields.Str()
    code = fields.Str()
    email = fields.Str()
