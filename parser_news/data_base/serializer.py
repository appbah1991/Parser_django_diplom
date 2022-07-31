from .models import News, Url, Title
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = '__all__'

class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'