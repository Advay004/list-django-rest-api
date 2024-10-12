from rest_framework import serializers
from .models import Drinkm

class Drinkserializer(serializers.ModelSerializer):
    class Meta:
        model=Drinkm
        fields="__all__"