from django.db import models
from django.contrib.postgres.fields import ArrayField


class Pizza(models.Model):
    pizza_id = models.IntegerField(primary_key=True, unique=True, null=False)
    pizza_name = models.CharField(unique=True, null=False, max_length=30)
    pizza_price = models.FloatField(unique=False, null=False)
    pizza_ingredients = models.ArrayField(CharField(max_length=100,null=False))
