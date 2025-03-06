from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name


class ReferralProgram(models.Model):
    REWARD_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Discount', 'Discount'),
        ('Points', 'Points'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    reward_type = models.CharField(max_length=10, choices=REWARD_TYPE_CHOICES)
    reward_value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    min_referral_count = models.IntegerField()
    max_referrals_per_user = models.IntegerField()
    program_duration = models.IntegerField()  # Durata in giorni
    allowed_regions = models.CharField(max_length=255)
    target_industry = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class ReferralCode(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
        ('Used', 'Used'),
    ]
    code = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    unique_url = models.URLField()
    campaign_source = models.CharField(max_length=255)
    campaign_medium = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    expiry_date = models.DateField()
    referred_user_count = models.IntegerField()
    
    def __str__(self):
        return self.code


class ReferralConversion(models.Model):
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    ]
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversion_date = models.DateField()
    conversion_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reward_issued = models.BooleanField(default=False)
    conversion_source = models.CharField(max_length=255)
    referral_type = models.CharField(max_length=255)

    def __str__(self):
        return f"Conversion {self.id}"


class ReferralBonus(models.Model):
    BONUS_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Discount', 'Discount'),
        ('Points', 'Points'),
    ]
    bonus_type = models.CharField(max_length=10, choices=BONUS_TYPE_CHOICES)
    bonus_value = models.DecimalField(max_digits=10, decimal_places=2)
    min_referrals_required = models.IntegerField()
    bonus_date = models.DateField()
    expiry_date = models.DateField()
    max_usage = models.IntegerField()
    eligibility_criteria = models.CharField(max_length=255)

    def __str__(self):
        return f"Bonus {self.id}"


class ReferralNotification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('Bonus', 'Bonus'),
        ('Alert', 'Alert'),
        ('Reminder', 'Reminder'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateField()
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPE_CHOICES)
    priority = models.CharField(max_length=10)
    action_required = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.user.name}"


class ReferralReward(models.Model):
    REWARD_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Discount', 'Discount'),
        ('Points', 'Points'),
    ]
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward_type = models.CharField(max_length=10, choices=REWARD_TYPE_CHOICES)
    reward_value = models.DecimalField(max_digits=10, decimal_places=2)
    date_awarded = models.DateField()
    status = models.CharField(max_length=10)
    expiry_date = models.DateField()
    reward_description = models.TextField()
    reward_source = models.CharField(max_length=255)

    def __str__(self):
        return f"Reward for {self.referred_user.name}"


class ReferralProgramParticipation(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    date_joined = models.DateField()
    reward_earned = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"Participation {self.id}"


class ReferralStats(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    period = models.CharField(max_length=10)
    click_count = models.IntegerField()
    conversion_count = models.IntegerField()
    total_rewards = models.DecimalField(max_digits=10, decimal_places=2)
    average_conversion_value = models.DecimalField(max_digits=10, decimal_places=2)
    highest_referral_earning = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Stats for {self.referral_code.code} in {self.period}"


class ReferralTransaction(models.Model):
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    order_id = models.CharField(max_length=255)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    conversion_value = models.DecimalField(max_digits=10, decimal_places=2)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_code_used = models.CharField(max_length=255)
    channel = models.CharField(max_length=255)

    def __str__(self):
        return f"Transaction {self.order_id}"


class ReferralUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_referrals = models.IntegerField()
    active_referrals = models.IntegerField()
    inactive_referrals = models.IntegerField()
    total_rewards_earned = models.DecimalField(max_digits=10, decimal_places=2)
    total_spent_by_referred_users = models.DecimalField(max_digits=10, decimal_places=2)
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    loyalty_points_earned = models.IntegerField()

    def __str__(self):
        return f"Referral User {self.user.name}"


class Referral(models.Model):
    referral_program = models.ForeignKey(ReferralProgram, on_delete=models.CASCADE)
    referrer = models.ForeignKey(User, related_name='referrer', on_delete=models.CASCADE)
    referred = models.ForeignKey(User, related_name='referred', on_delete=models.CASCADE)
    reward_given = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Referral {self.id}"
