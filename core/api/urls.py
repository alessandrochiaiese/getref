from django.urls import path
from . import views

urlpatterns = [
    path('referral-levels/', views.ReferralLevelAPIView, name='referral_level_api_list'),
    path('referral-levels/<int:pk>/', views.ReferralLevelAPIView, name='referral_level_api_detail'),
    
    path('stats/', views.StatsAPIView, name='stats_api_list'),
    path('stats/<int:pk>/', views.StatsAPIView, name='stats_api_detail'),
    
    path('conversions/', views.ConversionAPIView, name='conversion_api_list'),
    path('conversions/<int:pk>/', views.ConversionAPIView, name='conversion_api_detail'),
    
    path('bonus/', views.BonusAPIView, name='bonus_api_list'),
    path('bonus/<int:pk>/', views.BonusAPIView, name='bonus_api_detail'),
    
    path('referral-codes/', views.ReferralCodeAPIView, name='referral_code_api_list'),
    path('referral-codes/<int:pk>/', views.ReferralCodeAPIView, name='referral_code_api_detail'),
    
    path('support-tickets/', views.SupportTicketAPIView, name='support_ticket_api_list'),
    path('support-tickets/<int:pk>/', views.SupportTicketAPIView, name='support_ticket_api_detail'),
    
    path('tiers/', views.TierAPIView, name='tier_api_list'),
    path('tiers/<int:pk>/', views.TierAPIView, name='tier_api_detail'),
    
    path('commissions/', views.CommissionAPIView, name='commission_api_list'),
    path('commissions/<int:pk>/', views.CommissionAPIView, name='commission_api_detail'),
    
    path('affiliates/', views.AffiliateAPIView, name='affiliate_api_list'),
    path('affiliates/<int:pk>/', views.AffiliateAPIView, name='affiliate_api_detail'),
    
    path('settings/', views.SettingsAPIView, name='settings_api_list'),
    path('settings/<int:pk>/', views.SettingsAPIView, name='settings_api_detail'),
    
    path('engagements/', views.EngagementAPIView, name='engagement_api_list'),
    path('engagements/<int:pk>/', views.EngagementAPIView, name='engagement_api_detail'),
    
    path('campaigns/', views.CampaignAPIView, name='campaign_api_list'),
    path('campaigns/<int:pk>/', views.CampaignAPIView, name='campaign_api_detail'),
    
    path('payment-methods/', views.PaymentMethodAPIView, name='payment_method_api_list'),
    path('payment-methods/<int:pk>/', views.PaymentMethodAPIView, name='payment_method_api_detail'),
    
    path('audits/', views.AuditAPIView, name='audit_api_list'),
    path('audits/<int:pk>/', views.AuditAPIView, name='audit_api_detail'),
    
    path('notifications/', views.NotificationAPIView, name='notification_api_list'),
    path('notifications/<int:pk>/', views.NotificationAPIView, name='notification_api_detail'),
    
    path('performances/', views.PerformanceAPIView, name='performance_api_list'),
    path('performances/<int:pk>/', views.PerformanceAPIView, name='performance_api_detail'),
    
    path('payouts/', views.PayoutAPIView, name='payout_api_list'),
    path('payouts/<int:pk>/', views.PayoutAPIView, name='payout_api_detail'),
    
    path('rewards/', views.RewardAPIView, name='reward_api_list'),
    path('rewards/<int:pk>/', views.RewardAPIView, name='reward_api_detail'),
    
    path('transactions/', views.TransactionAPIView, name='transaction_api_list'),
    path('transactions/<int:pk>/', views.TransactionAPIView, name='transaction_api_detail'),
    
    path('links/', views.LinkAPIView, name='link_api_list'),
    path('links/<int:pk>/', views.LinkAPIView, name='link_api_detail'),
    
    path('participants/', views.ParticipantAPIView, name='participant_api_list'),
    path('participants/<int:pk>/', views.ParticipantAPIView, name='participant_api_detail'),
    
    path('programs/', views.ProgramAPIView, name='program_api_list'),
    path('programs/<int:pk>/', views.ProgramAPIView, name='program_api_detail'),
]
