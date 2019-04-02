from django.db import models


class FeaturedEquipment(models.Model):
    user_id = models.IntegerField(default=None, null=True, db_index=True)
    equipment_id = models.IntegerField(default=None, null=True, db_index=True)
