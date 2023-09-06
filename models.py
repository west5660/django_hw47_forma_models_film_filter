from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    town = models.CharField(max_length=15, null=True, blank=True)

class Car(models.Model):
    marka = models.CharField(max_length=15)
    proizv = models.CharField(max_length=15)
    age = models.IntegerField()
    gn = models.CharField(max_length=15)

class Company(models.Model):
    name = models.CharField(max_length=20)
    yeae = models.IntegerField()

class Product(models.Model):
    title=models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Film(models.Model):
    country = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    year = models.IntegerField()