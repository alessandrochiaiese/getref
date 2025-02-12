from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from PIL import Image

from referral.models.referral_transaction import ReferralTransaction
import payments
from payments.models.payment_method import PaymentMethod

#User(username, first_name, last_name, email, is_staff, is_active, date_joined)

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    # User: username, first_name, last_name, email, is_staff, is_active, date_joined
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User")) 
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', verbose_name=_("Avatar"))
    bio = models.TextField(max_length=1024, null=True, blank=True, verbose_name=_("Bio"))

    # base data profile
    birth_date = models.DateTimeField(null=True, blank=True, verbose_name=_("Birth Date"))
    city = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("City"))
    street = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Street"))
    CAP = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("CAP"))
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True, verbose_name=_("Phone Number"))

    # To use platform and allow javascript to use API
    is_platform = models.BooleanField(default=True)

    # Differenet kind of profile (Business, Buyer, Base)
    is_business = models.BooleanField(default=False, verbose_name=_("Is Business"))
    is_buyer = models.BooleanField(default=False, verbose_name=_("Is Buyer"))
    
    # business
    name_business = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("Name Business")) # nome azienda
    is_owner = models.BooleanField(default=False, verbose_name=_("Is Owner"))
    user_ower = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("User Owner"), related_name="owner_business")
    iva = models.CharField(max_length=32, default="0000", verbose_name=_("IVA"))
    office_number = models.CharField(max_length=13, blank=True, null=True, unique=True, verbose_name=_("Office Number")) 
    
    
    # buyer
    #transactions = models.ManyToManyField(ReferralTransaction, related_name='txns')
    #payment_method = models.OneToOneField(PaymentMethod, blank=True, null=True, on_delete=models.CASCADE, related_name='payment')


    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
