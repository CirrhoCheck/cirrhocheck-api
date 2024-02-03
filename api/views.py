from rest_framework.response import Response
from rest_framework.decorators import api_view

from administration.models import DummyItem
from .serializers import DummyItemSerializer

@api_view(['GET'])
def getDummyItem(request):
    dummyItems = DummyItem.objects.all()
    serializer = DummyItemSerializer(dummyItems, many = True)
    return Response(serializer.data)