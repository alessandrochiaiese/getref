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
        regions_to_create = []
        for region_data in regions_data:
            if not Region.objects.filter(id=region_data['id']).exists():
                region = Region(
                    id=region_data['id'],
                    name=region_data['name'],
                    latitude=region_data['latitude'],
                    longitude=region_data['longitude']
                )
                regions_to_create.append(region)
        
        Region.objects.bulk_create(regions_to_create)
        self.stdout.write(f'{len(regions_to_create)} regioni create con successo.')

        # Create Province objects
        provinces_to_create = []
        for province_data in provinces_data:
            if not Province.objects.filter(id=province_data['id']).exists():
                region = Region.objects.get(id=province_data['id_region'])
                province = Province(
                    id=province_data['id'],
                    region=region,
                    name=province_data['name'],
                    automotive_acronym=province_data['automotive_acronym'],
                    latitude=province_data['latitude'],
                    longitude=province_data['longitude']
                )
                provinces_to_create.append(province)
        
        Province.objects.bulk_create(provinces_to_create)
        self.stdout.write(f'{len(provinces_to_create)} province create con successo.')

        # Create Municipality objects
        municipalities_to_create = []
        for municipality_data in municipalities_data:
            if not Municipality.objects.filter(id=municipality_data['id']).exists():
                region = Region.objects.get(id=municipality_data['id_region'])
                province = Province.objects.get(id=municipality_data['id_province'])
                municipality = Municipality(
                    id=municipality_data['id'],
                    region=region,
                    province=province,
                    name=municipality_data['name'],
                    is_capital_province=municipality_data['is_capital_province'],
                    cadastral_code=municipality_data['cadastral_code'],
                    latitude=municipality_data['latitude'],
                    longitude=municipality_data['longitude']
                )
                municipalities_to_create.append(municipality)
        
        Municipality.objects.bulk_create(municipalities_to_create)
        self.stdout.write(f'{len(municipalities_to_create)} comuni creati con successo.')
