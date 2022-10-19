from dataclasses import field
from rest_framework import serializers
from .models.modelPlatillos import platillos

class PlatillosSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=False)

    class Meta:
        model=platillos
        fields="__all__"