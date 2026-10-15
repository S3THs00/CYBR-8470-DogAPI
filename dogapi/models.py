from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Breed model stores information about each dog breed.
class Breed(models.Model):
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(max_length=100)

    # Limits breed size to the four values required by the assignment.
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

    # These fields only accept values from 1 through 5.
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    sheddingamount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exerciseneeds = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name


# Dog model stores information about individual dogs.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    # Each dog belongs to a Breed record.
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='dogs'
    )

    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
