from django.db import models
from .Country import Country


class Manufacturer(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    description = models.TextField()
    country = models.ForeignKey(
        to=Country, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='manufacture/%Y/%m/%d/', null=True, blank=True, max_length=512)
    # image_path = models.CharField(max_length=256, required=False)
    # image_name = models.CharField(max_length=256, required=False)
    # image_type = models.CharField(max_length=64, required=False)

    def __str__(self):
        return f'{self.name}'
