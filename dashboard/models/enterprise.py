from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='profile_businesses')
    number_job_request_desidered_per_week = models.IntegerField(default=0)
    have_office_shop_to_receive_customers = models.BooleanField(default=False)
    link_google_maps = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    chamber_commerce_certificate = models.ImageField(
        default='default.jpg', 
        upload_to='chamber_commerce_certificates', 
        help_text="Upload your chamber of commerce certificate."
    )
    insurance_policy_certificate = models.FileField(
        default='default.jpg', 
        upload_to='insurance_policy_certificates', 
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        help_text="Only image or PDF files are allowed."
    )
    region = models.ForeignKey(
        'Region', 
        related_name="regions", 
        on_delete=models.CASCADE, 
        help_text="Select your region."
    )
    sectors = models.ManyToManyField(
        'Sector',
        related_name="profile_businesses",
        help_text="Select the sectors relevant to this business."
    )
    holder = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.company_name or "Profile Business"

    class Meta:
        verbose_name = "ProfileBusiness"
        verbose_name_plural = "ProfileBusinesses" 