from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Genero
from .models import Director
from .models import Actor
from .models import Pelicula
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import GeneroSerializer, PeliculaSerializer, AutorSerializer



class GeneroSerializer( viewsets.ModelViewSet ):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class AutorSerializer( viewsets.ModelViewSet ):
    queryset = Director.objects.all()
    serializer_class = AutorSerializer

class ActorSerializer( viewsets.ModelViewSet ):
    queryset = Actor.objects.all()
    serializer_class = AutorSerializer

class PeliculaSerializer( viewsets.ModelViewSet ):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


@api_view(["GET"])
def peliculaByGenero (req, idGenero):
    try:
        # genero = req.GET.get('genero')
        peliculas = Pelicula.objects.filter( genero=idGenero)
        return JsonResponse( 
            { "cantidadPeliculas": peliculas.count() }, 
            safe=False,
            status=200 
        )
    except Exception as e:
        return JsonResponse({
            "message": "Algo salio mal"
        })