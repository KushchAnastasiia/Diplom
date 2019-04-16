from django.db import models


class Market(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    url = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    code = models.CharField(db_index=True, max_length=16)
    
    def __str__(self):
        return f'{self.name}'


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


class Type(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    
    def __str__(self):
        return f'{self.name}'

class Group(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    
    def __str__(self):
        return f'{self.name}'


class SubGroup(models.Model):
    name = models.CharField(db_index=True, max_length=64)
    group = models.ForeignKey(
        to=Group, on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.name}'


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


class EquipmentMarketConnection(models.Model):
    equipment = models.ForeignKey(
        to=Equipment, on_delete=models.CASCADE
    )
    market = models.ForeignKey(
        to=Market, on_delete=models.CASCADE
    )
    location = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name}'
