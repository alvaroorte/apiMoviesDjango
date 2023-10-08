from django.contrib import admin
from .models import Director
from .models import Pelicula
from .models import Genero
from .models import Actor
# Register your models here.


admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Actor)

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'genero', 'actor_principal','resumen', 'calificacion')
    ordering = ['titulo']
    search_fields = ['titulo']
admin.site.register(Pelicula, PeliculaAdmin)