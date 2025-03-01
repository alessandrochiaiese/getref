# referral_system/services.py

import datetime
import logging
 
from django.contrib.auth import get_user_model
from typing import List

from referral.models.referral_code import ReferralCode
from referral.models.referral_notification import ReferralNotification
 

User = get_user_model()


# Set up a logger
logger = logging.getLogger(__name__)


class ReferralNotificationService():
    def __init__(self) -> None:
        pass
    
    def get_referral_notifications(self) -> List[ReferralNotification]:
        try:
            referral_notifications = ReferralNotification.objects.all() 
            return referral_notifications
        except ReferralNotification.DoesNotExist:
            logger.warning(f"ReferralNotification not found")
            raise ValueError("ReferralNotification not found")
     
    def get_referral_notification(self, pk) -> ReferralNotification:
        try:
            referral_notification = ReferralNotification.objects.get(id=pk)
            return referral_notification
        except ReferralNotification.DoesNotExist:
            logger.warning(f"ReferralNotification not found: {pk}")
            raise ValueError("ReferralNotification not found")
     
    def create_referral_notification(self, data) -> ReferralNotification:
        try:
            referral_notification = ReferralNotification(
                user = data.get('user'),
                message = data.get('message'),
                date_sent = datetime.datetime.now(), #data.get('date_sent'),
                is_read = data.get('is_read'),
                notification_type = data.get('notification_type'),
                priority = data.get('priority'),
                action_required = data.get('action_required'))
            referral_notification.save() 
            
            logger.info(f"ReferralNotification created: {referral_notification}")
            return referral_notification
        except Exception as e:
            logger.error(f"Error creating referral_notification: {e}")
            raise e
 
    def update_referral_notification(self, pk, data) -> ReferralNotification:
        try:
            referral_notification = self.get_referral_notification(pk)
            for key, value in data.items():
                setattr(referral_notification, key, value)
            referral_notification.save()
            logger.info(f"ReferralNotification updated: {referral_notification}")
            return referral_notification
        except ReferralNotification.DoesNotExist:
            logger.warning(f"ReferralNotification not found: {pk}")
            raise ValueError("ReferralNotification not found")
        except Exception as e:
            logger.error(f"Error updating referral_notification: {e}")
            raise e
    
    def delete_referral_notification(self, pk) -> None:
        try:
            referral_notification = self.get_referral_notification(pk)
            referral_notification.delete()
            logger.info(f"ReferralNotification deleted: {referral_notification}")
        except ReferralNotification.DoesNotExist:
            logger.warning(f"ReferralNotification not found: {pk}")
            raise ValueError("ReferralNotification not found")
        except Exception as e:
            logger.error(f"Error deleting referral_notification: {e}")
            raise e
        