AffiliateAudit(referral_codes [AffiliateCode], action_taken, action_date, user [User], ip_address, device_info, location)
 
AffiliateCampaign(programs [AffiliateProgram], campaign_name, start_date, end_date, goal, budget, spending_to_date, target_audience)

AffiliateCommission(affiliates [Affiliate], programs [AffiliateProgram], amount, currency, date_awarded, status, approved_by, commission_type, description, tier) 

AffiliateIncentive(affiliate, program, incentive_type, date, amount, currency, status, description, ip_address, device_info, tracking_id, expiration_date is_incentive_active)

AffiliateLink(affiliates [Affiliate], programs [AffiliateProgram], url, click_count, conversion_count, date_created, last_used, link_status, landing_page, custom_tracking_id)

AffiliateNotification(user [User], message, date_sent, is_read, notification_type, priority, action_required)

AffiliatePayout(affiliates [Affiliate], amount, currency, payout_date, payout_method, payout_status, transaction_id, processing_fee, net_amount, payout_provider)

AffiliateProgramPartecipation(referral_codes, programs, date_joined, reward_earned, status)

AffiliateProgram(name, description, reward_type, reward_value, currency, min_referral_count, max_referrals_per_user, date_created, is_active, program_duration, allowed_regions, target_industry)

AffiliateReward(referral_codes [AffiliateCode], referred_user [User], reward_type, reward_value, date_awarded, status, expiry_date, reward_description, reward_source)

AffiliateSettings(user [User], default_reward_type, max_referrals_allowed, notification_preference, auto_share_setting, social_share_message)

AffiliateSupportTicket(affiliates [Affiliate], ticket_number, subject, description, status, date_created, date_closed, priority, assigned_agent)

AffiliateTier(programs [AffiliateProgram], tier_name, min_sales, commission_rate, tier_benefits, access_level, next_tier_threshold, tier_expiration)

AffiliateTransaction(referral_codes [AffiliateCode], referred_user [User], transaction_date, order_id, transaction_amount, currency, status, conversion_value, discount_value, coupon_code_used, channel)


ReferralAudit(referral_codes [ReferralCode], action_taken, action_date, user [User], ip_address, device_info, location)

ReferralBonus(programs [ReferralProgram], bonus_type, bonus_value, min_referrals_required, bonus_date, expiry_date, max_usage, eligibility_criteria)

ReferralCampaign(programs [ReferralProgram], campaign_name, start_date, end_date, goal, budget, spending_to_date, target_audience)

ReferralCode(user [User], programs [ReferralProgram], code, usage_count, date_created, status, expiry_date, referred_user_count, unique_url, campaign_source, campaign_medium)

ReferralConversion(referral_codes [ReferralCode], referred_user [User], conversion_date, conversion_value, status, reward_issued, conversion_source, referral_type)

ReferralEngagement(referral_codes [ReferralCode], user [User], email_opened, email_clicked, social_share_count, last_interaction_date)

ReferralNotification(user [User], message, date_sent, is_read, notification_type, priority, action_required)

ReferralProgramPartecipation(referral_codes, programs, date_joined, reward_earned, status)

ReferralProgram(name, description, reward_type, reward_value, currency, min_referral_count, max_referrals_per_user, date_created, is_active, program_duration, allowed_regions, target_industry)

ReferralReward(referral_codes [ReferralCode], referred_user [User], reward_type, reward_value, date_awarded, status, expiry_date, reward_description, reward_source)

ReferralSettings(user [User], default_reward_type, max_referrals_allowed, notification_preference, auto_share_setting, social_share_message)

ReferralStats(referral_codes [ReferralCode], period, click_count, conversion_count, total_rewards, average_conversion_value, highest_referral_earning)

ReferralTransaction(referral_codes [ReferralCode], referred_user [User], transaction_date, order_id, transaction_amount, currency, status, conversion_value, discount_value, coupon_code_used, channel)

ReferralUser(user [User], total_referrals, active_referrals, inactive_referrals, total_rewards_earned, total_spent_by_referred_users, average_order_value, loyalty_points_earned)

Referral(program, referrer, referred, reward_given)
 
Questo qui è lo schema del mio sistema di affiliazione e sistema di codici referenziati.

vorrei per ognuna di queste entità, il body POST per postman
ChatGPT said:
Ecco i vari body POST per Postman per ciascuna delle entità nel tuo schema. Ogni esempio utilizza il formato JSON per le richieste POST:

