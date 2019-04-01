from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=64)


class Equipment(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=16)
    guarantee = models.IntegerField(default=0)
    in_case = models.BooleanField(default=False)

    type = models.CharField(max_length=64)
    group = models.CharField(max_length=64)
    subgroup = models.CharField(max_length=64)

    image_path = models.CharField(max_length=256)
    image_name = models.CharField(max_length=256)
    image_type = models.CharField(max_length=64)
