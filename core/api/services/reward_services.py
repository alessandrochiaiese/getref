import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.reward import Reward

logger = logging.getLogger(__name__)


class RewardService:
    def __init__(self):
        pass

    def get_all(self) -> List[Reward]:
        """Retrieve all Reward instances."""
        try:
            return Reward.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Reward: {e}")
            raise e

    def get_by_id(self, pk: int) -> Reward:
        """Retrieve a specific Reward by ID."""
        try:
            return Reward.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Reward not found with ID: {pk}")
            raise ValueError(f"Reward with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Reward with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Reward:
        """Create a new Reward instance."""
        try:
            obj = Reward(**data)
            obj.save()
            logger.info(f"Reward created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Reward: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Reward:
        """Update an existing Reward instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Reward updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Reward not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Reward with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Reward by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Reward deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Reward not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Reward with ID {pk}: {e}")
            raise e
