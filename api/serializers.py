from rest_framework import serializers
from djJson.models import Movie

class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    active = serializers.BooleanField()

