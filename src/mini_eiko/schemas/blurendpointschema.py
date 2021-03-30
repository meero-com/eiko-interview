from marshmallow import Schema, fields


class BlurEndpointSchema(Schema):
    url = fields.Url(required=True)
