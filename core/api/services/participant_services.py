import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.participant import Participant

logger = logging.getLogger(__name__)


class ParticipantService:
    def __init__(self):
        pass

    def get_all(self) -> List[Participant]:
        """Retrieve all Participant instances."""
        try:
            return Participant.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Participant: {e}")
            raise e

    def get_by_id(self, pk: int) -> Participant:
        """Retrieve a specific Participant by ID."""
        try:
            return Participant.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Participant not found with ID: {pk}")
            raise ValueError(f"Participant with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Participant with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Participant:
        """Create a new Participant instance."""
        try:
            obj = Participant(**data)
            obj.save()
            logger.info(f"Participant created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Participant: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Participant:
        """Update an existing Participant instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Participant updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Participant not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Participant with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Participant by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Participant deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Participant not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Participant with ID {pk}: {e}")
            raise e