1. AffiliateAudit
json
Copy
{
  "referral_codes": ["code1", "code2"],
  "action_taken": "Signup",
  "action_date": "2025-02-13T12:00:00Z",
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "ip_address": "192.168.1.1",
  "device_info": "iPhone 13",
  "location": "New York, USA"
}
2. AffiliateCampaign
json
Copy
{
  "programs": ["Program1", "Program2"],
  "campaign_name": "Spring Sale",
  "start_date": "2025-03-01T00:00:00Z",
  "end_date": "2025-06-01T00:00:00Z",
  "goal": "Increase signups",
  "budget": 5000,
  "spending_to_date": 1200,
  "target_audience": "Young professionals"
}
3. AffiliateCommission
json
Copy
{
  "affiliates": ["Affiliate1", "Affiliate2"],
  "programs": ["Program1", "Program2"],
  "amount": 100,
  "currency": "USD",
  "date_awarded": "2025-02-13T12:00:00Z",
  "status": "Approved",
  "approved_by": "Admin",
  "commission_type": "Fixed",
  "description": "Commission for sale",
  "tier": "Silver"
}
4. AffiliateIncentive
json
Copy
{
  "affiliate": "Affiliate1",
  "program": "Program1",
  "incentive_type": "Bonus",
  "date": "2025-02-13T12:00:00Z",
  "amount": 50,
  "currency": "USD",
  "status": "Active",
  "description": "Incentive for achieving target",
  "ip_address": "192.168.1.1",
  "device_info": "Android",
  "tracking_id": "XYZ123",
  "expiration_date": "2025-03-01T00:00:00Z",
  "is_incentive_active": true
}
5. AffiliateLink
json
Copy
{
  "affiliates": ["Affiliate1"],
  "programs": ["Program1"],
  "url": "https://example.com/affiliate-link",
  "click_count": 100,
  "conversion_count": 50,
  "date_created": "2025-02-13T12:00:00Z",
  "last_used": "2025-02-12T12:00:00Z",
  "link_status": "Active",
  "landing_page": "https://example.com/landing-page",
  "custom_tracking_id": "Link123"
}
6. AffiliateNotification
json
Copy
{
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "message": "You have a new commission payout!",
  "date_sent": "2025-02-13T12:00:00Z",
  "is_read": false,
  "notification_type": "Payout",
  "priority": "High",
  "action_required": false
}
7. AffiliatePayout
json
Copy
{
  "affiliates": ["Affiliate1"],
  "amount": 150,
  "currency": "USD",
  "payout_date": "2025-02-15T12:00:00Z",
  "payout_method": "PayPal",
  "payout_status": "Pending",
  "transaction_id": "TX12345",
  "processing_fee": 5,
  "net_amount": 145,
  "payout_provider": "PayPal"
}
8. AffiliateProgramPartecipation
json
Copy
{
  "referral_codes": ["code1"],
  "programs": ["Program1"],
  "date_joined": "2025-02-13T12:00:00Z",
  "reward_earned": 50,
  "status": "Active"
}
9. AffiliateProgram
json
Copy
{
  "name": "Spring Sale",
  "description": "Earn commission on product sales",
  "reward_type": "Percentage",
  "reward_value": 10,
  "currency": "USD",
  "min_referral_count": 5,
  "max_referrals_per_user": 10,
  "date_created": "2025-02-01T00:00:00Z",
  "is_active": true,
  "program_duration": "3 months",
  "allowed_regions": ["USA", "Canada"],
  "target_industry": "E-commerce"
}
10. AffiliateReward
json
Copy
{
  "referral_codes": ["code1"],
  "referred_user": {
    "user_id": "54321",
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  },
  "reward_type": "Cash",
  "reward_value": 20,
  "date_awarded": "2025-02-13T12:00:00Z",
  "status": "Active",
  "expiry_date": "2025-03-01T00:00:00Z",
  "reward_description": "Referral reward for successful signup",
  "reward_source": "Spring Sale Program"
}
11. AffiliateSettings
json
Copy
{
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "default_reward_type": "Cash",
  "max_referrals_allowed": 10,
  "notification_preference": "Email",
  "auto_share_setting": true,
  "social_share_message": "Join our referral program and earn rewards!"
}
12. AffiliateSupportTicket
json
Copy
{
  "affiliates": ["Affiliate1"],
  "ticket_number": "TICKET12345",
  "subject": "Issue with Payout",
  "description": "I haven't received my payout yet",
  "status": "Open",
  "date_created": "2025-02-13T12:00:00Z",
  "date_closed": null,
  "priority": "High",
  "assigned_agent": "Support Agent 1"
}
13. AffiliateTier
json
Copy
{
  "programs": ["Program1"],
  "tier_name": "Gold",
  "min_sales": 1000,
  "commission_rate": 15,
  "tier_benefits": "Priority support, higher commission",
  "access_level": "High",
  "next_tier_threshold": 2000,
  "tier_expiration": "2025-12-31T23:59:59Z"
}
14. AffiliateTransaction
json
Copy
{
  "referral_codes": ["code1"],
  "referred_user": {
    "user_id": "54321",
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  },
  "transaction_date": "2025-02-13T12:00:00Z",
  "order_id": "ORD12345",
  "transaction_amount": 200,
  "currency": "USD",
  "status": "Completed",
  "conversion_value": 50,
  "discount_value": 10,
  "coupon_code_used": "SPRING10",
  "channel": "Mobile App"
}
15. ReferralAudit
json
Copy
{
  "referral_codes": ["code1"],
  "action_taken": "Referral",
  "action_date": "2025-02-13T12:00:00Z",
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "ip_address": "192.168.1.1",
  "device_info": "Samsung Galaxy S21",
  "location": "San Francisco, USA"
}
16. ReferralBonus
json
Copy
{
  "programs": ["ReferralProgram1"],
  "bonus_type": "Fixed",
  "bonus_value": 50,
  "min_referrals_required": 5,
  "bonus_date": "2025-02-13T12:00:00Z",
  "expiry_date": "2025-03-01T00:00:00Z",
  "max_usage": 10,
  "eligibility_criteria": "User must refer at least 5 people"
}
17. ReferralCampaign
json
Copy
{
  "programs": ["ReferralProgram1"],
  "campaign_name": "Summer Referral Campaign",
  "start_date": "2025-05-01T00:00:00Z",
  "end_date": "2025-08-01T00:00:00Z",
  "goal": "Increase signups",
  "budget": 3000,
  "spending_to_date": 500,
  "target_audience": "College students"
}
18. ReferralCode
json
Copy
{
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "programs": ["ReferralProgram1"],
  "code": "REF12345",
  "usage_count": 10,
  "date_created": "2025-02-01T00:00:00Z",
  "status": "Active",
  "expiry_date": "2025-12-31T23:59:59Z",
  "referred_user_count": 5,
  "unique_url": "https://example.com/referral/REF12345",
  "campaign_source": "Email",
  "campaign_medium": "Social Media"
}
19. ReferralConversion
json
Copy
{
  "referral_codes": ["REF12345"],
  "referred_user": {
    "user_id": "54321",
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  },
  "conversion_date": "2025-02-13T12:00:00Z",
  "conversion_value": 100,
  "status": "Completed",
  "reward_issued": 20,
  "conversion_source": "Mobile App",
  "referral_type": "Direct"
}
20. ReferralEngagement
json
Copy
{
  "referral_codes": ["REF12345"],
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "email_opened": 3,
  "email_clicked": 1,
  "social_share_count": 5,
  "last_interaction_date": "2025-02-12T12:00:00Z"
}
21. ReferralNotification
json
Copy
{
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "message": "You earned a referral reward!",
  "date_sent": "2025-02-13T12:00:00Z",
  "is_read": false,
  "notification_type": "Referral",
  "priority": "Medium",
  "action_required": true
}
22. ReferralProgramPartecipation
json
Copy
{
  "referral_codes": ["REF12345"],
  "programs": ["ReferralProgram1"],
  "date_joined": "2025-02-01T00:00:00Z",
  "reward_earned": 50,
  "status": "Active"
}
23. ReferralProgram
json
Copy
{
  "name": "Summer Referral Program",
  "description": "Earn rewards by referring others",
  "reward_type": "Percentage",
  "reward_value": 10,
  "currency": "USD",
  "min_referral_count": 3,
  "max_referrals_per_user": 10,
  "date_created": "2025-01-01T00:00:00Z",
  "is_active": true,
  "program_duration": "6 months",
  "allowed_regions": ["USA", "UK"],
  "target_industry": "Retail"
}
24. ReferralReward
json
Copy
{
  "referral_codes": ["REF12345"],
  "referred_user": {
    "user_id": "54321",
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  },
  "reward_type": "Cash",
  "reward_value": 20,
  "date_awarded": "2025-02-13T12:00:00Z",
  "status": "Active",
  "expiry_date": "2025-03-01T00:00:00Z",
  "reward_description": "Referral reward for successful referral",
  "reward_source": "Summer Referral Program"
}
25. ReferralSettings
json
Copy
{
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "default_reward_type": "Cash",
  "max_referrals_allowed": 15,
  "notification_preference": "SMS",
  "auto_share_setting": true,
  "social_share_message": "Earn rewards by referring others to join!"
}
26. ReferralStats
json
Copy
{
  "referral_codes": ["REF12345"],
  "period": "2025-01-01 to 2025-02-01",
  "click_count": 100,
  "conversion_count": 30,
  "total_rewards": 300,
  "average_conversion_value": 10,
  "highest_referral_earning": 50
}
27. ReferralTransaction
json
Copy
{
  "referral_codes": ["REF12345"],
  "referred_user": {
    "user_id": "54321",
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  },
  "transaction_date": "2025-02-13T12:00:00Z",
  "order_id": "ORD54321",
  "transaction_amount": 150,
  "currency": "USD",
  "status": "Completed",
  "conversion_value": 20,
  "discount_value": 10,
  "coupon_code_used": "SUMMER10",
  "channel": "Website"
}
28. ReferralUser
json
Copy
{
  "user": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "total_referrals": 10,
  "active_referrals": 8,
  "inactive_referrals": 2,
  "total_rewards_earned": 200,
  "total_spent_by_referred_users": 5000,
  "average_order_value": 100,
  "loyalty_points_earned": 50
}
29. Referral
json
Copy
{
  "program": "ReferralProgram1",
  "referrer": {
    "user_id": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "referred": {
    "user_id": "54321",
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  },
  "reward_given": 20
}
Questi sono i body POST per ciascuna delle entità, che puoi usare in Postman per testare le tue API!