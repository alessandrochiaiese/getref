# Generated by Django 5.1.3 on 2025-03-07 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0003_alter_referralaudit_action_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referralbonus',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2025, 4, 6), null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='referralcode',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2025, 4, 6), null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='referralprogram',
            name='reward_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Discount', 'Discount'), ('Points', 'Points'), ('Percentual', 'Percentual')], max_length=50, verbose_name='Reward Type'),
        ),
        migrations.AlterField(
            model_name='referralreward',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2025, 4, 6), null=True, verbose_name='Expiry Date'),
        ),
    ]
