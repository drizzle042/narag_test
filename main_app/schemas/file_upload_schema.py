from marshmallow import Schema, fields


class FileUploadSchema(Schema):
    name = fields.String(required=True)
    file = fields.Raw(type='file', required=True)
    