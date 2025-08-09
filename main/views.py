from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UrlSerializer, StatisticsSerializer
from .helpers import generate_unique_code
from rest_framework import status
from .models import Urls, Statistics
from django.shortcuts import redirect

@api_view(['POST'])
def shorten(request):
    payload = dict(request.data)
    actual_url = payload.get("actual_url")
    existing = Urls.objects.filter(actual_url = actual_url).first()
    if existing:
        serializer = UrlSerializer(existing)
        return Response(serializer.data, status=status.HTTP_200_OK)
    payload['short_code'] = generate_unique_code()
    serializer = UrlSerializer(data=payload)
    if serializer.is_valid():
        serializer.save()
        stat, flag = Statistics.objects.get_or_create(pk = 1)
        stat.total_links += 1
        stat.active_links += 1
        stat.save()
        stat_serializer = StatisticsSerializer(stat)
        data = serializer.data | stat_serializer.data
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_actual_url(request, short_code):
    existing = Urls.objects.filter(short_code = short_code).first()
    if existing:
        stat, flag = Statistics.objects.get_or_create(pk = 1)
        stat.total_clicks += 1
        stat.save()
        return redirect(existing.actual_url)
    return Response({"error":"URL not found"}, status=status.HTTP_400_BAD_REQUEST)