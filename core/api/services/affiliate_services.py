import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.affiliate import Affiliate

logger = logging.getLogger(__name__)


class AffiliateService:
    def __init__(self):
        pass

    def get_all(self) -> List[Affiliate]:
        """Retrieve all Affiliate instances."""
        try:
            return Affiliate.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Affiliate: {e}")
            raise e

    def get_by_id(self, pk: int) -> Affiliate:
        """Retrieve a specific Affiliate by ID."""
        try:
            return Affiliate.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Affiliate not found with ID: {pk}")
            raise ValueError(f"Affiliate with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Affiliate with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Affiliate:
        """Create a new Affiliate instance."""
        try:
            obj = Affiliate(**data)
            obj.save()
            logger.info(f"Affiliate created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Affiliate: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Affiliate:
        """Update an existing Affiliate instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Affiliate updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Affiliate not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Affiliate with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Affiliate by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Affiliate deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Affiliate not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Affiliate with ID {pk}: {e}")
            raise e
