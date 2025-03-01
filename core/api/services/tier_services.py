import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.tier import Tier

logger = logging.getLogger(__name__)


class TierService:
    def __init__(self):
        pass

    def get_all(self) -> List[Tier]:
        """Retrieve all Tier instances."""
        try:
            return Tier.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Tier: {e}")
            raise e

    def get_by_id(self, pk: int) -> Tier:
        """Retrieve a specific Tier by ID."""
        try:
            return Tier.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Tier not found with ID: {pk}")
            raise ValueError(f"Tier with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Tier with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Tier:
        """Create a new Tier instance."""
        try:
            obj = Tier(**data)
            obj.save()
            logger.info(f"Tier created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Tier: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Tier:
        """Update an existing Tier instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Tier updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Tier not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Tier with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Tier by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Tier deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Tier not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Tier with ID {pk}: {e}")
            raise e
