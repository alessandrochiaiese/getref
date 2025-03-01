import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.engagement import Engagement

logger = logging.getLogger(__name__)


class EngagementService:
    def __init__(self):
        pass

    def get_all(self) -> List[Engagement]:
        """Retrieve all Engagement instances."""
        try:
            return Engagement.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Engagement: {e}")
            raise e

    def get_by_id(self, pk: int) -> Engagement:
        """Retrieve a specific Engagement by ID."""
        try:
            return Engagement.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Engagement not found with ID: {pk}")
            raise ValueError(f"Engagement with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Engagement with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Engagement:
        """Create a new Engagement instance."""
        try:
            obj = Engagement(**data)
            obj.save()
            logger.info(f"Engagement created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Engagement: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Engagement:
        """Update an existing Engagement instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Engagement updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Engagement not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Engagement with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Engagement by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Engagement deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Engagement not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Engagement with ID {pk}: {e}")
            raise e
