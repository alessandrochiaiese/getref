import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.commission import Commission

logger = logging.getLogger(__name__)


class CommissionService:
    def __init__(self):
        pass

    def get_all(self) -> List[Commission]:
        """Retrieve all Commission instances."""
        try:
            return Commission.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Commission: {e}")
            raise e

    def get_by_id(self, pk: int) -> Commission:
        """Retrieve a specific Commission by ID."""
        try:
            return Commission.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Commission not found with ID: {pk}")
            raise ValueError(f"Commission with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Commission with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Commission:
        """Create a new Commission instance."""
        try:
            obj = Commission(**data)
            obj.save()
            logger.info(f"Commission created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Commission: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Commission:
        """Update an existing Commission instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Commission updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Commission not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Commission with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Commission by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Commission deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Commission not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Commission with ID {pk}: {e}")
            raise e
