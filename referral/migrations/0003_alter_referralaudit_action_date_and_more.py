# Generated by Django 5.1.3 on 2025-03-06 17:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0002_alter_referralprogram_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referralaudit',
            name='action_date',
            field=models.DateField(auto_now_add=True, verbose_name='Action Date'),
        ),
        migrations.AlterField(
            model_name='referralbonus',
            name='bonus_date',
            field=models.DateField(auto_now_add=True, verbose_name='Bonus Date'),
        ),
        migrations.AlterField(
            model_name='referralbonus',
            name='bonus_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Discount', 'Discount'), ('Points', 'Points')], default='Cash', max_length=50, verbose_name='Bonus Type'),
        ),
        migrations.AlterField(
            model_name='referralbonus',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2025, 4, 5), null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='referralcode',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2025, 4, 5), null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='referralcode',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral_code_program', to='referral.referralprogram', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='referralcode',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Used', 'Used')], default='Active', max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='referralconversion',
            name='conversion_date',
            field=models.DateField(auto_now_add=True, verbose_name='Conversion Date'),
        ),
        migrations.AlterField(
            model_name='referralconversion',
            name='conversion_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Conversion Value'),
        ),
        migrations.AlterField(
            model_name='referralnotification',
            name='date_sent',
            field=models.DateField(auto_now_add=True, verbose_name='Date Sent'),
        ),
        migrations.AlterField(
            model_name='referralprogram',
            name='program_duration',
            field=models.IntegerField(default=90, verbose_name='Program Duration'),
        ),
        migrations.AlterField(
            model_name='referralprogram',
            name='reward_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Reward Value'),
        ),
        migrations.AlterField(
            model_name='referralreward',
            name='date_awarded',
            field=models.DateField(auto_now_add=True, verbose_name='Date Awarded'),
        ),
        migrations.AlterField(
            model_name='referralreward',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2025, 4, 5), null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='referralreward',
            name='reward_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Discount', 'Discount'), ('Points', 'Points')], default='Cash', max_length=50, verbose_name='Reward Type'),
        ),
        migrations.AlterField(
            model_name='referralreward',
            name='reward_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Reward Value'),
        ),
        migrations.AlterField(
            model_name='referralstats',
            name='average_conversion_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Average Conversione Value'),
        ),
        migrations.AlterField(
            model_name='referralstats',
            name='highest_referral_earning',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Highest Referral Earning'),
        ),
        migrations.AlterField(
            model_name='referralstats',
            name='total_rewards',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Total Rewards'),
        ),
        migrations.AlterField(
            model_name='referraltransaction',
            name='currency',
            field=models.CharField(default='EUR', max_length=10, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='referraltransaction',
            name='transaction_date',
            field=models.DateField(auto_now_add=True, verbose_name='Transaction Date'),
        ),
    ]
