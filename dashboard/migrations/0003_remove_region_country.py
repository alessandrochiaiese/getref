# Generated by Django 5.1.3 on 2025-01-10 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_sector_region_latitude_region_longitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='country',
        ),
    ]