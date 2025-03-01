import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.conversion import Conversion

logger = logging.getLogger(__name__)


class ConversionService:
    def __init__(self):
        pass

    def get_all(self) -> List[Conversion]:
        """Retrieve all Conversion instances."""
        try:
            return Conversion.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Conversion: {e}")
            raise e

    def get_by_id(self, pk: int) -> Conversion:
        """Retrieve a specific Conversion by ID."""
        try:
            return Conversion.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Conversion not found with ID: {pk}")
            raise ValueError(f"Conversion with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Conversion with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Conversion:
        """Create a new Conversion instance."""
        try:
            obj = Conversion(**data)
            obj.save()
            logger.info(f"Conversion created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Conversion: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Conversion:
        """Update an existing Conversion instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Conversion updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Conversion not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Conversion with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Conversion by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Conversion deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Conversion not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Conversion with ID {pk}: {e}")
            raise e
