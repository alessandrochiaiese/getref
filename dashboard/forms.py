from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import * 


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User #get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control file-upload-info'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    #name_business = forms.CharField(widget=forms.TextInput(attrs={'required': False}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class UpdateBaseProfileForm(forms.ModelForm):
    
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False,
        input_formats=['%Y-%m-%d']  # Formato ISO della data, come "YYYY-MM-DD"
    )
    city = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    CAP = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control'}))
    
    class Meta:
        model = Profile
        fields = ['birth_date', 'city', 'street', 'CAP', 'phone_number',]


class UpdateBusinessProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control file-upload-info'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    # business
    name_business = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    iva = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'name_business', 'iva']





class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = ProfileBusiness
        fields = [
            'number_job_request_desidered_per_week',
            'have_office_shop_to_receive_customers',
            'link_google_maps',
            'contact_number',
            'chamber_commerce_certificate',
            'insurance_policy_certificate',
            'region',
            'sectors',
            'holder',
            'company_name',
            'email',
        ]
        widgets = {
            'number_job_request_desidered_per_week': forms.NumberInput(attrs={'class': 'form-control'}),
            'have_office_shop_to_receive_customers': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'link_google_maps': forms.URLInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'chamber_commerce_certificate': forms.ClearableFileInput(attrs={'required': False, 'class': 'form-control'}),
            'insurance_policy_certificate': forms.ClearableFileInput(attrs={'required': False, 'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'sectors': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'holder': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.all()
        self.fields['sectors'].queryset = Sector.objects.all()


# referral models 
class ReferralAuditForm(forms.ModelForm):
    class Meta:
        model = ReferralAudit
        #fields = ['id', 'action_taken', 'action_date', 'user', 'ip_address', 'device_info', 'location']# '__all__' #
        fields = ['id', 'action_taken', 'user', 'ip_address', 'device_info', 'location']# '__all__' #

class ReferralBonusForm(forms.ModelForm):
    class Meta:
        model = ReferralBonus
        fields = ['id', 'bonus_type', 'bonus_value', 'min_referrals_required', 'bonus_date', 'expiry_date', 'max_usage', 'eligibility_criteria']# '__all__' #

class ReferralCampaignForm(forms.ModelForm):
    class Meta:
        model = ReferralCampaign
        fields = ['id', 'campaign_name', 'start_date', 'end_date', 'goal', 'budget', 'spending_to_date', 'target_audience']# '__all__' #

class ReferralCodeForm(forms.ModelForm):
    class Meta:
        model = ReferralCode
        #fields = ['id', 'code', 'usage_count', 'date_created', 'status', 'expiry_date', 'referred_user_count', 'unique_url', 'campaign_source', 'campaign_medium']# '__all__' #
        fields = ['id', 'code', 'usage_count', 'status', 'expiry_date', 'referred_user_count', 'unique_url', 'campaign_source', 'campaign_medium']# '__all__' #

class ReferralConversionForm(forms.ModelForm):
    class Meta:
        model = ReferralConversion
        #fields = ['id', 'referred_user', 'conversion_value', 'status', 'reward_issued', 'conversion_source', 'referral_type']# '__all__' #
        fields = ['id', 'referred_user', 'conversion_date', 'conversion_value', 'status', 'reward_issued', 'conversion_source', 'referral_type']# '__all__' #

class ReferralEngagementForm(forms.ModelForm):
    class Meta:
        model = ReferralEngagement
        #fields = ['id', 'user', 'email_opened', 'email_clicked', 'social_share_count', 'last_interaction_date']# '__all__' #
        fields = ['id', 'user', 'email_opened', 'email_clicked', 'social_share_count']# '__all__' #

class ReferralNotificationForm(forms.ModelForm):
    class Meta:
        model = ReferralNotification
        #fields = ['id', 'user', 'message', 'date_sent', 'is_read', 'notification_type', 'priority', 'action_required']# '__all__' #
        fields = ['id', 'user', 'message', 'is_read', 'notification_type', 'priority', 'action_required']# '__all__' #

class ReferralProgramForm(forms.ModelForm):
    class Meta:
        model = ReferralProgram
        #fields = ['id', 'name', 'description', 'reward_type', 'reward_value', 'currency', 'min_referral_count', 'max_referrals_per_user', 'date_created', 'is_active', 'program_duration', 'allowed_regions', 'target_industry']# '__all__' #
        fields = ['id', 'name', 'description', 'reward_type', 'reward_value', 'currency', 'min_referral_count', 'max_referrals_per_user', 'is_active', 'program_duration', 'allowed_regions', 'target_industry']# '__all__' #

class ReferralProgramPartecipationForm(forms.ModelForm):
    class Meta:
        model = ReferralProgramPartecipation
        #fields = ['id', 'date_joined', 'reward_earned', 'status']# '__all__' #
        fields = ['id', 'reward_earned', 'status']# '__all__' #

class ReferralRewardForm(forms.ModelForm):
    class Meta:
        model = ReferralReward
        #fields = ['id', 'referred_user', 'reward_type', 'reward_value', 'date_awarded', 'status', 'expiry_date', 'reward_description', 'reward_source']# '__all__' #
        fields = ['id', 'referred_user', 'reward_type', 'reward_value', 'status', 'expiry_date', 'reward_description', 'reward_source']# '__all__' #

class ReferralSettingsForm(forms.ModelForm):
    class Meta:
        model = ReferralSettings
        fields = ['id', 'user', 'default_reward_type', 'max_referrals_allowed', 'notification_preference', 'auto_share_setting', 'social_share_message']# '__all__' #

class ReferralStatsForm(forms.ModelForm):
    class Meta:
        model = ReferralStats
        fields = ['id', 'period', 'click_count', 'conversion_count', 'total_rewards', 'average_conversion_value', 'highest_referral_earning']# '__all__' #

class ReferralTransactionForm(forms.ModelForm):
    class Meta:
        model = ReferralTransaction
        #fields = ['id', 'referred_user', 'transaction_date', 'order_id', 'transaction_amount', 'currency', 'status', 'conversion_value', 'discount_value', 'coupon_code_used', 'channel']# '__all__' #
        fields = ['id', 'referred_user', 'order_id', 'transaction_amount', 'currency', 'status', 'conversion_value', 'discount_value', 'coupon_code_used', 'channel']# '__all__' #

class ReferralUserForm(forms.ModelForm):
    class Meta:
        model = ReferralUser
        #fields = ['id', 'program', 'referrer', 'referred', 'reward_given']# '__all__' #
        fields = '__all__' #

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        #fields = ['id', 'user', 'total_rewards_earned', 'total_spent_by_referred_users', 'average_order_value', 'loyalty_points_earned']# '__all__' #
        fields = '__all__'