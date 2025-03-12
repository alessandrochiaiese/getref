from django import forms
from .models import *

# referral models 
class ReferralAuditForm(forms.ModelForm):
    class Meta:
        model = ReferralAudit
        fields = ['id', 'referral_code', 'action_taken', 'user', 'ip_address', 'device_info', 'location'] # '__all__' #

class ReferralBonusForm(forms.ModelForm):
    class Meta:
        model = ReferralBonus
        fields = ['id', 'program', 'bonus_type', 'bonus_value', 'min_referrals_required', 'expiry_date', 'max_usage', 'eligibility_criteria'] # '__all__' #

class ReferralCampaignForm(forms.ModelForm):
    class Meta:
        model = ReferralCampaign
        fields = ['id', 'program', 'campaign_name', 'start_date', 'end_date', 'goal', 'budget', 'spending_to_date', 'target_audience'] # '__all__' #

class ReferralCodeForm(forms.ModelForm):
    class Meta:
        model = ReferralCode
        fields = ['id', 'user', 'program', 'code', 'usage_count', 'status', 'expiry_date', 'referred_user_count', 'unique_url', 'campaign_source', 'campaign_medium'] # '__all__' #

class ReferralCommissionForm(forms.ModelForm):
    class Meta:
        model = ReferralCommission
        fields = ['id', 'referral_code', 'referred_user', 'commission_value', 'status', 'trigger_event', 'transaction', 'commission_percentage', 'expiry_date']# '__all__' #

class ReferralConversionForm(forms.ModelForm):
    class Meta:
        model = ReferralConversion
        fields = ['id', 'referral_code', 'referred_user', 'conversion_value', 'status', 'reward_issued', 'conversion_source', 'referral_type'] # '__all__' #

class ReferralEngagementForm(forms.ModelForm):
    class Meta:
        model = ReferralEngagement
        fields = ['id', 'referral_code', 'user', 'email_opened', 'email_clicked', 'social_share_count'] # '__all__' #

class ReferralNotificationForm(forms.ModelForm):
    class Meta:
        model = ReferralNotification
        fields = ['id', 'user', 'message', 'is_read', 'notification_type', 'priority', 'action_required'] # '__all__' #

class ReferralProgramForm(forms.ModelForm):
    class Meta:
        model = ReferralProgram
        fields = ['id', 'name', 'description', 'reward_type', 'reward_value', 'currency', 'min_referral_count', 'max_referrals_per_user', 'is_active', 'program_duration', 'allowed_regions', 'target_industry'] # '__all__' #

class ReferralProgramPartecipationForm(forms.ModelForm):
    class Meta:
        model = ReferralProgramPartecipation
        fields = ['id', 'referral_code', 'program', 'reward_earned', 'status'] # '__all__' #

class ReferralRewardForm(forms.ModelForm):
    class Meta:
        model = ReferralReward
        fields = ['id', 'referral_code', 'user', 'reward_type', 'reward_value', 'status', 'expiry_date', 'reward_description', 'reward_source'] # '__all__' #

class ReferralSettingsForm(forms.ModelForm):
    class Meta:
        model = ReferralSettings
        fields = ['id', 'user', 'default_reward_type', 'max_referrals_allowed', 'notification_preference', 'auto_share_setting', 'social_share_message'] # '__all__' #

class ReferralStatsForm(forms.ModelForm):
    class Meta:
        model = ReferralStats
        fields = ['id', 'referral_code', 'period', 'click_count', 'conversion_count', 'total_rewards', 'average_conversion_value', 'highest_referral_earning'] # '__all__' #

class ReferralTransactionForm(forms.ModelForm):
    class Meta:
        model = ReferralTransaction
        fields = ['id', 'referral_code', 'referred_user', 'order', 'transaction_amount', 'currency', 'status', 'conversion_value', 'discount_value', 'coupon_code_used', 'channel'] # '__all__' #

class ReferralUserForm(forms.ModelForm):
    class Meta:
        model = ReferralUser
        fields = ['id', 'user', 'total_referrals', 'active_referrals', 'inactive_referrals', 'total_rewards_earned', 'total_spent_by_referred_users', 'average_order_value', 'loyalty_points_earned']

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['id', 'program', 'referrer', 'referred', 'reward_given'] # '__all__' #
        