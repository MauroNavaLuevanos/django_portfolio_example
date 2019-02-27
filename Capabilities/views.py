from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CapabilitySerializer, ServicesSerializer
from .models import Capability, Service

# Create your views here.


@api_view(['GET'])
def get_capabilities(request):
    qs = Capability.objects.all().order_by('order')
    serializer = CapabilitySerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_services(request):
    qs = Service.objects.all().order_by('order')
    serializer = ServicesSerializer(qs, many=True)
    return Response(serializer.data)
