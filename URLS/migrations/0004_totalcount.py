# Generated by Django 5.0.6 on 2024-06-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLS', '0003_url_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_count', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
