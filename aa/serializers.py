from rest_framework import serializers
from .models import Raions, Addresses, Devices, Types


class RaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raions
        fields = ['id', 'raion']


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['num', 'address']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ['type']


class DevicesSerializer(serializers.ModelSerializer):
    address = AddressesSerializer(read_only=True)
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Devices
        fields = ['address', 'type', 'ip', 'gw', 'mask']
