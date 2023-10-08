from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"genero", views.GeneroSerializer)
router.register(r"director", views.AutorSerializer)
router.register(r"pelicula", views.PeliculaSerializer)
router.register(r"actor", views.PeliculaSerializer)

urlpatterns = [
    path("peliculaByGenero/<int:idGenero>", views.peliculaByGenero, name='peliculaByGenero'),
    path("", include(router.urls))
]