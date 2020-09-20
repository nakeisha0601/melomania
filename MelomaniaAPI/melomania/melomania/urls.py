"""melomania URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from melomaniapp.views import (CancionViewSet,AlbumViewSet,GeneroViewSet,GeneroArtistasViewSet,ArtistaViewSet,
EmocionViewSet,EmocionBasicaViewSet,UsuarioViewSet,PlaylistViewSet,RastreadorViewSet,SearchViewSet)

from melomaniapp.api import CancionesAPI

router = DefaultRouter()
router.register('canciones', CancionViewSet)
router.register('albumes', AlbumViewSet)
router.register('generos', GeneroViewSet)
router.register('generos-artistas', GeneroArtistasViewSet)
router.register('artistas', ArtistaViewSet)
router.register('emociones', EmocionViewSet)
router.register('emociones-basicas', EmocionBasicaViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('playlists', PlaylistViewSet)
router.register('rastreadores', RastreadorViewSet)

playlist_users = PlaylistViewSet.as_view({
    'get': 'get_user_playlists'
})
playlist_canciones = PlaylistViewSet.as_view({
    'get': 'get_canciones'
})
genero_artistas = GeneroViewSet.as_view({
    'get': 'get_artistas'
})
rastreador_usuario = RastreadorViewSet.as_view({
    'get': 'get_user_tracker'
})
artista_emociones = ArtistaViewSet.as_view({
    'get': 'get_emociones'
})
cancion_analisis = CancionViewSet.as_view({
    'get': 'get_analisis'
    
})
cancion_metadatos = CancionViewSet.as_view({
    'get': 'get_metadatos'
})
album_metadatos = AlbumViewSet.as_view({
    'get': 'get_metadatos'
})
album_canciones = AlbumViewSet.as_view({
    'get': 'get_canciones'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    path('api/v1/generos/<str:pk>/artistas/', genero_artistas, name='genero-artistas'),
    path('api/v1/canciones/<str:pk>/analisis/', cancion_analisis, name='cancion-analisis'),
    path('api/v1/canciones/<str:pk>/metadatos/', cancion_metadatos, name='cancion-metadatos'),
    path('api/v1/albumes/<str:pk>/metadatos/', album_metadatos, name='album-metadatos'),
    path('api/v1/albumes/<str:pk>/canciones/', album_canciones, name='album-canciones'),
    path('api/v1/usuarios/<str:pk>/playlists/', playlist_users, name='playlists-user'),
    path('api/v1/artistas/<str:pk>/emociones/', artista_emociones, name='artista-emociones'),
    path('api/v1/usuarios/<str:pk>/rastreadores/', rastreador_usuario, name='rastreador-user'),
    path('api/v1/playlists/<str:pk>/canciones/', playlist_canciones, name='playlists-tracks'),
    path('api/v1/search/', SearchViewSet.as_view()),
]

  