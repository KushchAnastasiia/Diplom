from django.db import models
from .Manufacturer import Manufacturer
from .SubGroup import SubGroup
from .Type import Type


class Equipment(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(db_index=True, default=0, decimal_places=3, max_digits=10)
    currency = models.CharField(max_length=16)
    guarantee = models.DecimalField(db_index=True, default=0, decimal_places=3, max_digits=10)
    in_case = models.BooleanField(db_index=True, default=False)

    manufacture = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE
    )

    type_of = models.ForeignKey(
        to=Type, on_delete=models.CASCADE
    )

    subgroup = models.ForeignKey(
        to=SubGroup, on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to='equipment/%Y/%m/%d/', null=True, blank=True, max_length=512)
    # image_path = models.CharField(max_length=256, required=False)
    # image_name = models.CharField(max_length=256, required=False)
    # image_type = models.CharField(max_length=64, required=False)

    def __str__(self):
        return f'{self.name}'
