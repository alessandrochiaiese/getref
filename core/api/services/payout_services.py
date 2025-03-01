import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.payout import Payout

logger = logging.getLogger(__name__)


class PayoutService:
    def __init__(self):
        pass

    def get_all(self) -> List[Payout]:
        """Retrieve all Payout instances."""
        try:
            return Payout.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Payout: {e}")
            raise e

    def get_by_id(self, pk: int) -> Payout:
        """Retrieve a specific Payout by ID."""
        try:
            return Payout.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Payout not found with ID: {pk}")
            raise ValueError(f"Payout with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Payout with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Payout:
        """Create a new Payout instance."""
        try:
            obj = Payout(**data)
            obj.save()
            logger.info(f"Payout created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Payout: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Payout:
        """Update an existing Payout instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Payout updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Payout not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Payout with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Payout by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Payout deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Payout not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Payout with ID {pk}: {e}")
            raise e
