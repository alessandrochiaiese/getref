# referral_system/services.py

import datetime
import logging
 
from django.contrib.auth import get_user_model
from typing import List

from referral.models.referral_code import ReferralCode
from referral.models.referral_commission import ReferralCommission
 

User = get_user_model()


# Set up a logger
logger = logging.getLogger(__name__)


class ReferralCommissionService():
    def __init__(self) -> None:
        pass
    
    def get_referral_commissions(self) -> List[ReferralCommission]:
        try:
            referral_commissions = ReferralCommission.objects.all() 
            return referral_commissions
        except ReferralCommission.DoesNotExist:
            logger.warning(f"ReferralCommission not found")
            raise ValueError("ReferralCommission not found")
     
    def get_referral_commission(self, pk) -> ReferralCommission:
        try:
            referral_commission = ReferralCommission.objects.get(id=pk)
            return referral_commission
        except ReferralCommission.DoesNotExist:
            logger.warning(f"ReferralCommission not found: {pk}")
            raise ValueError("ReferralCommission not found")
     
    def create_referral_commission(self, data) -> ReferralCommission:
        try:
            referral_commission = ReferralCommission(
                referral_code = data.get('referral_code'),
                referral_user = data.get('referral_user'),
                commission_date = datetime.datetime.now(), #data.get('commission_date'),
                commission_value = data.get('commission_value'),
                status = data.get('status'),
                trigger_event = data.get('trigger_event'),
                transaction = data.get('transaction'),
                commission_percentage = data.get('commission_percentage'),
                expiry_date = data.get('expiry_date', None))
            referral_commission.save() 
            
            logger.info(f"ReferralCommission created: {referral_commission}")
            return referral_commission
        except Exception as e:
            logger.error(f"Error creating referral_commission: {e}")
            raise e
 
    def update_referral_commission(self, pk, data) -> ReferralCommission:
        try:
            referral_commission = self.get_referral_commission(pk)
            for key, value in data.items():
                setattr(referral_commission, key, value)
            referral_commission.save()
            logger.info(f"ReferralCommission updated: {referral_commission}")
            return referral_commission
        except ReferralCommission.DoesNotExist:
            logger.warning(f"ReferralCommission not found: {pk}")
            raise ValueError("ReferralCommission not found")
        except Exception as e:
            logger.error(f"Error updating referral_commission: {e}")
            raise e
    
    def delete_referral_commission(self, pk) -> None:
        try:
            referral_commission = self.get_referral_commission(pk)
            referral_commission.delete()
            logger.info(f"ReferralCommission deleted: {referral_commission}")
        except ReferralCommission.DoesNotExist:
            logger.warning(f"ReferralCommission not found: {pk}")
            raise ValueError("ReferralCommission not found")
        except Exception as e:
            logger.error(f"Error deleting referral_commission: {e}")
            raise e
        