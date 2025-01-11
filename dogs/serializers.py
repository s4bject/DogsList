from rest_framework.serializers import ModelSerializer, ValidationError

from dogs.models import Dog, Breed


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

    def validate_data(self, value):
        if value < 1 or value > 5:
            raise ValidationError("Некорректное значение")
        return value
