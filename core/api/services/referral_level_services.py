import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.referral_level import ReferralLevel

logger = logging.getLogger(__name__)


class ReferralLevelService:
    def __init__(self):
        pass

    def get_all(self) -> List[ReferralLevel]:
        """Retrieve all ReferralLevel instances."""
        try:
            return ReferralLevel.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all ReferralLevel: {e}")
            raise e

    def get_by_id(self, pk: int) -> ReferralLevel:
        """Retrieve a specific ReferralLevel by ID."""
        try:
            return ReferralLevel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"ReferralLevel not found with ID: {pk}")
            raise ValueError(f"ReferralLevel with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving ReferralLevel with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> ReferralLevel:
        """Create a new ReferralLevel instance."""
        try:
            obj = ReferralLevel(**data)
            obj.save()
            logger.info(f"ReferralLevel created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating ReferralLevel: {e}")
            raise e

    def update(self, pk: int, data: dict) -> ReferralLevel:
        """Update an existing ReferralLevel instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"ReferralLevel updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: ReferralLevel not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating ReferralLevel with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific ReferralLevel by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"ReferralLevel deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: ReferralLevel not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting ReferralLevel with ID {pk}: {e}")
            raise e
