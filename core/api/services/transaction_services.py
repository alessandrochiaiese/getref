import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.transaction import Transaction

logger = logging.getLogger(__name__)


class TransactionService:
    def __init__(self):
        pass

    def get_all(self) -> List[Transaction]:
        """Retrieve all Transaction instances."""
        try:
            return Transaction.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all Transaction: {e}")
            raise e

    def get_by_id(self, pk: int) -> Transaction:
        """Retrieve a specific Transaction by ID."""
        try:
            return Transaction.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"Transaction not found with ID: {pk}")
            raise ValueError(f"Transaction with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving Transaction with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> Transaction:
        """Create a new Transaction instance."""
        try:
            obj = Transaction(**data)
            obj.save()
            logger.info(f"Transaction created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating Transaction: {e}")
            raise e

    def update(self, pk: int, data: dict) -> Transaction:
        """Update an existing Transaction instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"Transaction updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: Transaction not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating Transaction with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific Transaction by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"Transaction deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: Transaction not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting Transaction with ID {pk}: {e}")
            raise e
