from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from dogs.models import Dog, Breed


class DogSerializer(ModelSerializer):
    breed_count = SerializerMethodField()
    breed_name = SerializerMethodField()

    class Meta:
        model = Dog
        fields = '__all__'

    def get_breed_count(self, obj):
        return getattr(obj, 'breed_count', 0)

    def get_breed_name(self,obj):
        return obj.breed.name if obj.breed else None



class BreedSerializer(ModelSerializer):
    dog_count = SerializerMethodField()
    average_age = SerializerMethodField()

    class Meta:
        model = Breed
        fields = '__all__'

    def get_dog_count(self, obj):
        return getattr(obj, 'dog_count', 0)

    def get_average_age(self, obj):
        return getattr(obj, 'average_age', None)
