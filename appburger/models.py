from django.db import models

# Create your models here.

class BurgerBuy(models.Model):
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)

