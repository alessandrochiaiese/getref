# referral_system/services.py

import logging

from typing import List
from django.contrib.auth import get_user_model

from core.models.referral_code import ReferralCode
from referral.models.referral_campaign import ReferralCampaign
from referral.models.referral_program import ReferralProgram
from referral.models.referral_stats import ReferralStats

User = get_user_model()


# Set up a logger
logger = logging.getLogger(__name__)


class ReferralCampaignService():
    def __init__(self) -> None:
        pass
    
    def get_referral_campaigns(self) -> List[ReferralCampaign]:
        try:
            referral_campaigns = ReferralCampaign.objects.all() 
            return referral_campaigns
        except ReferralCampaign.DoesNotExist:
            logger.warning(f"ReferralCampaign not found")
            raise ValueError("ReferralCampaign not found")
     
    def get_referral_campaign(self, pk) -> ReferralCampaign:
        try:
            referral_campaign = ReferralCampaign.objects.get(id=pk)
            return referral_campaign
        except ReferralCampaign.DoesNotExist:
            logger.warning(f"ReferralCampaign not found: {pk}")
            raise ValueError("ReferralCampaign not found")
     
    def create_referral_campaign(self, data) -> ReferralCampaign:
        try:
            # Associa il programma esistente
            program = ReferralProgram.objects.get(id=data['program_id'])

            referral_campaign = ReferralCampaign( 
                campaign_name = data.get('campaign_name'),
                start_date = data.get('start_date'),
                end_date = data.get('end_date'),
                goal = data.get('goal'),
                budget = data.get('budget'),
                spending_to_date = data.get('spending_to_date'),
                target_audience = data.get('target_audience', None))
            referral_campaign.save()

            referral_programs = ReferralProgram.objects.filter(id__in=data['programs'])
            referral_campaign.programs.set(referral_programs)
            
            """referral_codes = ReferralCode.objects.filter(referral_code__programs__contains=referral_campaign.programs)
            
            # 1. Troviamo o creiamo ReferralStats associato al ReferralProgram
            program_statses, created = ReferralStats.objects.filter(referral_codes__contains=referral_codes)

            # 2. Incrementiamo il contatore delle campagne
            for program_stats in program_statses:
                program_stats.total_campaigns += 1
                program_stats.save() """
                
            logger.info(f"ReferralCampaign created: {referral_campaign}")
            return referral_campaign
        except Exception as e:
            logger.error(f"Error creating referral_campaign: {e}")
            raise e
 
    def update_referral_campaign(self, pk, data) -> ReferralCampaign:
        try:
            referral_campaign = self.get_referral_campaign(pk)
            for key, value in data.items():
                setattr(referral_campaign, key, value)
            referral_campaign.save()
            logger.info(f"ReferralCampaign updated: {referral_campaign}")
            return referral_campaign
        except ReferralCampaign.DoesNotExist:
            logger.warning(f"ReferralCampaign not found: {pk}")
            raise ValueError("ReferralCampaign not found")
        except Exception as e:
            logger.error(f"Error updating referral_campaign: {e}")
            raise e
    
    def delete_referral_campaign(self, pk) -> None:
        try:
            referral_campaign = self.get_referral_campaign(pk)
            referral_campaign.delete()
            logger.info(f"ReferralCampaign deleted: {referral_campaign}")
        except ReferralCampaign.DoesNotExist:
            logger.warning(f"ReferralCampaign not found: {pk}")
            raise ValueError("ReferralCampaign not found")
        except Exception as e:
            logger.error(f"Error deleting referral_campaign: {e}")
            raise e
        