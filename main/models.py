from django.db import models

class Urls(models.Model):
    actual_url = models.CharField(max_length=250)
    short_code = models.CharField(max_length=10, unique = True)
    last_created_or_used = models.DateTimeField(auto_now = True)

class Statistics(models.Model):
    total_links = models.PositiveIntegerField(default=0)
    total_clicks = models.PositiveIntegerField(default=0)
    active_links = models.PositiveIntegerField(default=0)
