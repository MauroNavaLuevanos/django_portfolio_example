from rest_framework.serializers import ModelSerializer

from .models import Experience

class ExperiencesSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            'pk',
            'position',
            'get_timeline',
            'description',
            'get_company',
        )
