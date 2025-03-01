import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.notification import Notification

logger = logging.getLogger(__name__)


class NotificationService:
    def __init__(self):
        pass

    def get_all(self) -> List[Notification]:
        """Retrieve all Notification instances."""
        try:
            return Notification.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Notification: {e}")
            raise e

    def get_by_id(self, pk: int) -> Notification:
        """Retrieve a specific Notification by ID."""
        try:
            return Notification.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Notification not found with ID: {pk}")
            raise ValueError(f"Notification with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Notification with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Notification:
        """Create a new Notification instance."""
        try:
            obj = Notification(**data)
            obj.save()
            logger.info(f"Notification created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Notification: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Notification:
        """Update an existing Notification instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Notification updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Notification not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Notification with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Notification by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Notification deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Notification not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Notification with ID {pk}: {e}")
            raise e
