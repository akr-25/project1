from django.db import models
from django.contrib.auth.models import User


class Items(models.Model):
    category = models.CharField(max_length = 1000)
    name =  models.CharField(max_length = 1000)
    price = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    image = models.ImageField()


