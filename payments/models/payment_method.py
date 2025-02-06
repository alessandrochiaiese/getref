# models.py
from django.db import models  
from django.contrib.auth.models import User  # Presupponiamo che tu stia usando il modello User di default per il cliente
from django.utils.translation import gettext_lazy as _

class PaymentMethod(models.Model): 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} - {self.description}'

    class Meta:
        db_table = 'my_payment_methods'
        verbose_name = 'MyPaymentMethod'
        verbose_name_plural = 'MyPaymentMethods'
