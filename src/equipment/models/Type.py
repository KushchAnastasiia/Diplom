from django.db import models


class Type(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    
    def __str__(self):
        return f'{self.name}'
