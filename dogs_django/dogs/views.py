from rest_framework.viewsets import ModelViewSet
from django.db.models import Avg, Count
from dogs.models import Dog, Breed
from dogs.serializers import BreedSerializer, DogDetailSerializer, DogListSerializer


class DogViewSet(ModelViewSet):
    """ViewSet для модели собаки."""
    queryset = Dog.objects.all()

    def get_serializer_class(self):
        """Определяет, какой сериализатор использовать в зависимости от действия."""
        if self.action == 'retrieve':
            return DogDetailSerializer
        return DogListSerializer

    def get_queryset(self):
        """Получает queryset с аннотациями для списка и детального запроса.

        Returns:
            QuerySet: Отфильтрованный queryset с добавленными полями breed_avg_age или breed_count.
        """
        if self.action == 'list':
            return Dog.objects.annotate(breed_avg_age=Avg('breed__dog__age'))
        elif self.action == 'retrieve':
            return Dog.objects.annotate(breed_count=Count('breed__dog'))
        return super().get_queryset()

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
        )
