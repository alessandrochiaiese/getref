User(id, username, first_name, last_name, email, is_staff, is_active, date_joined)

Profile(id, user_id, avatar, bio, birth_date, city, street, postal_code, phone_number, is_business, is_buyer, business_name, is_owner, iva, office_number)

Country(id, name)

Region(id, country_id, name)

Program(id, name, description, program_type, reward_type, reward_value, currency, commission_rate, min_payout_threshold, max_payout_limit, date_created, is_active, duration, allowed_regions, target_industry)

Participant(id, user_id, program_id, status, total_earnings, account_balance, date_joined, last_login, referral_source)

Link(id, participant_id, program_id, url, click_count, conversion_count, date_created, last_used, status, landing_page, custom_tracking_id)

Transaction(id, participant_id, link_id, transaction_amount, transaction_date, order_id, product_id, status, payment_date, commission_rate, discount_applied, coupon_code)

Reward(id, participant_id, program_id, reward_type, reward_value, currency, date_awarded, status, expiry_date, description, source)

Payout(id, participant_id, amount, currency, payout_date, payout_method, status, transaction_id, processing_fee, net_amount, provider)

Performance(id, participant_id, period, total_clicks, total_conversions, conversion_rate, total_earnings, average_order_value, refund_rate, customer_lifetime_value, top_product)

Notification(id, participant_id, message, date_sent, is_read, priority, type, action_required)

Audit(id, participant_id, action_taken, action_date, ip_address, device_info, location)

Order(id, customer_id, created_at, status, total_price)

OrderItem(id, order_id, product_id, quantity)

PaymentMethod(id, amount, description, paid, user_id)

Product(id, name, description, thumbnail, url, price, quantity, created_at, updated_at)

ProductTag(id, name, created_at, updated_at)

Campaign(id, program_id, name, start_date, end_date, goal, budget, spending_to_date, target_audience)

Engagement(id, link_id, participant_id, email_opened, email_clicked, social_share_count, last_interaction_date)

Settings(id, participant_id, preferred_currency, preferred_payment_method, payout_schedule, notification_preference, dashboard_layout, auto_share_setting, social_share_message)

CustmOrder(id, amount, description, buyer_id)

Price(id, product_id, price, created_at, updated_at)

Affiliate(id, user_id, name, email, phone, date_joined, status, total_earnings, country, profile_picture, account_balance, last_login, referral_source)

Commission(id, participant_id, program_id, amount, currency, date_awarded, status, approved_by, type, description, tier)

Tier(id, program_id, tier_name, min_sales, commission_rate, benefits, access_level, next_tier_threshold, expiration_date)

SupportTicket(id, participant_id, ticket_number, subject, description, status, date_created, date_closed, priority, assigned_agent)

ReferralCode(id, participant_id, program_id, code, usage_count, date_created, status, expiry_date, referred_user_count, unique_url, campaign_source, campaign_medium)

Bonus(id, program_id, type, value, min_referrals_required, bonus_date, expiry_date, max_usage, eligibility_criteria)

Conversion(id, link_id, referred_user_id, conversion_date, conversion_value, status, reward_issued, source, type)

Stats(id, link_id, period, click_count, conversion_count, total_rewards, average_conversion_value, highest_referral_earning)

ReferralLevel(id, referrer, referred, level)