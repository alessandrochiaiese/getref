# affiliate_system/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Affiliate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"), related_name='affiliate_user')
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=15, blank=True, verbose_name=_("Phone"))
    date_joined = models.DateField(verbose_name=_("Date Joined"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Earning"))
    country = models.CharField(max_length=50, verbose_name=_("Country"))
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, verbose_name=_("Profile Picture"))
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Account Balance"))
    last_login = models.DateTimeField(null=True, blank=True, verbose_name=_("Last Login"))
    referral_source = models.CharField(max_length=255, verbose_name=_("Referral Source"))

    def __str__(self):
        return f"{self.user.username} - {self.code}"

    def generate_code(self):
        self.code = get_random_string(10)
        self.save()
