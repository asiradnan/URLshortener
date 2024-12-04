from django.db import models
from django.utils import timezone
class URL(models.Model):
    url = models.CharField(max_length=2500)
    short_url = models.CharField(max_length=16)
    count  = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)

class TotalCount(models.Model):
    total_count = models.PositiveBigIntegerField(default=0)
    click_count = models.PositiveBigIntegerField(default=0)