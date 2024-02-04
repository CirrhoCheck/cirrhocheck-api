from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from administration.models.dummy_item import DummyItem
from .serializers import DummyItemSerializer

class GetDummyItemAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request) -> Response:
        dummyItems = DummyItem.objects.all()
        serializer = DummyItemSerializer(dummyItems, many = True)
        return Response(serializer.data)