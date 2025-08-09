from rest_framework import serializers
from .models import Urls, Statistics

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'
        
class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'