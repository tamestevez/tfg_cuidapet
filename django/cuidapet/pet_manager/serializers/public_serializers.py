from rest_framework import serializers
from pet_manager.models import Animal

class ListAdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields=[
            'id',
            'name',
            'sex',
            'image',
        ]

class AdoptionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields=[
            'id',
            'name',
            'specie',
            'sex',
            'birth_date',
            'color',
            'notable_characteristics',
            'owner',
            'ppp',
            'attitudes',
            'image',
        ]