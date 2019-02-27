from rest_framework.serializers import ModelSerializer

from .models import Capability, Service


class CapabilitySerializer(ModelSerializer):

    class Meta:
        model = Capability
        fields = (
            'pk',
            'name',
            'level',
            'description',
            'color',
            'get_type',
        )


class ServicesSerializer(ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'pk',
            'name',
            'get_icon',
            'description',
            'order',
        )
