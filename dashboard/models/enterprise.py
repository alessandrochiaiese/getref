from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Sector(models.Model):
    SECTOR_CHOICES = [
        ('lawn_care', 'Lawn Care'),
        ('disinfestations', 'Disinfestations'),
        ('swimming_pools', 'Company specializing in swimming pools'),
        ('electrician', 'Electrician'),
        ('carpentry', 'Carpentry'),
        ('foundation', 'Foundation'),
        ('roofing', 'Roof installation and repair'),
        ('home_inspection', 'Home inspection'),
        ('plumbing', 'Plumbing work'),
        ('landscaping', 'Landscaping'),
        ('floors', 'Floors'),
        ('garage_doors', 'Garage Doors'),
        ('window_cleaning', 'Window Cleaning'),
        ('carpet_cleaning', 'Carpet cleaning'),
        ('pool_cleaning', 'Swimming pool cleaning'),
        ('house_cleaning', 'House cleaning'),
        ('fences', 'Fences'),
        ('appliance_repairs', 'Household appliance repairs'),
        ('hvac', 'Heating and Air Conditioning'),
        ('coatings', 'Coatings'),
        ('worktop_installation', 'Worktop installation services'),
        ('snow_removal', 'Snow removal services'),
        ('tree_services', 'Tree Services'),
        ('water_damage', 'Water damage services'),
        ('window_services', 'Window services'),
        ('procurement', 'Procurement service'),
        ('waste_disposal', 'Waste disposal'),
        ('removals', 'Removals'),
        ('handyman', 'Handyman'),
    ]

    name = models.CharField(max_length=100, unique=True, choices=SECTOR_CHOICES)

    def get_name_display(self):
        return self.name
    
    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors" 

class ProfileBusiness(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name=_("User"), related_name='profile_businesses')
    number_job_request_desidered_per_week = models.IntegerField(default=0, verbose_name=_("Number Job Request Desidered Per Week"))
    have_office_shop_to_receive_customers = models.BooleanField(default=False, verbose_name=_("Have Office Shop To Receive Customers"))
    link_google_maps = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Link Google Maps"))
    contact_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Conctac Number"))
    chamber_commerce_certificate = models.ImageField(
        default='default.jpg', 
        upload_to='chamber_commerce_certificates', 
        help_text="Upload your chamber of commerce certificate.",
        verbose_name=_("Chamber Commerce Certificate")
    )
    insurance_policy_certificate = models.FileField(
        default='default.jpg', 
        upload_to='insurance_policy_certificates', 
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        help_text="Only image or PDF files are allowed.",
        verbose_name=_("Insurance Policy Certificate")
    )
    region = models.ForeignKey(
        'Region', 
        related_name="regions", 
        on_delete=models.CASCADE, 
        help_text="Select your region.",
        verbose_name=_("Region")
    )
    sectors = models.ManyToManyField(
        'Sector',
        related_name="profile_businesses",
        help_text="Select the sectors relevant to this business.",
        verbose_name=_("Sectors")
    )
    holder = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Holder"))
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Company Name"))
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name=_("Email"))

    def __str__(self):
        return self.company_name or "Profile Business"

    class Meta:
        verbose_name = "ProfileBusiness"
        verbose_name_plural = "ProfileBusinesses" 