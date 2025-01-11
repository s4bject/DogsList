from rest_framework.viewsets import ModelViewSet
from django.db.models import Avg, Count
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer


class DogViewSet(ModelViewSet):
    """ViewSet для модели собаки."""
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        """Получает queryset с дополнительной аннотацией для подсчета количества собак в породах.

        Returns:
            QuerySet: Отфильтрованный queryset с добавленным полем breed_count.
        """
        return Dog.objects.annotate(
            breed_count=Count('breed__dog')
        )


class BreedViewSet(ModelViewSet):
    """ViewSet для модели породы."""
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_queryset(self):
        """Получает queryset с дополнительной аннотацией для подсчета количества собак в породах
        и вычисления среднего возраста.

        Returns:
            QuerySet: Отфильтрованный queryset с добавленными полями dog_count и average_age.
        """
        return Breed.objects.annotate(
            dog_count=Count('dog'),
            average_age=Avg('dog__age')
        )
