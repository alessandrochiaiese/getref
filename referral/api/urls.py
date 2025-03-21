from django.urls import path
from referral.api.views.views_referral_audit import ReferralAuditAPIView
from referral.api.views.views_referral_bonus import ReferralBonusAPIView
from referral.api.views.views_referral_campaign import ReferralCampaignAPIView
from referral.api.views.views_referral_code import ReferralCodeAPIView
from referral.api.views.views_referral_commission import ReferralCommissionAPIView
from referral.api.views.views_referral_conversion import ReferralConversionAPIView
from referral.api.views.views_referral_notification import ReferralNotificationAPIView
from referral.api.views.views_referral_program import ReferralProgramAPIView
from referral.api.views.views_referral_program_partecipation import ReferralProgramPartecipationAPIView
from referral.api.views.views_referral_settings import ReferralSettingsAPIView
from referral.api.views.views_referral_stats import ReferralStatsAPIView
from referral.api.views.views_referral_transaction import ReferralTransactionAPIView

urlpatterns = [
    #path("referral/program/", ReferralProgramView.as_view(), name="referral-program"),
    #path("referral/", ReferralView.as_view(), name="referral"),
    #path("referral/reward/<int:referral_id>/", ReferralRewardView.as_view(), name="referral-reward"),

    path('audits/', ReferralAuditAPIView.as_view(), name='referral_audits'),
    path('audits/<int:referral_audit_id>/', ReferralAuditAPIView.as_view(), name='referral_audit'),

    path('bonus/', ReferralBonusAPIView.as_view(), name='referral_bonuses'),
    path('bonus/<int:referral_bonus_id>/', ReferralBonusAPIView.as_view(), name='referral_bonus'), 

    path('campaigns/', ReferralCampaignAPIView.as_view(), name='referral_campaigns'),
    path('campaigns/<int:referral_campaign_id>/', ReferralCampaignAPIView.as_view(), name='referral_campaign'), 

    path('codes/', ReferralCodeAPIView.as_view(), name='referral_codes'),
    path('codes/<int:referral_code_id>/', ReferralCodeAPIView.as_view(), name='referral_code'), 

    path('commissions/', ReferralCommissionAPIView.as_view(), name='referral_commissions'),
    path('commissions/<int:referral_commission_id>/', ReferralCommissionAPIView.as_view(), name='referral_commission'), 
    
    path('conversions/', ReferralConversionAPIView.as_view(), name='referral_conversions'),
    path('conversions/<int:referral_conversion_id>/', ReferralConversionAPIView.as_view(), name='referral_conversion'), 
    
    path('notifications/', ReferralNotificationAPIView.as_view(), name='referral_notifications'),
    path('notifications/<int:referral_notification_id>/', ReferralNotificationAPIView.as_view(), name='referral_notification'), 
    
    path('rewards/', ReferralProgramAPIView.as_view(), name='referral_rewards'),
    path('rewards/<int:referral_reward_id>/', ReferralProgramAPIView.as_view(), name='referral_reward'),

    path('programs/', ReferralProgramAPIView.as_view(), name='referral_programs'),
    path('programs/<int:referral_program_id>/', ReferralProgramAPIView.as_view(), name='referral_program'),

    path('programs/<int:referral_program_id>/partecipations/', ReferralProgramPartecipationAPIView.as_view(), name='referral_program_partecipations'),
    path('programs/<int:referral_program_id>/partecipations/<int:referral_program_partecipation_id>', ReferralProgramPartecipationAPIView.as_view(), name='referral_program_partecipation'),
    
    path('stats/', ReferralStatsAPIView.as_view(), name='referral_stats'),
    path('stats/<int:referral_stat_id>/', ReferralStatsAPIView.as_view(), name='referral_stat'),
     
    path('settings/', ReferralSettingsAPIView.as_view(), name='referral_settings'),
    path('settings/<int:referral_setting_id>/', ReferralSettingsAPIView.as_view(), name='referral_setting'),
     
    path('transactions/', ReferralTransactionAPIView.as_view(), name='referral_transactions'),
    path('transactions/<int:referral_transaction_id>/', ReferralTransactionAPIView.as_view(), name='referral_transaction'),
    
]
