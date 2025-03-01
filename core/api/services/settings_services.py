import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.settings import Settings

logger = logging.getLogger(__name__)


class SettingsService:
    def __init__(self):
        pass

    def get_all(self) -> List[Settings]:
        """Retrieve all Settings instances."""
        try:
            return Settings.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Settings: {e}")
            raise e

    def get_by_id(self, pk: int) -> Settings:
        """Retrieve a specific Settings by ID."""
        try:
            return Settings.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Settings not found with ID: {pk}")
            raise ValueError(f"Settings with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Settings with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Settings:
        """Create a new Settings instance."""
        try:
            obj = Settings(**data)
            obj.save()
            logger.info(f"Settings created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Settings: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Settings:
        """Update an existing Settings instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Settings updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Settings not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Settings with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Settings by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Settings deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Settings not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Settings with ID {pk}: {e}")
            raise e
