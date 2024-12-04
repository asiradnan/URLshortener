from django.shortcuts import redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from URLS.models import URL, TotalCount
from django.utils import timezone
import secrets,string
from django.utils import timezone
from datetime import timedelta
import urllib.parse
import qrcode
from io import BytesIO
import base64

def generator():
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(4))

@api_view(["GET"])
def shortened_url(request,url):
    url = urllib.parse.unquote(url)
    try:
        x = URL.objects.get(url=url)
        shorturl = "https://chottourlserver.asiradnan.com/" + x.short_url
        img = qrcode.make(shorturl)
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        tc, createdtc = TotalCount.objects.get_or_create(id=1)
        tc.total_count +=1 
        tc.save()
        return Response({"shorturl": shorturl, "count": x.count,"qrcode":img_base64 })
    except URL.DoesNotExist:
        shorturl = generator()
        x = URL.objects.filter(short_url=shorturl)
        while(x.exists()):
            if timezone.now() - timedelta(days=5) > x.first().time:
                x.time = timezone.now()
                x.url = url
                x.count = 0
                x.save()
                shorturl = "https://chottourlserver.asiradnan.com/" + x.short_url
                img = qrcode.make(shorturl)
                buffer = BytesIO()
                img.save(buffer)
                buffer.seek(0)
                img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                tc, createdtc = TotalCount.objects.get_or_create(id=1)
                tc.total_count +=1 
                tc.save()
                return Response({"shorturl": shorturl, "count": x.count, "qrcode":img_base64 })
            shorturl = generator()
            x = URL.objects.filter(short_url=shorturl)
        x = URL.objects.create(url=url,short_url = shorturl)
        shorturl = "https://chottourlserver.asiradnan.com/" + x.short_url
        img = qrcode.make(shorturl)
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        tc, createdtc = TotalCount.objects.get_or_create(id=1)
        tc.total_count +=1 
        tc.save()
        return Response({"shorturl": shorturl, "count": x.count, "qrcode":img_base64 })
    
def bypass(request,shorturl):
    try:
        x = URL.objects.get(short_url=shorturl)
        x.count+=1
        x.save()
        tc,createdtc = TotalCount.objects.get_or_create(id=1)
        tc.click_count +=1 
        tc.save()
        return redirect("http://" + x.url)
    except URL.DoesNotExist:
        pass
@api_view(["GET"])
def count(request,shorturl):
    try:
        x = URL.objects.get(short_url=shorturl)
        return Response({"count":x.count})
    except URL.DoesNotExist:
        pass

@api_view(["GET"])
def totalcount(request):
    tc,createdtc = TotalCount.objects.get_or_create(id=1)
    return Response({"total_count":tc.total_count,"click_count":tc.click_count,"active_links":URL.objects.count()})

