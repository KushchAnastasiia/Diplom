from rest_framework import serializers
from .models import FeaturedEquipment


class FeaturedEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedEquipment
        fields = '__all__'
