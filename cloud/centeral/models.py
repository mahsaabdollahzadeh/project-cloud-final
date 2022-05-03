from django.db import models

# Create your models here.
class airfield(models.Model):
    city_name = models.CharField(max_length=300)
    airfield_name = models.CharField(max_length=300)

class airplane(models.Model):
    plane = models.CharField(max_length=300)
    capacity = models.IntegerField()

class transport(models.Model) :
    company = models.CharField(max_length=300)
    rank = models.IntegerField()

class centeral(models.Model):
    city_origin = models.CharField(max_length=300)
    airfield_origin = models.CharField(max_length=300)
    destination_city = models.CharField(max_length=300)
    destination_airport = models.CharField(max_length=300)
    datetime = models.DateTimeField()
    price = models.FloatField()
    transport = models.CharField(max_length=300)
    centeral_class = models.CharField(max_length=300)
    airplane_type = models.CharField(max_length=300)
    reserved = models.IntegerField()
