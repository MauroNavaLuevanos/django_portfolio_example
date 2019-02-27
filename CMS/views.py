from rest_framework.decorators import api_view
from rest_framework.response import Response

from Capabilities.models import Service, Capability
from Experiences.models import Experience
from Social.models import SocialNetwork
from .serializers import CMSSerializer
from .models import CMS

# Create your views here.

@api_view(['GET'])
def get_general(request):
    qs = CMS.objects.get()
    serializer = CMSSerializer(qs)
    return Response(serializer.data)
