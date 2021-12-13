from app import app
from flask_marshmallow import Marshmallow, Schema, fields
from .models import Vehicle

ma = Marshmallow(app)


class DriverSchema(ma.Schema):
    class Meta:
        fields = ("first_name", "last_name")


class VehicleSchema(ma.Schema):
    class Meta:
        fields = ("make", "model", "plate_number", "created_at", "updated_at")




