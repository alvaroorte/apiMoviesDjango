from rest_framework import serializers
from .models import Genero
from .models import Director
from .models import Pelicula


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = "__all__"
