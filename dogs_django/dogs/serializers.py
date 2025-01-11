from django.db.models import Avg
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from dogs.models import Dog, Breed


class DogListSerializer(ModelSerializer):
    """Сериализатор для списка собак."""
    breed_name = SerializerMethodField()
    breed_avg_age = SerializerMethodField()

    class Meta:
        model = Dog
        fields = '__all__'

    def get_breed_name(self, obj):
        """Получает название породы собаки.

        Args:
            obj (Dog): Экземпляр модели собаки.

        Returns:
            str: Название породы собаки или None, если порода не указана.
        """
        return obj.breed.name if obj.breed else None

    def get_breed_avg_age(self, obj):
        """Получает средний возраст собак в породе из аннотации для списка.

        Args:
            obj (Dog): Экземпляр модели собаки.

        Returns:
            float: Средний возраст собак в породе или None, если информация отсутствует.
        """
        return getattr(obj, 'breed_avg_age', None)

class DogDetailSerializer(ModelSerializer):
    """Сериализатор для детального запроса собаки."""
    breed_name = SerializerMethodField()
    breed_count = SerializerMethodField()

    class Meta:
        model = Dog
        fields = '__all__'

    def get_breed_name(self, obj):
        """Получает название породы собаки.

        Args:
            obj (Dog): Экземпляр модели собаки.

        Returns:
            str: Название породы собаки или None, если порода не указана.
        """
        return obj.breed.name if obj.breed else None

    def get_breed_count(self, obj):
        """Получает количество собак той же породы из аннотации для детального запроса.

        Args:
            obj (Dog): Экземпляр модели собаки.

        Returns:
            int: Количество собак той же породы или 0, если информация отсутствует.
        """
        return getattr(obj, 'breed_count', 0)



class BreedSerializer(ModelSerializer):
    """Сериализатор для модели породы."""
    dog_count = SerializerMethodField()

    class Meta:
        model = Breed
        fields = '__all__'

    def get_dog_count(self, obj):
        """Получает количество собак в породе.

        Args:
            obj (Breed): Экземпляр модели породы.

        Returns:
            int: Количество собак в породе.
        """
        return getattr(obj, 'dog_count', 0)
