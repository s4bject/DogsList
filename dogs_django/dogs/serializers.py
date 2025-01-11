from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from dogs.models import Dog, Breed


class DogSerializer(ModelSerializer):
    """Сериализатор для модели собаки."""
    breed_count = SerializerMethodField()
    breed_name = SerializerMethodField()

    class Meta:
        model = Dog
        fields = '__all__'

    def get_breed_count(self, obj):
        """Получает количество собак в породе.

        Args:
            obj (Dog): Экземпляр модели собаки.

        Returns:
            int: Количество собак в породе.
        """
        return getattr(obj, 'breed_count', 0)

    def get_breed_name(self, obj):
        """Получает название породы собаки.

        Args:
            obj (Dog): Экземпляр модели собаки.

        Returns:
            str: Название породы собаки или None, если порода не указана.
        """
        return obj.breed.name if obj.breed else None


class BreedSerializer(ModelSerializer):
    """Сериализатор для модели породы."""
    dog_count = SerializerMethodField()
    average_age = SerializerMethodField()

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

    def get_average_age(self, obj):
        """Получает средний возраст собак в породе.

        Args:
            obj (Breed): Экземпляр модели породы.

        Returns:
            float: Средний возраст собак в породе или None, если информация отсутствует.
        """
        return getattr(obj, 'average_age', None)
