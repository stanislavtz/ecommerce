from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    cart_items = models.CharField(max_length=1000)
    amount_total = models.CharField(max_length=10)

    def __str__(self):
        return self.name + "'s order."