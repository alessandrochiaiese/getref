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

        with open(os.path.join(STATIC_ROOT, 'cities', 'provinces.json'), 'r') as file:
            provinces_data = json.load(file)

        with open(os.path.join(STATIC_ROOT, 'cities', 'municipalities.json'), 'r') as file:
            municipalities_data = json.load(file)

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

        # Create Province objects
        for province_data in provinces_data:
            region = Region.objects.get(id=province_data['id_region'])
            province, created = Province.objects.get_or_create(
                id=province_data['id'],
                defaults={
                    'region': region,
                    'name': province_data['name'],
                    'automotive_acronym': province_data['automotive_acronym'],
                    'latitude': province_data['latitude'],
                    'longitude': province_data['longitude']
                }
            )
            if created:
                self.stdout.write(f'Provincia {province.name} creata con successo.')
            else:
                self.stdout.write(f'Provincia {province.name} già esistente.')

        # Create Municipality objects
        for municipality_data in municipalities_data:
            region = Region.objects.get(id=municipality_data['id_region'])
            province = Province.objects.get(id=municipality_data['id_province'])
            municipality, created = Municipality.objects.get_or_create(
                id=municipality_data['id'],
                defaults={
                    'region': region,
                    'province': province,
                    'name': municipality_data['name'],
                    'is_capital_province': municipality_data['is_capital_province'],
                    'cadastral_code': municipality_data['cadastral_code'],
                    'latitude': municipality_data['latitude'],
                    'longitude': municipality_data['longitude']
                }
            )
            if created:
                self.stdout.write(f'Comune {municipality.name} creato con successo.')
            else:
                self.stdout.write(f'Comune {municipality.name} già esistente.')
