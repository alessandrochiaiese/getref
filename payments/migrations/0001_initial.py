# Generated by Django 5.1.3 on 2025-03-06 13:47

import django.db.models.deletion
import payments.models.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Description')),
                ('thumbnail', models.ImageField(blank=True, upload_to=payments.models.utils.get_image_filename, verbose_name='Thumbnail')),
                ('url', models.URLField(verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'CustomProduct',
                'verbose_name_plural': 'CustomProducts',
                'db_table': 'custom_products',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Designates the name of the tag.', max_length=100, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'CustomProductTag',
                'verbose_name_plural': 'CustomProductTags',
                'db_table': 'custom_product_tags',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='CustomOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Amount')),
                ('description', models.CharField(max_length=128, verbose_name='Description')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Buyer')),
            ],
            options={
                'verbose_name': 'CustomOrder',
                'verbose_name_plural': 'CustomOrder',
                'db_table': 'custom_orders',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=50, verbose_name='Status')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Price')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'MyCustomOrder',
                'verbose_name_plural': 'MyCustomOrders',
                'db_table': 'my_orders',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MyPaymentMethod',
                'verbose_name_plural': 'MyPaymentMethods',
                'db_table': 'my_payment_methods',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='payments.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'MyPrice',
                'verbose_name_plural': 'MyPrices',
                'db_table': 'my_prices',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.product')),
            ],
            options={
                'verbose_name': 'MyCustomOrderItem',
                'verbose_name_plural': 'MyCustomOrderItems',
                'db_table': 'my_custom_order_items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='payments.OrderItem', to='payments.product', verbose_name='Products'),
        ),
    ]
