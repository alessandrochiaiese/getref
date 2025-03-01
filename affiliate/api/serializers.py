# affiliate_system/serializers.py

from rest_framework import serializers
from affiliate.models import *

class AffiliateAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateAudit
        fields = ['id', 'action_taken', 'user', 'ip_address', 'device_info', 'location'] #'__all__'

class AffiliateCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateCampaign
        fields = ['id', 'campaign_name', 'start_date', 'end_date', 'goal', 'budget', 'spending_to_date', 'target_audience'] #'__all__'

class AffiliateCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateCommission
        fields = ['id', 'amount', 'currency', 'date_awarded', 'status', 'approved_by', 'commission_type', 'description', 'tier'] #'__all__'

class AffiliateIncentiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateIncentive
        fields = ['id', 'program', 'incentive_type', 'amount', 'currency', 'status', 'description', 'ip_address', 'device_info', 'tracking_id', 'expiration_date is_incentive_active'] #'__all__'

class AffiliateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateLink
        fields = ['id', 'url', 'click_count', 'conversion_count', 'last_used', 'link_status', 'landing_page', 'custom_tracking_id'] #'__all__'
                  
class AffiliateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateNotification
        fields = ['id', 'user', 'message', 'is_read', 'notification_type', 'priority', 'action_required'] #'__all__'
                  
class AffiliatePayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliatePayout
        fields = ['id', 'amount', 'currency', 'payout_method', 'payout_status', 'transaction_id', 'processing_fee', 'net_amount', 'payout_provider'] #'__all__'
                  
class AffiliatePerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliatePerformance
        fields = '__all__'
                  
class AffiliateProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateProgram
        fields = ['id', 'name', 'description', 'reward_type', 'reward_value', 'currency', 'min_referral_count', 'max_referrals_per_user', 'is_active', 'program_duration', 'allowed_regions', 'target_industry'] #'__all__'
                  
class AffiliateProgramPartecipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateProgramPartecipation
        fields = ['id', 'reward_earned', 'status'] #'__all__'
        
class AffiliateRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateReward
        fields = ['id', 'referred_user', 'reward_type', 'reward_value', 'status', 'expiry_date', 'reward_description', 'reward_source'] #'__all__'
                  
class AffiliateSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateSettings
        fields = ['id', 'user', 'default_reward_type', 'max_referrals_allowed', 'notification_preference', 'auto_share_setting', 'social_share_message'] #'__all__'
                  
class AffiliateSupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateSupportTicket
        fields = ['id', 'ticket_number', 'subject', 'description', 'status', 'date_closed', 'priority', 'assigned_agent'] #'__all__'
        
class AffiliateTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateTier
        fields = ['id', 'tier_name', 'min_sales', 'commission_rate', 'tier_benefits', 'access_level', 'next_tier_threshold', 'tier_expiration'] #'__all__'
        
class AffiliateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateTransaction
        fields = ['id', 'referred_user', 'order_id', 'transaction_amount', 'currency', 'status', 'conversion_value', 'discount_value', 'coupon_code_used', 'channel'] #'__all__'
