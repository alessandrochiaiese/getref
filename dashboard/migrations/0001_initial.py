# Generated by Django 5.1.3 on 2025-03-06 13:47

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_google_maps', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link Google Maps')),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Conctac Number')),
                ('chamber_commerce_certificate', models.ImageField(default='default.jpg', help_text='Upload your chamber of commerce certificate.', upload_to='chamber_commerce_certificates', verbose_name='Chamber Commerce Certificate')),
                ('insurance_policy_certificate', models.FileField(default='default.jpg', help_text='Only image or PDF files are allowed.', upload_to='insurance_policy_certificates', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])], verbose_name='Insurance Policy Certificate')),
                ('holder', models.CharField(blank=True, max_length=255, null=True, verbose_name='Holder')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Company Name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Italia', max_length=256, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Nation',
                'verbose_name_plural': 'Nations',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('latitude', models.FloatField(default=0.0, verbose_name='Latitude')),
                ('longitude', models.FloatField(default=0.0, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('lawn_care', 'Lawn Care'), ('disinfestations', 'Disinfestations'), ('swimming_pools', 'Company specializing in swimming pools'), ('electrician', 'Electrician'), ('carpentry', 'Carpentry'), ('foundation', 'Foundation'), ('roofing', 'Roof installation and repair'), ('home_inspection', 'Home inspection'), ('plumbing', 'Plumbing work'), ('landscaping', 'Landscaping'), ('floors', 'Floors'), ('garage_doors', 'Garage Doors'), ('window_cleaning', 'Window Cleaning'), ('carpet_cleaning', 'Carpet cleaning'), ('pool_cleaning', 'Swimming pool cleaning'), ('house_cleaning', 'House cleaning'), ('fences', 'Fences'), ('appliance_repairs', 'Household appliance repairs'), ('hvac', 'Heating and Air Conditioning'), ('coatings', 'Coatings'), ('worktop_installation', 'Worktop installation services'), ('snow_removal', 'Snow removal services'), ('tree_services', 'Tree Services'), ('water_damage', 'Water damage services'), ('window_services', 'Window services'), ('procurement', 'Procurement service'), ('waste_disposal', 'Waste disposal'), ('removals', 'Removals'), ('handyman', 'Handyman')], max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectors',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images', verbose_name='Avatar')),
                ('bio', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Bio')),
                ('birth_date', models.DateTimeField(blank=True, null=True, verbose_name='Birth Date')),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='City')),
                ('street', models.CharField(blank=True, max_length=64, null=True, verbose_name='Street')),
                ('CAP', models.CharField(blank=True, max_length=64, null=True, verbose_name='CAP')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='Phone Number')),
                ('is_platform', models.BooleanField(default=True, verbose_name='Is Platform')),
                ('is_business', models.BooleanField(default=False, verbose_name='Is Business')),
                ('is_buyer', models.BooleanField(default=False, verbose_name='Is Buyer')),
                ('is_owner', models.BooleanField(default=False, verbose_name='Is Owner')),
                ('iva', models.CharField(default='0000', max_length=32, verbose_name='IVA')),
                ('business', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.business', verbose_name='Business')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metropolitan_city_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='Metropolitan City Code')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('automotive_acronym', models.CharField(max_length=3, verbose_name='Automotive Acronym')),
                ('latitude', models.FloatField(default=0.0, verbose_name='Latitude')),
                ('longitude', models.FloatField(default=0.0, verbose_name='Longitude')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province_region', to='dashboard.region', verbose_name='Region')),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('is_capital_province', models.BooleanField(default=False, verbose_name='Is Capital Province')),
                ('cadastral_code', models.CharField(max_length=4, verbose_name='Cadastral Code')),
                ('latitude', models.FloatField(default=0.0, verbose_name='Latitude')),
                ('longitude', models.FloatField(default=0.0, verbose_name='Longitude')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipality_province', to='dashboard.province', verbose_name='Province')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipality_region', to='dashboard.region', verbose_name='Region')),
            ],
            options={
                'verbose_name': 'Municipality',
                'verbose_name_plural': 'Municipalities',
            },
        ),
        migrations.AddField(
            model_name='business',
            name='region',
            field=models.ForeignKey(help_text='Select your region.', on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='dashboard.region', verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='business',
            name='sectors',
            field=models.ManyToManyField(help_text='Select the sectors relevant to this business.', related_name='profile_businesses', to='dashboard.sector', verbose_name='Sectors'),
        ),
        migrations.CreateModel(
            name='ProfileBusiness',
            fields=[
                ('business_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.business')),
                ('number_job_request_desidered_per_week', models.IntegerField(default=0, verbose_name='Number Job Request Desidered Per Week')),
                ('have_office_shop_to_receive_customers', models.BooleanField(default=False, verbose_name='Have Office Shop To Receive Customers')),
                ('status', models.CharField(default='inactive', max_length=50, verbose_name='Status')),
                ('code', models.CharField(default='HREMFSD', max_length=50, unique=True, verbose_name='Code')),
                ('unique_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Company Invitation URL')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_businesses', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('user_ower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_registered', to=settings.AUTH_USER_MODEL, verbose_name='User Registered')),
            ],
            options={
                'verbose_name': 'ProfileBusiness',
                'verbose_name_plural': 'ProfileBusinesses',
            },
            bases=('dashboard.business',),
        ),
    ]
