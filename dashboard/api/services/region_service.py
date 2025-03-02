import datetime
import logging
from typing import List
from django.http import JsonResponse
from dashboard.models.region import Region
from dashboard.api.serializers import RegionSerializer 
from django.contrib.auth.models import User

# Set up a logger
logger = logging.getLogger(__name__)

class RegionService():
    def __init__(self) -> None:
        pass

    def get_regions(self) ->  List[Region]:
        try:
            regions = Region.objects.all() 
            return regions
        except Region.DoesNotExist:
            logger.warning(f"Region not found")
            raise ValueError("Region not found")
     
    def get_region(self, pk) -> Region:
        try:
            region = Region.objects.get(id=pk)
            return region
        except Region.DoesNotExist:
            logger.warning(f"Region not found: {pk}")
            raise ValueError("Region not found")
     
    def create_region(self, data) -> Region:
        try:
            region = Region.objects.create(
                name=data.get('name'),
                latitude=data.get('latitude'),
                longitude=data.get('longitude')
            )
            region.save()
 
            logger.info(f"Region created: {region}")
            return region
        except Exception as e:
            logger.error(f"Error creating region: {e}")
            raise e
 
    def update_region(self, region_id, data) -> Region:
        try:
            # Recupera il profilo esistente
            region = Region.objects.get(id=region_id)

            # Aggiorna i campi
            for field, value in data.items():
                setattr(region, field, value)

            # Salva il profilo aggiornato
            region.save()
            return region

        except Region.DoesNotExist:
            # Gestisci l'errore se il profilo non esiste
            raise Region.DoesNotExist(f"Region with id {region_id} does not exist.")

        except Exception as e:
            # Logga e rilancia qualsiasi altro errore
            logger.error(f"Error updating region: {e}")
            raise e
    
    def delete_region(self, pk) -> None:
        try:
            region = self.get_region(pk)
            region.delete()
            logger.info(f"Region deleted: {region}")
        except Exception as e:
            logger.error(f"Error deleting region: {e}")
            raise e