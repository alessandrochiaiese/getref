import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.campaign import Campaign

logger = logging.getLogger(__name__)


class CampaignService:
    def __init__(self):
        pass

    def get_all(self) -> List[Campaign]:
        """Retrieve all Campaign instances."""
        try:
            return Campaign.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Campaign: {e}")
            raise e

    def get_by_id(self, pk: int) -> Campaign:
        """Retrieve a specific Campaign by ID."""
        try:
            return Campaign.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Campaign not found with ID: {pk}")
            raise ValueError(f"Campaign with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Campaign with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Campaign:
        """Create a new Campaign instance."""
        try:
            obj = Campaign(**data)
            obj.save()
            logger.info(f"Campaign created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Campaign: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Campaign:
        """Update an existing Campaign instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Campaign updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Campaign not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Campaign with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Campaign by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Campaign deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Campaign not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Campaign with ID {pk}: {e}")
            raise e
