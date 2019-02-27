from rest_framework.serializers import ModelSerializer

from .models import Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'pk',
            'name',
            'description',
            'link',
            'get_date',
            'get_stack',
            'get_type',
            'get_company',
            'get_picture',
        )
