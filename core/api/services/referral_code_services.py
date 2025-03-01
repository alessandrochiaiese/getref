import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.referral_code import ReferralCode

logger = logging.getLogger(__name__)


class ReferralCodeService:
    def __init__(self):
        pass

    def get_all(self) -> List[ReferralCode]:
        """Retrieve all ReferralCode instances."""
        try:
            return ReferralCode.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all ReferralCode: {e}")
            raise e

    def get_by_id(self, pk: int) -> ReferralCode:
        """Retrieve a specific ReferralCode by ID."""
        try:
            return ReferralCode.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"ReferralCode not found with ID: {pk}")
            raise ValueError(f"ReferralCode with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving ReferralCode with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> ReferralCode:
        """Create a new ReferralCode instance."""
        try:
            obj = ReferralCode(**data)
            obj.save()
            logger.info(f"ReferralCode created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating ReferralCode: {e}")
            raise e

    def update(self, pk: int, data: dict) -> ReferralCode:
        """Update an existing ReferralCode instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"ReferralCode updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: ReferralCode not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating ReferralCode with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific ReferralCode by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"ReferralCode deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: ReferralCode not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting ReferralCode with ID {pk}: {e}")
            raise e
