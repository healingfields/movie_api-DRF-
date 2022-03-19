from logging import exception
from wsgiref.validate import validator
from rest_framework import serializers
from djJson.models import WatchList, StreamPlatform
from rest_framework import validators


class WatchListSerializer(serializers.ModelSerializer):
    name_length = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = ['name', 'name_length', 'storyline', 'active', 'created', 'platform']
        # exclude = ['active']

    def get_name_length(self, obj):
        return len(obj.name)


class StreamPlatformSerializer(serializers.ModelSerializer):
    # adding s for plural is necessary, wont work w/o it
    watchlists = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'

# def check_length(value):
#     if len(value)<3:
#         raise validators.ValidationError('name must contains more than 3 caracteres')
#     return value

# class MovieSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=150, validators=[check_length])
#     description = serializers.CharField(max_length=250)
#     active = serializers.BooleanField()

#     def create(self, validated_date):
#         return Movie.objects.create(**validated_date)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise validators.ValidationError('name and description should not be the same')
#         return data

# def validate_name(self, value):
#     if len(value)<2:
#         raise validators.ValidationError('name must contains more than 2 caracteres')
#     return value
