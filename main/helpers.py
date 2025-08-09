import random
from .models import Urls
from datetime import datetime, timedelta

def generate_short_code():
    return chr(random.randint(97,97+25))+chr(random.randint(97,97+25))+chr(random.randint(97,97+25))

def generate_unique_code():
    short_code = generate_short_code()
    while True:
        existing = Urls.objects.filter(short_code=short_code).first()
        if existing == None:
            return short_code
        if existing.last_created_or_used + timedelta(days=30) < datetime.now():
            existing.delete()
            return short_code
        short_code = generate_short_code()    