from rest_framework.serializers import ModelSerializer

from .models import SocialNetwork

class SocialNetworksSerializer(ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = (
            'pk',
            'name',
            'link',
            'color',
            'get_icon',
        )
