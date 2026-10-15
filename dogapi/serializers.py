from rest_framework import serializers
from .models import Dog, Breed


# Converts Breed model objects to and from JSON for the API.
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds',
        ]


# Converts Dog model objects to and from JSON for the API.
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = [
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favoritefood',
            'favoritetoy',
        ]