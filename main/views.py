from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UrlSerializer
from .helpers import generate_unique_code
from rest_framework import status
from .models import Urls

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)