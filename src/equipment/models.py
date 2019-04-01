from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Equipment(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    currency = models.CharField(max_length=16)
    guarantee = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    in_case = models.BooleanField(default=False)
    manufacture = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE
    )

    type = models.CharField(max_length=64)
    group = models.CharField(max_length=64)
    subgroup = models.CharField(max_length=64)

    image_path = models.CharField(max_length=256)
    image_name = models.CharField(max_length=256)
    image_type = models.CharField(max_length=64)
