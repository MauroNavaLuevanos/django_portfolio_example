from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SocialNetworksSerializer
from .models import SocialNetwork

# Create your views here.

@api_view(['GET'])
def get_social(request):
    qs = SocialNetwork.objects.all().order_by('name')
    serializer = SocialNetworksSerializer(qs, many=True)
    return Response(serializer.data)
