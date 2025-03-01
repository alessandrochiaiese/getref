import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.performance import Performance

logger = logging.getLogger(__name__)


class PerformanceService:
    def __init__(self):
        pass

    def get_all(self) -> List[Performance]:
        """Retrieve all Performance instances."""
        try:
            return Performance.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Performance: {e}")
            raise e

    def get_by_id(self, pk: int) -> Performance:
        """Retrieve a specific Performance by ID."""
        try:
            return Performance.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Performance not found with ID: {pk}")
            raise ValueError(f"Performance with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Performance with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Performance:
        """Create a new Performance instance."""
        try:
            obj = Performance(**data)
            obj.save()
            logger.info(f"Performance created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Performance: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Performance:
        """Update an existing Performance instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Performance updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Performance not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Performance with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Performance by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Performance deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Performance not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Performance with ID {pk}: {e}")
            raise e
