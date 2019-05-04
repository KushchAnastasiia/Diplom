from django.db import models


class Country(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    code = models.CharField(db_index=True, max_length=16)
    
    def __str__(self):
        return f'{self.name}'
# CharField - varchar
