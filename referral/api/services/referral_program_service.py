# referral_system/services.py
 
import datetime
import logging

from typing import List
from dashboard.models.region import Region
from getref.settings import DOMAIN
from referral.models import *
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string 

User = get_user_model()

# Set up a logger
logger = logging.getLogger(__name__)


class ReferralProgramService():
    def __init__(self) -> None:
        pass
    
    def get_referral_programs(self) -> List[ReferralProgram]:
        try:
            referral_programs = ReferralProgram.objects.all() 
            return referral_programs
        except ReferralProgram.DoesNotExist:
            logger.warning(f"ReferralProgram not found")
            raise ValueError("ReferralProgram not found")
     
    def get_referral_program(self, pk) -> ReferralProgram:
        try:
            referral_program = ReferralProgram.objects.get(id=pk)
            return referral_program
        except ReferralProgram.DoesNotExist:
            logger.warning(f"ReferralProgram not found: {pk}")
            raise ValueError("ReferralProgram not found")
     
    def create_referral_program(self, data, user) -> ReferralProgram:
        try:
            referral_program = ReferralProgram( 
                name = data.get('name'),
                description = data.get('description'),
                reward_type = data.get('reward_type'),
                reward_value = data.get('reward_value'),
                currency = data.get('currency'),
                min_referral_count = data.get('min_referral_count'),
                max_referrals_per_user = data.get('max_referrals_per_user'),
                date_created = datetime.datetime.now(),#data.get('date_created'),
                is_active = True,
                program_duration = data.get('program_duration'), 
                target_industry = data.get('target_industry'))
            referral_program.save()
                
            # Creazione ReferralCode per l'utente creatore 
            referral_code, created = ReferralCode.objects.get_or_create(user=user)
            if created:
                code = get_random_string(length=8).upper()
                referral_code.status="active"
                referral_code.expiry_date=datetime.datetime.today() - datetime.timedelta(days=30)
                referral_code.unique_url=f'{DOMAIN}/c/?code={code}'
            referral_code.programs.add(referral_program)

            # Creazione Stats iniziali
            referraul_stats = ReferralStats.objects.create( 
                period="daily",  # Esempio: può essere settimanale o mensile
                click_count=0,
                conversion_count=0,
                total_rewards=0,
                average_conversion_value=0,
                highest_referral_earning=0
            )
            referraul_stats.referral_codes.add(referral_code)

            # Creazione o aggiornamento ReferralUser
            referral_user, created = ReferralUser.objects.get_or_create(user=user)
            referral_user.total_referrals += 1 if created else 0
            referral_user.total_rewards_earned = 0.00
            referral_user.total_spent_by_referred_users = 0.00
            referral_user.average_order_value = 0.00
            referral_user.save()

            logger.info(f"ReferralProgram created: {referral_program}")
            return referral_program
        except Exception as e:
            logger.error(f"Error creating referral_program: {e}")
            raise e
 
    def update_referral_program(self, pk, data) -> ReferralProgram:
        try:
            referral_program = self.get_referral_program(pk)
            for key, value in data.items():
                setattr(referral_program, key, value)
            referral_program.save()
            logger.info(f"ReferralProgram updated: {referral_program}")
            return referral_program
        except ReferralProgram.DoesNotExist:
            logger.warning(f"ReferralProgram not found: {pk}")
            raise ValueError("ReferralProgram not found")
        except Exception as e:
            logger.error(f"Error updating referral_program: {e}")
            raise e
    
    def delete_referral_program(self, pk) -> None:
        try:
            referral_program = self.get_referral_program(pk)
            referral_program.delete()
            logger.info(f"ReferralProgram deleted: {referral_program}")
        except ReferralProgram.DoesNotExist:
            logger.warning(f"ReferralProgram not found: {pk}")
            raise ValueError("ReferralProgram not found")
        except Exception as e:
            logger.error(f"Error deleting referral_program: {e}")
            raise e
        