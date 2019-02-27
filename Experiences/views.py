from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ExperiencesSerializer
from .models import Experience

# Create your views here.

@api_view(['GET'])
def get_experiences(request):
    qs = Experience.objects.all().order_by('-since')
    serializer = ExperiencesSerializer(qs, many=True)
    return Response(serializer.data)
