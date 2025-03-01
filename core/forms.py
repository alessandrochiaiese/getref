from django import forms
from .models.program import Program
from .models.participant import Participant
from .models.link import Link
from .models.transaction import Transaction
from .models.reward import Reward
from .models.payout import Payout
from .models.performance import Performance
from .models.notification import Notification
from .models.audit import Audit
from .models.payment_method import PaymentMethod
from .models.campaign import Campaign
from .models.engagement import Engagement
from .models.settings import Settings
from .models.affiliate import Affiliate
from .models.commission import Commission
from .models.tier import Tier
from .models.support_ticket import SupportTicket
from .models.referral_code import ReferralCode
from .models.bonus import Bonus
from .models.conversion import Conversion
from .models.stats import Stats
from .models.referral_level import ReferralLevel



class ProgramForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    description = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    program_type = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    reward_type = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    reward_value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    currency = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    commission_rate = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    min_payout_threshold = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    max_payout_limit = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    date_created = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    is_active = forms.BooleanField( widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=True, )
    duration = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    allowed_regions = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    target_industry = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Program
        fields = '__all__'



class ParticipantForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    user_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    total_earnings = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    account_balance = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    date_joined = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    last_login = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    referral_source = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Participant
        fields = '__all__'



class LinkForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    url = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    click_count = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    conversion_count = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    date_created = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    last_used = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    landing_page = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    custom_tracking_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Link
        fields = '__all__'



class TransactionForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    link_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    transaction_amount = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    transaction_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    order_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    product_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    payment_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    commission_rate = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    discount_applied = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    coupon_code = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Transaction
        fields = '__all__'



class RewardForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    reward_type = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    reward_value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    currency = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    date_awarded = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    expiry_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    description = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    source = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Reward
        fields = '__all__'



class PayoutForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    amount = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    currency = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    payout_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    payout_method = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    transaction_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    processing_fee = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    net_amount = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    provider = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Payout
        fields = '__all__'



class PerformanceForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    period = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    total_clicks = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    total_conversions = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    conversion_rate = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    total_earnings = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    average_order_value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    refund_rate = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    customer_lifetime_value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    top_product = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Performance
        fields = '__all__'



class NotificationForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    message = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    date_sent = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    is_read = forms.BooleanField( widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=True, )
    priority = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    type = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    action_required = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Notification
        fields = '__all__'



class AuditForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    action_taken = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    action_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    ip_address = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    device_info = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    location = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Audit
        fields = '__all__'





class PaymentMethodForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    amount = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    description = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    paid = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    user_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = PaymentMethod
        fields = '__all__'




class CampaignForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    start_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    end_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    goal = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    budget = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    spending_to_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    target_audience = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Campaign
        fields = '__all__'



class EngagementForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    link_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    email_opened = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    email_clicked = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    social_share_count = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    last_interaction_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Engagement
        fields = '__all__'



class SettingsForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    preferred_currency = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    preferred_payment_method = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    payout_schedule = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    notification_preference = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    dashboard_layout = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    auto_share_setting = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    social_share_message = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Settings
        fields = '__all__'




class AffiliateForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    user_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    email = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    phone = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    date_joined = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    total_earnings = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    country = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    profile_picture = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    account_balance = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    last_login = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    referral_source = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Affiliate
        fields = '__all__'



class CommissionForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    amount = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    currency = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    date_awarded = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    approved_by = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    type = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    description = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    tier = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Commission
        fields = '__all__'



class TierForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    tier_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    min_sales = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    commission_rate = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    benefits = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    access_level = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    next_tier_threshold = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    expiration_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Tier
        fields = '__all__'



class SupportTicketForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    ticket_number = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    description = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    date_created = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    date_closed = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    priority = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    assigned_agent = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = SupportTicket
        fields = '__all__'



class ReferralCodeForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    participant_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    code = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    usage_count = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    date_created = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    expiry_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    referred_user_count = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    unique_url = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    campaign_source = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    campaign_medium = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = ReferralCode
        fields = '__all__'



class BonusForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    program_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    type = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    min_referrals_required = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    bonus_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    expiry_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    max_usage = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    eligibility_criteria = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Bonus
        fields = '__all__'



class ConversionForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    link_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    referred_user_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    conversion_date = forms.DateTimeField( widget=forms.DateInput(attrs={'class': 'form-control'}), required=True, )
    conversion_value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    status = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    reward_issued = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    source = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    type = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Conversion
        fields = '__all__'



class StatsForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    link_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    period = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    click_count = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    conversion_count = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    total_rewards = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    average_conversion_value = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    highest_referral_earning = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = Stats
        fields = '__all__'



class ReferralLevelForm(forms.ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    referrer = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    referred = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, )
    level = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True, )
    class Meta:
        model = ReferralLevel
        fields = '__all__'
