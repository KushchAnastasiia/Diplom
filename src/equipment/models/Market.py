from django.db import models


class Market(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    url = models.CharField(max_length=256)
    location = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name}'
