from rest_framework.viewsets import ModelViewSet
from django.db.models import Avg, Count
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        return Dog.objects.annotate(
            breed_count=Count('breed__dog')
        )


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_queryset(self):
        return Breed.objects.annotate(
            dog_count=Count('dog'),
            average_age=Avg('dog__age')
        )
