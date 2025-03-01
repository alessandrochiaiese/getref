import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.program import Program

logger = logging.getLogger(__name__)


class ProgramService:
    def __init__(self):
        pass

    def get_all(self) -> List[Program]:
        """Retrieve all Program instances."""
        try:
            return Program.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Program: {e}")
            raise e

    def get_by_id(self, pk: int) -> Program:
        """Retrieve a specific Program by ID."""
        try:
            return Program.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Program not found with ID: {pk}")
            raise ValueError(f"Program with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Program with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Program:
        """Create a new Program instance."""
        try:
            obj = Program(**data)
            obj.save()
            logger.info(f"Program created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Program: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Program:
        """Update an existing Program instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Program updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Program not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Program with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Program by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Program deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Program not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Program with ID {pk}: {e}")
            raise e
