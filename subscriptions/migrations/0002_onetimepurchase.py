# Generated by Django 5.1.3 on 2025-02-11 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimePurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=255)),
                ('price_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('status', models.CharField(default='completed', max_length=50)),
                ('purchased_at', models.DateTimeField(auto_now_add=True)),
                ('stripe_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.stripecustomer')),
            ],
        ),
    ]
