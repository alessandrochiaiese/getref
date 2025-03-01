import logging
from typing import List
from django.core.exceptions import ObjectDoesNotExist
from ...models.payment_method import PaymentMethod

logger = logging.getLogger(__name__)


class PaymentMethodService:
    def __init__(self):
        pass

    def get_all(self) -> List[PaymentMethod]:
        """Retrieve all PaymentMethod instances."""
        try:
            return PaymentMethod.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving all PaymentMethod: {e}")
            raise e

    def get_by_id(self, pk: int) -> PaymentMethod:
        """Retrieve a specific PaymentMethod by ID."""
        try:
            return PaymentMethod.objects.get(pk=pk)
        except ObjectDoesNotExist:
            logger.warning(f"PaymentMethod not found with ID: {pk}")
            raise ValueError(f"PaymentMethod with ID {pk} not found")
        except Exception as e:
            logger.error(f"Error retrieving PaymentMethod with ID {pk}: {e}")
            raise e

    def create(self, data: dict) -> PaymentMethod:
        """Create a new PaymentMethod instance."""
        try:
            obj = PaymentMethod(**data)
            obj.save()
            logger.info(f"PaymentMethod created: {obj}")
            return obj
        except Exception as e:
            logger.error(f"Error creating PaymentMethod: {e}")
            raise e

    def update(self, pk: int, data: dict) -> PaymentMethod:
        """Update an existing PaymentMethod instance."""
        try:
            obj = self.get_by_id(pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            logger.info(f"PaymentMethod updated: {obj}")
            return obj
        except ValueError as e:
            logger.warning(f"Update failed: PaymentMethod not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error updating PaymentMethod with ID {pk}: {e}")
            raise e

    def delete(self, pk: int) -> None:
        """Delete a specific PaymentMethod by ID."""
        try:
            obj = self.get_by_id(pk)
            obj.delete()
            logger.info(f"PaymentMethod deleted: {obj}")
        except ValueError as e:
            logger.warning(f"Delete failed: PaymentMethod not found with ID: {pk}")
            raise e
        except Exception as e:
            logger.error(f"Error deleting PaymentMethod with ID {pk}: {e}")
            raise e
