# Generated by Django 5.1.3 on 2025-01-25 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('usage_count', models.IntegerField(default=0)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('referred_user_count', models.IntegerField(default=0)),
                ('unique_url', models.URLField(blank=True)),
                ('campaign_source', models.CharField(blank=True, max_length=100)),
                ('campaign_medium', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral_code_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Code',
                'verbose_name_plural': 'Referral Codes',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='ReferralAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_taken', models.TextField()),
                ('action_date', models.DateField()),
                ('ip_address', models.GenericIPAddressField()),
                ('device_info', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral_audit_referral_user', to=settings.AUTH_USER_MODEL)),
                ('referral_codes', models.ManyToManyField(related_name='referral_audit_referral_codes', to='referral.referralcode')),
            ],
            options={
                'verbose_name': 'Referral Audit',
                'verbose_name_plural': 'Referral Audits',
                'ordering': ['-action_date'],
            },
        ),
        migrations.CreateModel(
            name='ReferralConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversion_date', models.DateField()),
                ('conversion_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
                ('reward_issued', models.BooleanField(default=False)),
                ('conversion_source', models.CharField(max_length=50)),
                ('referral_type', models.CharField(blank=True, max_length=50)),
                ('referral_codes', models.ManyToManyField(related_name='referral_conversion_referral_codes', to='referral.referralcode')),
                ('referred_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral_conversion_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Conversation',
                'verbose_name_plural': 'Referral Conversations',
                'ordering': ['-conversion_date'],
            },
        ),
        migrations.CreateModel(
            name='ReferralEngagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_opened', models.BooleanField(default=False)),
                ('email_clicked', models.BooleanField(default=False)),
                ('social_share_count', models.IntegerField(default=0)),
                ('last_interaction_date', models.DateField(blank=True, null=True)),
                ('referral_codes', models.ManyToManyField(related_name='referral_engagement_referral_codes', to='referral.referralcode')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Engagement',
                'verbose_name_plural': 'Referral Engagements',
                'ordering': ['-last_interaction_date'],
            },
        ),
        migrations.CreateModel(
            name='ReferralNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_sent', models.DateField()),
                ('is_read', models.BooleanField(default=False)),
                ('notification_type', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('action_required', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engagement_notification_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Notification',
                'verbose_name_plural': 'Referral Notifications',
                'ordering': ['-date_sent'],
            },
        ),
        migrations.CreateModel(
            name='ReferralProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('reward_type', models.CharField(max_length=50)),
                ('reward_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('min_referral_count', models.IntegerField(default=0)),
                ('max_referrals_per_user', models.IntegerField(default=100)),
                ('date_created', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('program_duration', models.IntegerField()),
                ('target_industry', models.CharField(max_length=100)),
                ('allowed_regions', models.ManyToManyField(related_name='engagement_program_regions', to='dashboard.region')),
            ],
            options={
                'verbose_name': 'Referral Program',
                'verbose_name_plural': 'Referral Program',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='referralcode',
            name='programs',
            field=models.ManyToManyField(related_name='referral_code_programs', to='referral.referralprogram'),
        ),
        migrations.CreateModel(
            name='ReferralCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('goal', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spending_to_date', models.DecimalField(decimal_places=2, max_digits=10)),
                ('target_audience', models.TextField(blank=True)),
                ('programs', models.ManyToManyField(related_name='referral_campaign_programs', to='referral.referralprogram')),
            ],
            options={
                'verbose_name': 'Referral Campaign',
                'verbose_name_plural': 'Referral Campaigns',
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='ReferralBonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus_type', models.CharField(max_length=50)),
                ('bonus_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_referrals_required', models.IntegerField(default=0)),
                ('bonus_date', models.DateField()),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('max_usage', models.IntegerField(default=1)),
                ('eligibility_criteria', models.TextField(blank=True)),
                ('programs', models.ManyToManyField(related_name='referral_bonus_programs', to='referral.referralprogram')),
            ],
            options={
                'verbose_name': 'Referral Bonus',
                'verbose_name_plural': 'Referral Bonus',
                'ordering': ['-expiry_date'],
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_given', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('referred', models.ManyToManyField(related_name='referrals_received', to=settings.AUTH_USER_MODEL)),
                ('referrer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='referrals_made', to=settings.AUTH_USER_MODEL)),
                ('program', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='referral.referralprogram')),
            ],
            options={
                'verbose_name': 'Referral',
                'verbose_name_plural': 'Referrals',
            },
        ),
        migrations.CreateModel(
            name='ReferralProgramPartecipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('reward_earned', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=50)),
                ('programs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='engagement_program_partecipation_programs', to='referral.referralprogram')),
                ('referral_codes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='engagement_program_partecipation_referral_codes', to='referral.referralcode')),
            ],
            options={
                'verbose_name': 'Referral Program Partecipation',
                'verbose_name_plural': 'Referral Program Partecipations',
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='ReferralReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_type', models.CharField(max_length=50)),
                ('reward_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_awarded', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('reward_description', models.TextField(blank=True)),
                ('reward_source', models.CharField(blank=True, max_length=100)),
                ('referral_codes', models.ManyToManyField(related_name='referra_reward_referral_codes', to='referral.referralcode')),
                ('referred_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referra_reward_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Reward',
                'verbose_name_plural': 'Referral Rewards',
                'ordering': ['-date_awarded'],
            },
        ),
        migrations.CreateModel(
            name='ReferralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_reward_type', models.CharField(max_length=50)),
                ('max_referrals_allowed', models.IntegerField(default=100)),
                ('notification_preference', models.CharField(max_length=50)),
                ('auto_share_setting', models.BooleanField(default=True)),
                ('social_share_message', models.TextField(blank=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referra_setting_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Settings',
                'verbose_name_plural': 'Referral Settings',
            },
        ),
        migrations.CreateModel(
            name='ReferralStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=50)),
                ('click_count', models.IntegerField(default=0)),
                ('conversion_count', models.IntegerField(default=0)),
                ('total_rewards', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_conversion_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('highest_referral_earning', models.DecimalField(decimal_places=2, max_digits=10)),
                ('referral_codes', models.ManyToManyField(related_name='referra_stats_referral_codes', to='referral.referralcode')),
            ],
            options={
                'verbose_name': 'Referral Stat',
                'verbose_name_plural': 'Referral Stats',
            },
        ),
        migrations.CreateModel(
            name='ReferralTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('order_id', models.CharField(max_length=255)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=50)),
                ('conversion_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('coupon_code_used', models.CharField(blank=True, max_length=100)),
                ('channel', models.CharField(blank=True, max_length=50)),
                ('referral_codes', models.ManyToManyField(related_name='referra_transaction_referral_codes', to='referral.referralcode')),
                ('referred_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referra_transaction_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Transaction',
                'verbose_name_plural': 'Referral Transactions',
                'ordering': ['-transaction_date'],
            },
        ),
        migrations.CreateModel(
            name='ReferralUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_referrals', models.IntegerField(default=0)),
                ('active_referrals', models.IntegerField(default=0)),
                ('inactive_referrals', models.IntegerField(default=0)),
                ('total_rewards_earned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_spent_by_referred_users', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_order_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loyalty_points_earned', models.IntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referra_user_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral User',
                'verbose_name_plural': 'Referral Users',
            },
        ),
    ]
