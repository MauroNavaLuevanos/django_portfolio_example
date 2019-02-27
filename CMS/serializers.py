from rest_framework.serializers import ModelSerializer

from .models import CMS

class CMSSerializer(ModelSerializer):
    class Meta:
        model = CMS
        fields = (
            'get_picture',
            'get_location',
            'in_development',
            'email',
            'phone',
            'cellphone',
            'city',
            'state',
            'country',
            'linkedin',
            'get_company',
            'work_phone',
            'work_city',
            'work_state',
            'work_country',
            'work_email',
        )
