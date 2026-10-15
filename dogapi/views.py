from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


# ViewSet that provides GET, POST, PUT, and DELETE operations
# for Dog records through the REST API.
class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


# ViewSet that provides GET, POST, PUT, and DELETE operations
# for Breed records through the REST API.
class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer