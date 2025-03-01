import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.bonus import Bonus

logger = logging.getLogger(__name__)


class BonusService:
    def __init__(self):
        pass

    def get_all(self) -> List[Bonus]:
        """Retrieve all Bonus instances."""
        try:
            return Bonus.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Bonus: {e}")
            raise e

    def get_by_id(self, pk: int) -> Bonus:
        """Retrieve a specific Bonus by ID."""
        try:
            return Bonus.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Bonus not found with ID: {pk}")
            raise ValueError(f"Bonus with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Bonus with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Bonus:
        """Create a new Bonus instance."""
        try:
            obj = Bonus(**data)
            obj.save()
            logger.info(f"Bonus created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Bonus: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Bonus:
        """Update an existing Bonus instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Bonus updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Bonus not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Bonus with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Bonus by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Bonus deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Bonus not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Bonus with ID {pk}: {e}")
            raise e
