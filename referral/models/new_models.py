from django.db import models

class ReferralProgram(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    reward_type = models.CharField(max_length=50)
    reward_value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    min_referral_count = models.IntegerField()
    max_referrals_per_user = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    program_duration = models.IntegerField()  # in days
    allowed_regions = models.CharField(max_length=255)
    target_industry = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Altri dettagli utente (es. password, etc.)

class ReferralCode(models.Model):
    code = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    usage_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    expiry_date = models.DateTimeField()
    referred_user_count = models.IntegerField(default=0)
    unique_url = models.URLField()
    campaign_source = models.CharField(max_length=100)
    campaign_medium = models.CharField(max_length=100)

class ReferralBonus(models.Model):
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    bonus_type = models.CharField(max_length=50)
    bonus_value = models.DecimalField(max_digits=10, decimal_places=2)
    min_referrals_required = models.IntegerField()
    bonus_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    max_usage = models.IntegerField()
    eligibility_criteria = models.TextField()

class ReferralCampaign(models.Model):
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    campaign_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    goal = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    spending_to_date = models.DecimalField(max_digits=10, decimal_places=2)
    target_audience = models.TextField()

class ReferralConversion(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversion_date = models.DateTimeField()
    conversion_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    reward_issued = models.BooleanField(default=False)
    conversion_source = models.CharField(max_length=255)
    referral_type = models.CharField(max_length=50)

class ReferralEngagement(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_opened = models.BooleanField(default=False)
    email_clicked = models.BooleanField(default=False)
    social_share_count = models.IntegerField(default=0)
    last_interaction_date = models.DateTimeField()

class ReferralNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=100)
    priority = models.CharField(max_length=50)
    action_required = models.BooleanField(default=False)

class ReferralProgramParticipation(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    reward_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=50)

class ReferralReward(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward_type = models.CharField(max_length=50)
    reward_value = models.DecimalField(max_digits=10, decimal_places=2)
    date_awarded = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    expiry_date = models.DateTimeField()
    reward_description = models.TextField()
    reward_source = models.CharField(max_length=100)

class ReferralSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_reward_type = models.CharField(max_length=50)
    max_referrals_allowed = models.IntegerField()
    notification_preference = models.CharField(max_length=100)
    auto_share_setting = models.BooleanField(default=False)
    social_share_message = models.TextField()

class ReferralStats(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    period = models.CharField(max_length=100)
    click_count = models.IntegerField(default=0)
    conversion_count = models.IntegerField(default=0)
    total_rewards = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    average_conversion_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    highest_referral_earning = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class ReferralTransaction(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    order_id = models.CharField(max_length=255)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=50)
    conversion_value = models.DecimalField(max_digits=10, decimal_places=2)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_code_used = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=100)

class ReferralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_referrals = models.IntegerField(default=0)
    active_referrals = models.IntegerField(default=0)
    inactive_referrals = models.IntegerField(default=0)
    total_rewards_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_spent_by_referred_users = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loyalty_points_earned = models.IntegerField(default=0)

class Referral(models.Model):
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    referrer = models.ForeignKey(User, related_name="referrer", on_delete=models.CASCADE)
    referred = models.ForeignKey(User, related_name="referred", on_delete=models.CASCADE)
    reward_given = models.DecimalField(max_digits=10, decimal_places=2)
