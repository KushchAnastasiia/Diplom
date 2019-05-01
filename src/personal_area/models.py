from django.db import models
from django.contrib.auth.models import User
from equipment.models import Equipment

class FeaturedEquipment(models.Model):
    # user_id = models.IntegerField(default=None, null=True, db_index=True)
    # equipment_id = models.IntegerField(default=None, null=True, db_index=True)

    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE
    )
    equipment_id = models.ForeignKey(
        to=Equipment, on_delete=models.CASCADE
    )
