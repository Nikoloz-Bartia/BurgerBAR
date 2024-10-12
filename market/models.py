from django.db import models

class BurgerList(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.CharField(max_length=1000)
    description = models.TextField(default="No description")

    class Meta:
        verbose_name_plural = 'Burger List'

    def __str__(self):
        return self.name
    

class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    payment_method = models.CharField(max_length=10, choices=[('cash', 'Cash'), ('card', 'Card')])

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
