
from marshmallow import Schema, fields, ValidationError

def validate_age(value):
    if value <= 0:
        raise ValidationError("Age must be greater than zero.")

def validate_phone(value):
    if not value.isdigit() or len(value) != 8:
        raise ValidationError("Phone number must be 8 digits long and contain only numbers.")

class PersonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    phone = fields.Str(required=True, validate=[validate_phone], error_messages={"invalid": "Phone number must be 8 digits long and contain only numbers."})
    address = fields.Str(required=True)
    age = fields.Int(required=True, validate=[validate_age], error_messages={"invalid": "Age must be a valid integer."})
