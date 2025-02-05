# Generated by Django 5.1.3 on 2025-02-05 18:06

import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        ('payments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Phone')),
                ('date_joined', models.DateField(verbose_name='Date Joined')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('total_earnings', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Earning')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pics/', verbose_name='Profile Picture')),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Account Balance')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Last Login')),
                ('referral_source', models.CharField(max_length=255, verbose_name='Referral Source')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='AffiliateAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_taken', models.TextField(verbose_name='Action Taken')),
                ('action_date', models.DateField(verbose_name='Action Date')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP Address')),
                ('device_info', models.TextField(verbose_name='Device Info')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('affiliates', models.ManyToManyField(blank=True, related_name='affiliate_audit_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
            ],
            options={
                'verbose_name': 'Affiliate Audit',
                'verbose_name_plural': 'Affiliate Audits',
                'ordering': ['-action_date'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('date_sent', models.DateField(verbose_name='Date Sent')),
                ('is_read', models.BooleanField(default=False, verbose_name='Is Read')),
                ('priority', models.CharField(max_length=50, verbose_name='Priority')),
                ('notification_type', models.CharField(max_length=50, verbose_name='Notification Type')),
                ('affiliates', models.ManyToManyField(related_name='affiliate_notification_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
            ],
            options={
                'verbose_name': 'Affiliate Notification',
                'verbose_name_plural': 'Affiliate Notifications',
                'ordering': ['-date_sent'],
            },
        ),
        migrations.CreateModel(
            name='AffiliatePerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('annual', 'Annual')], max_length=50, verbose_name='Period')),
                ('total_clicks', models.IntegerField(verbose_name='Total Clicks')),
                ('total_conversions', models.IntegerField(verbose_name='Total Conversions')),
                ('conversion_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Conversion Rate')),
                ('total_earnings', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Earnings')),
                ('average_order_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Average Order Value')),
                ('refund_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Refund Rate')),
                ('customer_lifetime_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Customer Lifetime Value')),
                ('top_product', models.CharField(max_length=255, verbose_name='Top Product')),
                ('affiliates', models.ManyToManyField(related_name='affiliate_performance_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
            ],
            options={
                'verbose_name': 'Affiliate Perfomance',
                'verbose_name_plural': 'Affiliate Perfomances',
            },
        ),
        migrations.CreateModel(
            name='AffiliateProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('commission_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Commission Rate')),
                ('currency', models.CharField(max_length=10, verbose_name='Currency')),
                ('min_payout_threshold', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Min Payout Threshould')),
                ('max_payout_limit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Min Payout Limit')),
                ('date_created', models.DateField(verbose_name='Date Created')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('duration', models.IntegerField(verbose_name='Duration')),
                ('target_industry', models.CharField(max_length=100, verbose_name='Target Industry')),
                ('allowed_countries', models.ManyToManyField(related_name='affiliate_program_countries', to='dashboard.country', verbose_name='Allowed Countries')),
            ],
            options={
                'verbose_name': 'Affiliate Program',
                'verbose_name_plural': 'Affiliate Programs',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('click_count', models.IntegerField(default=0, verbose_name='Click Count')),
                ('conversion_count', models.IntegerField(default=0, verbose_name='Conversion Count')),
                ('date_created', models.DateField(verbose_name='Date Created')),
                ('last_used', models.DateTimeField(blank=True, null=True, verbose_name='Last Used')),
                ('link_status', models.CharField(max_length=50, verbose_name='Link Status')),
                ('landing_page', models.URLField(blank=True, verbose_name='Landing Page')),
                ('custom_tracking_id', models.CharField(blank=True, max_length=255, verbose_name='Custom Tracking ID')),
                ('affiliates', models.ManyToManyField(related_name='affiliate_link_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
                ('programs', models.ManyToManyField(related_name='affiliate_link_programs', to='affiliate.affiliateprogram', verbose_name='Programs')),
            ],
            options={
                'verbose_name': 'Affiliate Link',
                'verbose_name_plural': 'Affiliate Links',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateIncentive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incentive_type', models.CharField(choices=[('click', 'Click'), ('signup', 'Signup'), ('purchase', 'Purchase')], max_length=20, verbose_name='Incentive Type')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, verbose_name='Amount')),
                ('currency', models.CharField(default='USD', max_length=10, verbose_name='Currency')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined'), ('expired', 'Expired')], default='pending', max_length=20, verbose_name='Status')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP Address')),
                ('device_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Device Info')),
                ('tracking_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tracking ID')),
                ('expiration_date', models.DateTimeField(blank=True, null=True, verbose_name='Expiration Date')),
                ('is_incentive_active', models.BooleanField(default=True, verbose_name='Is Incentive Active')),
                ('affiliate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_incentive_affiliate', to='affiliate.affiliate', verbose_name='Affiliate')),
                ('program', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_incentive_program', to='affiliate.affiliateprogram', verbose_name='Program')),
            ],
            options={
                'verbose_name': 'Affiliate Incentive',
                'verbose_name_plural': 'Affiliate Incentives',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateCommission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('currency', models.CharField(max_length=10, verbose_name='Currency')),
                ('date_awarded', models.DateField(verbose_name='Date Awarded')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('approved_by', models.CharField(max_length=255, verbose_name='Approved By')),
                ('commission_type', models.CharField(max_length=50, verbose_name='Commission Type')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('tier', models.CharField(max_length=50, verbose_name='Tier')),
                ('affiliates', models.ManyToManyField(related_name='affiliate_commission_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
                ('programs', models.ManyToManyField(related_name='affiliate_commission_programs', to='affiliate.affiliateprogram', verbose_name='Programs')),
            ],
            options={
                'verbose_name': 'Affiliate Commission',
                'verbose_name_plural': 'Affiliate Commissions',
                'ordering': ['-date_awarded'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=255, verbose_name='Campaign Name')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('goal', models.TextField(verbose_name='Goal')),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Budget')),
                ('spending_to_date', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Spending To Date')),
                ('programs', models.ManyToManyField(related_name='affiliate_campaign_programs', to='affiliate.affiliateprogram', verbose_name='Programs')),
            ],
            options={
                'verbose_name': 'Affiliate Campaign',
                'verbose_name_plural': 'Affiliate Campaigns',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateProgramPartecipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('commission_earned', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Commission Earned')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=50, verbose_name='Status')),
                ('affiliate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_program_partecipation_affiliate', to='affiliate.affiliate', verbose_name='Affiliate')),
                ('program', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_program_partecipation_program', to='affiliate.affiliateprogram', verbose_name='Program')),
            ],
            options={
                'verbose_name': 'Affiliate Program Partecipation',
                'verbose_name_plural': 'Affiliate Program Partecipations',
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('affiliate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_reward_affiliates', to='affiliate.affiliate', verbose_name='Affiliate')),
            ],
            options={
                'verbose_name': 'Affiliate Reward',
                'verbose_name_plural': 'Affiliate Rewards',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AffiliateSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_currency', models.CharField(max_length=10, verbose_name='Preferred Currency')),
                ('preferred_payment_method', models.CharField(max_length=50, verbose_name='Preferred Payment Method')),
                ('payout_schedule', models.CharField(max_length=50, verbose_name='Payout Schedule')),
                ('notification_preference', models.CharField(max_length=50, verbose_name='Notification Preference')),
                ('dashboard_layout', models.CharField(max_length=50, verbose_name='Dashboard Layout')),
                ('affiliates', models.ManyToManyField(related_name='affiiate_setting_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
            ],
            options={
                'verbose_name': 'Affiliate Setting',
                'verbose_name_plural': 'Affiliate Settings',
            },
        ),
        migrations.CreateModel(
            name='AffiliateSupportTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=100, verbose_name='Ticket Number')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('description', models.TextField(verbose_name='Description')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('date_created', models.DateField(verbose_name='Date Created')),
                ('date_closed', models.DateField(blank=True, null=True, verbose_name='Date Closed')),
                ('priority', models.CharField(max_length=50, verbose_name='Priority')),
                ('assigned_agent', models.CharField(max_length=255, verbose_name='Assigned Agent')),
                ('affiliates', models.ManyToManyField(related_name='affiliate_supportticket_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
            ],
            options={
                'verbose_name': 'Affiliate Support Ticket',
                'verbose_name_plural': 'Affiliate Support Tickets',
            },
        ),
        migrations.CreateModel(
            name='AffiliateTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_name', models.CharField(max_length=50, verbose_name='Tier Name')),
                ('min_sales', models.IntegerField(verbose_name='Min Sales')),
                ('commission_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Commission Rate')),
                ('tier_benefits', models.TextField(blank=True, verbose_name='Tier Benefits')),
                ('access_level', models.IntegerField(verbose_name='Access Level')),
                ('next_tier_threshold', models.IntegerField(verbose_name='Next Tier Threshold')),
                ('tier_expiration', models.DateField(blank=True, null=True, verbose_name='Tier Expiration')),
                ('programs', models.ManyToManyField(related_name='affiliate_tier_programs', to='affiliate.affiliateprogram', verbose_name='Programs')),
            ],
            options={
                'verbose_name': 'Affiliate Tier',
                'verbose_name_plural': 'Affiliate Tiers',
            },
        ),
        migrations.CreateModel(
            name='AffiliateTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Transaction Amount')),
                ('transaction_date', models.DateField(verbose_name='Transaction Date')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Payment Date')),
                ('commission_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Commission Rate')),
                ('discount_applied', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Discount Applied')),
                ('coupon_code', models.CharField(blank=True, max_length=255, verbose_name='Coupon Code')),
                ('affiliates', models.ManyToManyField(related_name='affiliate_transaction_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
                ('commissions', models.ManyToManyField(related_name='affiliate_transaction_commissions', to='affiliate.affiliatecommission')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.order', verbose_name='Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Affiliate Transaction',
                'verbose_name_plural': 'Affiliate Transactions',
            },
        ),
        migrations.CreateModel(
            name='AffiliatePayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('currency', models.CharField(max_length=10, verbose_name='Currency')),
                ('payout_date', models.DateField(verbose_name='Payout Date')),
                ('payout_method', models.CharField(max_length=50, verbose_name='Payout Method')),
                ('payout_status', models.CharField(max_length=50, verbose_name='Payout Status')),
                ('processing_fee', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Processing Fee')),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Net Amount')),
                ('payout_provider', models.CharField(max_length=50, verbose_name='Payout Provider')),
                ('affiliates', models.ManyToManyField(related_name='affiliate_payout_affiliates', to='affiliate.affiliate', verbose_name='Affiliates')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='affiliate.affiliatetransaction', verbose_name='Transaction')),
            ],
            options={
                'verbose_name': 'Affiliate Payout',
                'verbose_name_plural': 'Affiliate Payouts',
                'ordering': ['-payout_date'],
            },
        ),
    ]
