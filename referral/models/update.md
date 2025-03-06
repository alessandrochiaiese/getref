1. ReferralAudit
Tieni traccia delle azioni intraprese su un codice referral (monitoraggio delle modifiche).

plaintext
Copy
ReferralAudit
- id (PK)
- referral_code_id (FK → ReferralCode)
- action_taken
- action_date
- user_id (FK → User)
- ip_address
- device_info
- location
Relazioni:

ReferralCode (uno) → ReferralAudit (molti)
User (uno) → ReferralAudit (molti)
2. ReferralBonus
Definisci i bonus legati ai programmi di referral.

plaintext
Copy
ReferralBonus
- id (PK)
- referral_program_id (FK → ReferralProgram)
- bonus_type
- bonus_value
- min_referrals_required
- bonus_date
- expiry_date
- max_usage
- eligibility_criteria
Relazioni:

ReferralProgram (uno) → ReferralBonus (molti)
3. ReferralCampaign
Gestisci le campagne di referral legate a un programma.

plaintext
Copy
ReferralCampaign
- id (PK)
- referral_program_id (FK → ReferralProgram)
- campaign_name
- start_date
- end_date
- goal
- budget
- spending_to_date
- target_audience
Relazioni:

ReferralProgram (uno) → ReferralCampaign (molti)
4. ReferralCode
Tieni traccia dei codici referral generati.

plaintext
Copy
ReferralCode
- id (PK)
- user_id (FK → User)
- referral_program_id (FK → ReferralProgram)
- code
- usage_count
- date_created
- status
- expiry_date
- referred_user_count
- unique_url
- campaign_source
- campaign_medium
Relazioni:

User (uno) → ReferralCode (molti)
ReferralProgram (uno) → ReferralCode (molti)
ReferralConversion (uno) → ReferralCode (molti)
ReferralEngagement (uno) → ReferralCode (molti)
ReferralStats (uno) → ReferralCode (molti)
5. ReferralConversion
Traccia la conversione dei riferimenti (acquisti, azioni completate).

plaintext
Copy
ReferralConversion
- id (PK)
- referral_code_id (FK → ReferralCode)
- referred_user_id (FK → User)
- conversion_date
- conversion_value
- status
- reward_issued
- conversion_source
- referral_type
Relazioni:

ReferralCode (uno) → ReferralConversion (molti)
User (uno) → ReferralConversion (molti)
6. ReferralEngagement
Tieni traccia delle interazioni con i codici referral, come email e social media.

plaintext
Copy
ReferralEngagement
- id (PK)
- referral_code_id (FK → ReferralCode)
- user_id (FK → User)
- email_opened
- email_clicked
- social_share_count
- last_interaction_date
Relazioni:

ReferralCode (uno) → ReferralEngagement (molti)
User (uno) → ReferralEngagement (molti)
7. ReferralNotification
Gestisci le notifiche per gli utenti.

plaintext
Copy
ReferralNotification
- id (PK)
- user_id (FK → User)
- message
- date_sent
- is_read
- notification_type
- priority
- action_required
Relazioni:

User (uno) → ReferralNotification (molti)
8. ReferralProgramPartecipation
Registra la partecipazione degli utenti ai programmi di referral.

plaintext
Copy
ReferralProgramPartecipation
- id (PK)
- referral_code_id (FK → ReferralCode)
- referral_program_id (FK → ReferralProgram)
- date_joined
- reward_earned
- status
Relazioni:

ReferralCode (uno) → ReferralProgramPartecipation (molti)
ReferralProgram (uno) → ReferralProgramPartecipation (molti)
9. ReferralProgram
Definisci il programma di referral, con i relativi dettagli.

plaintext
Copy
ReferralProgram
- id (PK)
- name
- description
- reward_type
- reward_value
- currency
- min_referral_count
- max_referrals_per_user
- date_created
- is_active
- program_duration
- allowed_regions
- target_industry
Relazioni:

ReferralBonus (uno) → ReferralProgram (molti)
ReferralCode (uno) → ReferralProgram (molti)
ReferralCampaign (uno) → ReferralProgram (molti)
ReferralProgramPartecipation (uno) → ReferralProgram (molti)
10. ReferralReward
Registra i premi ottenuti dai referiti.

plaintext
Copy
ReferralReward
- id (PK)
- referral_code_id (FK → ReferralCode)
- referred_user_id (FK → User)
- reward_type
- reward_value
- date_awarded
- status
- expiry_date
- reward_description
- reward_source
Relazioni:

ReferralCode (uno) → ReferralReward (molti)
User (uno) → ReferralReward (molti)
11. ReferralSettings
Gestisci le impostazioni di referral per ciascun utente.

plaintext
Copy
ReferralSettings
- id (PK)
- user_id (FK → User)
- default_reward_type
- max_referrals_allowed
- notification_preference
- auto_share_setting
- social_share_message
Relazioni:

User (uno) → ReferralSettings (uno)
12. ReferralStats
Monitoraggio delle statistiche dei codici referral.

plaintext
Copy
ReferralStats
- id (PK)
- referral_code_id (FK → ReferralCode)
- period
- click_count
- conversion_count
- total_rewards
- average_conversion_value
- highest_referral_earning
Relazioni:

ReferralCode (uno) → ReferralStats (molti)
13. ReferralTransaction
Registra le transazioni associate ai codici referral.

plaintext
Copy
ReferralTransaction
- id (PK)
- referral_code_id (FK → ReferralCode)
- referred_user_id (FK → User)
- transaction_date
- order_id
- transaction_amount
- currency
- status
- conversion_value
- discount_value
- coupon_code_used
- channel
Relazioni:

ReferralCode (uno) → ReferralTransaction (molti)
User (uno) → ReferralTransaction (molti)
14. ReferralUser
Gestisci i dettagli di ogni utente nel programma di referral.

plaintext
Copy
ReferralUser
- id (PK)
- user_id (FK → User)
- total_referrals
- active_referrals
- inactive_referrals
- total_rewards_earned
- total_spent_by_referred_users
- average_order_value
- loyalty_points_earned
Relazioni:

User (uno) → ReferralUser (uno)
15. Referral
Registra la relazione tra il programma, l'utente che ha effettuato il referral e il referito.

plaintext
Copy
Referral
- id (PK)
- referral_program_id (FK → ReferralProgram)
- referrer_id (FK → User)
- referred_id (FK → User)
- reward_given
Relazioni:

ReferralProgram (uno) → Referral (molti)
User (uno) → Referral (molti)
Riepilogo delle relazioni principali:
Uno a molti:
Un programma di referral può avere molteplici codici referral, campagne, e bonus.
Un codice referral può avere molte conversioni, transazioni, engagement, premi e statistiche.
Un utente può avere molte notifiche, interazioni e partecipazioni ai programmi di referral.
Uno a uno:
Ogni utente ha una configurazione di referral unica (ReferralSettings).
Ogni utente ha una voce unica nel sistema di gestione dei referral (ReferralUser).
Questa versione aggiornata tiene conto delle relazioni tra le entità e assicura che il sistema sia ben normalizzato, riducendo al minimo la possibilità di dati incoerenti o duplicati.