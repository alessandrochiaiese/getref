from django.core.management.base import BaseCommand
from referral.models import (
    ReferralBonus, ReferralCampaign, ReferralProgram
)

class Command(BaseCommand):
    help = "Test completo del sistema di referral con tutti i modelli"

    def handle(self, *args, **kwargs):
        print("Creazione del programma di referral...")
        referral_program = ReferralProgram.objects.create(
            name="Programma Referral Premium",
            description="Programma per utenti premium",
            reward_type="Cash",
            reward_value=100.00,
            currency="USD",
            min_referral_count=5,
            max_referrals_per_user=10,
            program_duration=30,  # Durata di 30 giorni
            allowed_regions="IT,US",
            target_industry="E-commerce"
        )

        print("Creazione della campagna di referral...")
        referral_campaign = ReferralCampaign.objects.create(
            referral_program=referral_program,
            campaign_name="Campagna Social Media",
            start_date="2025-03-01",
            end_date="2025-03-31",
            goal="Raggiungere 500 nuove iscrizioni",
            budget=5000.00,
            spending_to_date=1500.00,
            target_audience="Giovani professionisti"
        )
        
        print("Creazione del bonus per Giovanni Verdi...")
        referral_bonus = ReferralBonus.objects.create(
            referral_program=referral_program,
            bonus_type="Cash",
            bonus_value=200.00,
            min_referrals_required=5,
            bonus_date="2025-03-01",
            expiry_date="2025-06-01",
            max_usage=1,
            eligibility_criteria="Completa almeno 5 referral"
        )