from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


# Handles requests involving the collection of all Dog records.
# GET returns all dogs.
# POST validates the supplied JSON and creates a new dog.
class DogList(APIView):

    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# Handles requests involving one specific Dog record.
# GET retrieves a dog by ID.
# PUT updates a dog by ID.
# DELETE removes a dog by ID.
class DogDetail(APIView):

    # Helper method used to find the requested Dog.
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            return None

    def get(self, request, pk):
        dog = self.get_object(pk)

        if dog is None:
            return Response(
                {"error": "Dog not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk):
        dog = self.get_object(pk)

        if dog is None:
            return Response(
                {"error": "Dog not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DogSerializer(dog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        dog = self.get_object(pk)

        if dog is None:
            return Response(
                {"error": "Dog not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Handles requests involving the collection of all Breed records.
# GET returns all breeds.
# POST validates the supplied JSON and creates a new breed.
class BreedList(APIView):

    def get(self, request):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BreedSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# Handles requests involving one specific Breed record.
# GET retrieves a breed by ID.
# PUT updates a breed by ID.
# DELETE removes a breed by ID.
class BreedDetail(APIView):

    # Helper method used to find the requested Breed.
    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            return None

    def get(self, request, pk):
        breed = self.get_object(pk)

        if breed is None:
            return Response(
                {"error": "Breed not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk):
        breed = self.get_object(pk)

        if breed is None:
            return Response(
                {"error": "Breed not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BreedSerializer(breed, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        breed = self.get_object(pk)

        if breed is None:
            return Response(
                {"error": "Breed not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)