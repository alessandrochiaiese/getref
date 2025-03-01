import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.link import Link

logger = logging.getLogger(__name__)


class LinkService:
    def __init__(self):
        pass

    def get_all(self) -> List[Link]:
        """Retrieve all Link instances."""
        try:
            return Link.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Link: {e}")
            raise e

    def get_by_id(self, pk: int) -> Link:
        """Retrieve a specific Link by ID."""
        try:
            return Link.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Link not found with ID: {pk}")
            raise ValueError(f"Link with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Link with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Link:
        """Create a new Link instance."""
        try:
            obj = Link(**data)
            obj.save()
            logger.info(f"Link created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Link: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Link:
        """Update an existing Link instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Link updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Link not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Link with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Link by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Link deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Link not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Link with ID {pk}: {e}")
            raise e
