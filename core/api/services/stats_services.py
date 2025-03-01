import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.stats import Stats

logger = logging.getLogger(__name__)


class StatsService:
    def __init__(self):
        pass

    def get_all(self) -> List[Stats]:
        """Retrieve all Stats instances."""
        try:
            return Stats.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Stats: {e}")
            raise e

    def get_by_id(self, pk: int) -> Stats:
        """Retrieve a specific Stats by ID."""
        try:
            return Stats.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Stats not found with ID: {pk}")
            raise ValueError(f"Stats with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Stats with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Stats:
        """Create a new Stats instance."""
        try:
            obj = Stats(**data)
            obj.save()
            logger.info(f"Stats created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Stats: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Stats:
        """Update an existing Stats instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Stats updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Stats not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Stats with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Stats by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Stats deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Stats not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Stats with ID {pk}: {e}")
            raise e
