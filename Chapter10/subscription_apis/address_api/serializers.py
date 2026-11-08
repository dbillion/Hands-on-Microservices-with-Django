from bson import ObjectId
from rest_framework import serializers

from .models import Address


class ObjectIdField(serializers.Field):
    """Serialise a MongoDB ObjectId as its 24-character hex string."""

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)


class AddressSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)

    def validate(self, data):
        if 'country' in data and 'postalcode' in data:
            if data["country"] == "Utopia" and len(data["postalcode"]) != 7:
                raise serializers.ValidationError("The postal code for Utopia must be seven characters long.")
        return data
