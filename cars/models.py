from typing_extensions import Self
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100,primary_key=True)

class Trim(models.Model):
    name = models.CharField(max_length=30)

class FuelType(models.Model):
    name = models.CharField(max_length=30,primary_key=True)

class Make(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    parent = models.ForeignKey(Self,on_delete=models.SET_NULL)
    country = models.ForeignKey(Country,on_delete=models.PROTECT)
    us_domestic = models.BooleanField(default=False)

class Model(models.Model):
    name = models.CharField(max_length=100)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    available_trims = models.ManyToManyField(Trim)
    fuel_types = models.ManyToManyField(FuelType)

class Vehicles(models.Model):
    model = models.ForeignKey(Model,on_delete=models.PROTECT)
    friendly_name = models.CharField("Name",max_length=50)
    tank_size = models.DecimalField(decimal_places=3,blank=True,null=True)
    battery_size = models.DecimalField(blank=True,null=True)