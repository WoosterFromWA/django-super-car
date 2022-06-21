from typing_extensions import Self
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100,primary_key=True)

class Trim(models.Model):
    name = models.CharField(max_length=30)

class FuelType(models.Model):
    name = models.CharField(max_length=30,primary_key=True)

class Make(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    slug = models.SlugField(editable=False,unique=True)
    parent = models.ForeignKey(Self,on_delete=models.SET_NULL)
    country = models.ForeignKey(Country,on_delete=models.PROTECT)
    us_domestic = models.BooleanField(default=False)

class Model(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(editable=False,unique=True)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    available_trims = models.ManyToManyField(Trim)
    fuel_types = models.ManyToManyField(FuelType)

class Vehicles(models.Model):
    model = models.ForeignKey(Model,on_delete=models.PROTECT)
    slug = models.SlugField(editable=False,unique=True)
    friendly_name = models.CharField("Name",max_length=50)
    tank_size = models.DecimalField(decimal_places=3,blank=True,null=True)
    battery_size = models.DecimalField(blank=True,null=True)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('vehicle_detail', kwargs=kwargs)

@receiver(pre_save, sender=Vehicles)
def set_vehicle_slug(sender,instance):
    if not instance.pk:
        instance.slug = slugify(instance.friendly_name, allow_unicode=True)