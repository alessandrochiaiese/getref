from django.core.management.base import BaseCommand
from referral.models import (
    User, ReferralProgram, ReferralCode, ReferralBonus, ReferralCampaign,
    ReferralConversion, ReferralEngagement, ReferralNotification, ReferralProgramPartecipation,
    ReferralReward, ReferralSettings, ReferralStats, ReferralTransaction, ReferralUser, Referral
)

class Command(BaseCommand):
    help = "Test completo del sistema di referral con tutti i modelli"

    def handle(self, *args, **kwargs):
        # 1. Creazione del programma di referral
        print("Creazione del programma di referral...")
        referral_program = ReferralProgram.objects.create(
            name="Programma Referral Premium",
            description="Programma per utenti premium",
            reward_type="Cash",
            reward_value=100.00,
            currency="EUR",
            min_referral_count=5,
            max_referrals_per_user=10,
            program_duration=365*10,  # Durata di 30 giorni
            allowed_regions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            target_industry="Getref"
        )

        # 2. Creazione di un utente che diventa referrer
        print("Creazione del primo utente (referrer)...")
        user1 = User.objects.create(name="Giovanni Verdi", email="giovanni@esempio.com")

        # 3. Creazione di un codice referral per Giovanni
        print("Generazione del codice referral per Giovanni Verdi...")
        referral_code = ReferralCode.objects.create(
            code="GIOVANNI123",
            user=user1,
            referral_program=referral_program,
            unique_url="http://example.com/referral/GIOVANNI123",
            campaign_source="social_media",
            campaign_medium="facebook",
            status="Active",
            expiry_date="2025-01-01",
            referred_user_count=0
        )

        # 4. Creazione di una campagna di referral
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

        # 5. Creazione di un secondo utente che si iscrive tramite il codice referral
        print("Creazione di un secondo utente (referred user)...")
        user2 = User.objects.create(name="Lucia Rossi", email="lucia@esempio.com")
        referral_conversion = ReferralConversion.objects.create(
            referral_code=referral_code,
            referred_user=user2,
            conversion_date="2025-03-01",
            conversion_value=100.00,
            status="Completed",
            reward_issued=False,
            conversion_source="website",
            referral_type="Standard"
        )

        # 6. Creazione dell'interazione del referral (engagement)
        print("Registrazione dell'interazione del referral...")
        referral_engagement = ReferralEngagement.objects.create(
            referral_code=referral_code,
            user=user2,
            email_opened=True,
            email_clicked=True,
            social_share_count=3,
            last_interaction_date="2025-03-01"
        )

        # 7. Assegnazione del premio al referred user (Lucia)
        print("Premio assegnato a Lucia Rossi...")
        referral_reward = ReferralReward.objects.create(
            referral_code=referral_code,
            referred_user=user2,
            reward_type="Cash",
            reward_value=50.00,
            date_awarded="2025-03-01",
            status="Awarded",
            expiry_date="2025-04-01",
            reward_description="Premio per aver completato la registrazione",
            reward_source="ReferralProgram"
        )

        # 8. Creazione di un bonus per il referrer (Giovanni)
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

        # 9. Registrazione della partecipazione di Giovanni nel programma
        print("Registrazione della partecipazione di Giovanni al programma...")
        referral_program_participation = ReferralProgramPartecipation.objects.create(
            referral_code=referral_code,
            referral_program=referral_program,
            date_joined="2025-03-01",
            reward_earned=50.00,
            status="Active"
        )

        # 10. Creazione delle statistiche di referral
        print("Generazione delle statistiche di referral...")
        referral_stats = ReferralStats.objects.create(
            referral_code=referral_code,
            period="2025-03",
            click_count=20,
            conversion_count=10,
            total_rewards=500.00,
            average_conversion_value=50.00,
            highest_referral_earning=100.00
        )

        # 11. Creazione di una transazione di referral (quando l'utente referenziato effettua un acquisto)
        print("Creazione di una transazione di referral...")
        referral_transaction = ReferralTransaction.objects.create(
            referral_code=referral_code,
            referred_user=user2,
            transaction_date="2025-03-02",
            order_id="ORD123456",
            transaction_amount=200.00,
            currency="USD",
            status="Completed",
            conversion_value=100.00,
            discount_value=20.00,
            coupon_code_used="DISCOUNT2025",
            channel="Website"
        )

        # 12. Creazione dell'utente ReferralUser
        print("Creazione dell'utente ReferralUser...")
        referral_user = ReferralUser.objects.create(
            user=user1,
            total_referrals=5,
            active_referrals=3,
            inactive_referrals=2,
            total_rewards_earned=500.00,
            total_spent_by_referred_users=2000.00,
            average_order_value=100.00,
            loyalty_points_earned=300
        )

        # 13. Creazione di una notifica per il referrer (Giovanni)
        print("Creazione di una notifica per Giovanni Verdi...")
        referral_notification = ReferralNotification.objects.create(
            user=user1,
            message="Hai ricevuto un nuovo referral bonus!",
            date_sent="2025-03-01",
            is_read=False,
            notification_type="Bonus",
            priority="High",
            action_required=True
        )

        # 14. Creazione delle impostazioni di referral per l'utente
        print("Creazione delle impostazioni di referral per Giovanni...")
        referral_settings = ReferralSettings.objects.create(
            user=user1,
            default_reward_type="Cash",
            max_referrals_allowed=10,
            notification_preference="Email",
            auto_share_setting=True,
            social_share_message="Unisciti al programma di referral!"
        )

        # 15. Creazione del referral (associando un referrer e un referred)
        print("Creazione del referral completo...")
        referral = Referral.objects.create(
            referral_program=referral_program,
            referrer=user1,
            referred=user2,
            reward_given=50.00
        )

        print("Test del sistema di referral completato con successo!")
