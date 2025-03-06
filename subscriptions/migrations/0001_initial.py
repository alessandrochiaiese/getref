# Generated by Django 5.1.3 on 2025-03-06 13:47

import django.db.models.deletion
import oauth2_provider.generators
import oauth2_provider.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(choices=[('daily', 'Giornaliero'), ('weekly', 'Settimanale'), ('monthly', 'Mensile'), ('yearly', 'Annuale')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tokens_included', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TokenPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_in_cents', models.IntegerField()),
                ('tokens', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TokenPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('last_used_at', models.DateTimeField(blank=True, null=True)),
                ('request_count', models.PositiveIntegerField(default=0)),
                ('plan', models.CharField(choices=[('free', 'Free'), ('pro', 'Pro')], default='free', max_length=20)),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=255, null=True)),
                ('client_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomApplication',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('client_id', models.CharField(db_index=True, default=oauth2_provider.generators.generate_client_id, max_length=100, unique=True)),
                ('redirect_uris', models.TextField(blank=True, help_text='Allowed URIs list, space separated')),
                ('post_logout_redirect_uris', models.TextField(blank=True, default='', help_text='Allowed Post Logout URIs list, space separated')),
                ('client_type', models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], max_length=32)),
                ('authorization_grant_type', models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials'), ('openid-hybrid', 'OpenID connect hybrid')], max_length=32)),
                ('client_secret', oauth2_provider.models.ClientSecretField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, help_text='Hashed on Save. Copy it now if this is a new secret.', max_length=255)),
                ('hash_client_secret', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('algorithm', models.CharField(blank=True, choices=[('', 'No OIDC support'), ('RS256', 'RSA with SHA-2 256'), ('HS256', 'HMAC with SHA-2 256')], default='', max_length=5)),
                ('allowed_origins', models.TextField(blank=True, default='', help_text='Allowed origins list to enable CORS, space separated')),
                ('extra_field', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_product_id', models.CharField(max_length=255)),
                ('promotion_link', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchased_at', models.DateTimeField(auto_now_add=True)),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.promotion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StripeCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripeCustomerId', models.CharField(max_length=255)),
                ('stripeSubscriptionId', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'StripeCustomer',
                'verbose_name_plural': 'StripeCustomers',
                'db_table': 'stripe_customers',
            },
        ),
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
        migrations.CreateModel(
            name='StripeSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('subscription_date', models.DateTimeField(auto_now_add=True)),
                ('stripe_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='subscriptions.stripecustomer')),
            ],
            options={
                'verbose_name': 'StripeSubscription',
                'verbose_name_plural': 'StripeSubscriptions',
                'db_table': 'custom_stripe_subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='APIUsageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('api_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.apikey')),
            ],
            options={
                'indexes': [models.Index(fields=['timestamp'], name='subscriptio_timesta_552a5a_idx')],
            },
        ),
    ]
