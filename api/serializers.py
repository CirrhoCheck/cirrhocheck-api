from rest_framework import serializers
from administration.models import DummyItem

class DummyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyItem
        fields = '__all__'