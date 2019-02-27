from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.

@api_view(['GET'])
def get_projects(request):
    qs = Project.objects.all().order_by('-date')
    serializer = ProjectSerializer(qs, many=True)
    return Response(serializer.data)
