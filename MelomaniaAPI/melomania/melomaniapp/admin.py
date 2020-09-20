from django.contrib import admin
from .models import Cancion, Album, Artista, Genero
# Register your models here.

admin.site.register(Cancion)
admin.site.register(Album)
admin.site.register(Artista)
admin.site.register(Genero)