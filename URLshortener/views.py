from django.shortcuts import redirect,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from URLS.models import URL
from django.utils import timezone
import secrets,string

def generator():
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(8))

@api_view(["GET"])
def shortened_url(request,url):
    try:
        x = URL.objects.get(url=url)
        return Response({"shorturl": "http://127.0.0.1:8000/" + x.short_url, "count": x.count })
    except URL.DoesNotExist:
        pass
    shorturl = generator()
    x = URL.objects.get(short_url=shorturl)
    while(x):
        if x.time < 7:
            x.time = timezone.now()
            x.url = url
            x.count = 0
            x.save()
            return Response({"shorturl": "http://127.0.0.1:8000/" + x.short_url, "count": x.count })
        shorturl = generator()
    x = URL.objects.create(url=url,short_url = shorturl)
    return Response({"name":"127.0.0.1:8000/"+x.short_url, "count": x.count })

def bypass(request,shorturl):
    try:
        x = URL.objects.get(short_url=shorturl)
        x.count+=1
        x.save()
        return redirect("http://"+x.url)
    except URL.DoesNotExist:
        pass
@api_view(["GET"])
def count(request,shorturl):
    try:
        x = URL.objects.get(short_url=shorturl)
        return Response({"count":x.count})
    except URL.DoesNotExist:
        pass

