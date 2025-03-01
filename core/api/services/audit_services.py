import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.audit import Audit

logger = logging.getLogger(__name__)


class AuditService:
    def __init__(self):
        pass

    def get_all(self) -> List[Audit]:
        """Retrieve all Audit instances."""
        try:
            return Audit.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Audit: {e}")
            raise e

    def get_by_id(self, pk: int) -> Audit:
        """Retrieve a specific Audit by ID."""
        try:
            return Audit.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Audit not found with ID: {pk}")
            raise ValueError(f"Audit with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Audit with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Audit:
        """Create a new Audit instance."""
        try:
            obj = Audit(**data)
            obj.save()
            logger.info(f"Audit created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Audit: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Audit:
        """Update an existing Audit instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Audit updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Audit not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Audit with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Audit by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Audit deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Audit not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Audit with ID {pk}: {e}")
            raise e
