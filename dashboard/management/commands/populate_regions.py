import json
import os
from django.core.management.base import BaseCommand
from dashboard.models import Region, Province, Municipality
from getref.settings import STATIC_ROOT

class Command(BaseCommand):
    help = 'Popola le tabelle Region, Province, e Municipality da file JSON'

    def handle(self, *args, **options):
        # Load data from JSON files
        with open(os.path.join(STATIC_ROOT, 'cities', 'regions.json'), 'r') as file:
            regions_data = json.load(file)

        # Create Region objects
        for region_data in regions_data:
            region, created = Region.objects.get_or_create(
                id=region_data['id'],
                defaults={
                    'name': region_data['name'],
                    'latitude': region_data['latitude'],
                    'longitude': region_data['longitude']
                }
            )
            if created:
                self.stdout.write(f'Regione {region.name} creata con successo.')
            else:
                self.stdout.write(f'Regione {region.name} già esistente.')
