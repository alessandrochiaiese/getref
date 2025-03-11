from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=100, unique=True)
    stripe_coupon_id = models.CharField(max_length=100)
    percent_off = models.IntegerField()
    duration = models.CharField(max_length=10)
