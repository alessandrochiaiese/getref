
from django.contrib import admin
from .models import Program
from .models import Participant
from .models import Link
from .models import Transaction
from .models import Reward
from .models import Payout
from .models import Performance
from .models import Notification
from .models import Audit
from .models import PaymentMethod
from .models import Campaign
from .models import Engagement
from .models import Settings
from .models import Affiliate
from .models import Commission
from .models import Tier
from .models import SupportTicket
from .models import ReferralCode
from .models import Bonus
from .models import Conversion
from .models import Stats
from .models import ReferralLevel


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['id', 'program']


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'participant']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'link']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction']


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ['id', 'reward']


@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'payout']


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'performance']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'notification']


@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ['id', 'audit']


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'paymentmethod']


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['id', 'campaign']


@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = ['id', 'engagement']


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'settings']


@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    list_display = ['id', 'affiliate']


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'commission']


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ['id', 'tier']


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'supportticket']


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'referralcode']


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ['id', 'bonus']


@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ['id', 'conversion']


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'stats']


@admin.register(ReferralLevel)
class ReferralLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'referrallevel']


admin.site.register(Program, ProgramAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(Payout, PayoutAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Audit, AuditAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Engagement, EngagementAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Affiliate, AffiliateAdmin)
admin.site.register(Commission, CommissionAdmin)
admin.site.register(Tier, TierAdmin)
admin.site.register(SupportTicket, SupportTicketAdmin)
admin.site.register(ReferralCode, ReferralCodeAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Conversion, ConversionAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(ReferralLevel, ReferralLevelAdmin)