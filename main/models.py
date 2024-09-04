from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(auto_now_add=True)
    description = models.TextField()


# Create your models here.
