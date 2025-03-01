import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.support_ticket import SupportTicket

logger = logging.getLogger(__name__)


class SupportTicketService:
    def __init__(self):
        pass

    def get_all(self) -> List[SupportTicket]:
        """Retrieve all SupportTicket instances."""
        try:
            return SupportTicket.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all SupportTicket: {e}")
            raise e

    def get_by_id(self, pk: int) -> SupportTicket:
        """Retrieve a specific SupportTicket by ID."""
        try:
            return SupportTicket.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"SupportTicket not found with ID: {pk}")
            raise ValueError(f"SupportTicket with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving SupportTicket with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> SupportTicket:
        """Create a new SupportTicket instance."""
        try:
            obj = SupportTicket(**data)
            obj.save()
            logger.info(f"SupportTicket created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating SupportTicket: {e}")
            raise e

    def update(self, pk: int, data: dict) -> SupportTicket:
        """Update an existing SupportTicket instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"SupportTicket updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: SupportTicket not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating SupportTicket with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific SupportTicket by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"SupportTicket deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: SupportTicket not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting SupportTicket with ID {pk}: {e}")
            raise e
