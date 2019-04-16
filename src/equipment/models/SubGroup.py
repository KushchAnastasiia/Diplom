from django.db import models
from .Group import Group


class SubGroup(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}'
