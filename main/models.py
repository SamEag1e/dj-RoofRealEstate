from django.db import models


class Apartment(models.Model):
    ad_date = models.DateField()
    token = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField()
    floor_number = models.IntegerField()
    total_floors = models.IntegerField()
    msquare = models.IntegerField()
    total_price = models.BigIntegerField()
    price_per_msquare = models.BigIntegerField()
    production_year = models.IntegerField()
    rooms = models.IntegerField()
    elevator = models.BooleanField()
    parking = models.BooleanField()
    storeroom = models.BooleanField()

    def __str__(self):
        return self.token


class Villa(models.Model):
    ad_date = models.DateField()
    token = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField()
    land_msquare = models.IntegerField()
    msquare = models.IntegerField()
    total_price = models.BigIntegerField()
    price_per_msquare = models.BigIntegerField()
    production_year = models.IntegerField()
    rooms = models.IntegerField()
    storeroom = models.BooleanField()
    parking = models.BooleanField()
    balcony = models.BooleanField()

    def __str__(self):
        return self.token


class Land(models.Model):
    ad_date = models.DateField()
    token = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField()
    land_msquare = models.IntegerField()
    total_price = models.BigIntegerField()
    price_per_msquare = models.BigIntegerField()

    def __str__(self):
        return self.token
