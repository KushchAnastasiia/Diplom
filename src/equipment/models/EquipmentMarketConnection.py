from django.db import models
from .Market import Market
from .Equipment import Equipment


class EquipmentMarketConnection(models.Model):
    equipment = models.ForeignKey(
        to=Equipment, on_delete=models.CASCADE
    )
    market = models.ForeignKey(
        to=Market, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.equipment.name} --> {self.market.name}'
