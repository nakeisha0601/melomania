from rest_framework import viewsets, status, generics, renderers, views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer
from .models import (Cancion, Album, Artista, Genero, Emocion_Basica,Emocion_Combinada,
Playlist,Usuario,Artistas_Genero,Analisis_Cancion,Canciones_Album,Canciones_Artista,
Canciones_Playlist,Emociones_Artista,Metadatos_Album,Metadatos_Cancion,Metadatos_Artista,Rastreador_Emocional)

from .serializers import * 
from .analisis import search

# Create your views here.

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
   
    def get_analisis(self, request, pk=None, *args, **kwargs):
        analisis = Analisis_Cancion.objects.filter(cancion_id= pk)
        serializer = AnalisisCancionSerializer(analisis, many=True)
        return Response(serializer.data)

    def get_metadatos(self, request, pk=None, *args, **kwargs):
        metadatos = Metadatos_Cancion.objects.filter(cancion_id= pk)
        serializer = MetadatosCancionSerializer(metadatos, many=True)
        return Response(serializer.data)

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_canciones(self, request, pk=None, *args, **kwargs):
        canciones = Canciones_Album.objects.filter(album_id= pk)
        serializer = CancionesAlbumSerializer(canciones, many=True)
        return Response(serializer.data)

    def get_metadatos(self, request, pk=None, *args, **kwargs):
        metadatos = Metadatos_Album.objects.filter(album_id= pk)
        serializer = MetadatosAlbumSerializer(metadatos, many=True)
        return Response(serializer.data)

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

    def get_emociones(self, request, pk=None, *args, **kwargs):
        emociones = Emociones_Artista.objects.filter(artista_id= pk)
        serializer = EmocionesArtistaSerializer(emociones, many=True)
        return Response(serializer.data)

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

    def get_artistas(self, request, pk=None, *args, **kwargs):
        artistas = Artistas_Genero.objects.filter(genero_id= pk)
        serializer = ArtistasGeneroSerializer(artistas, many=True)
        return Response(serializer.data)

class GeneroArtistasViewSet(viewsets.ModelViewSet):
    queryset = Artistas_Genero.objects.all()
    serializer_class = ArtistasGeneroSerializer

class EmocionBasicaViewSet(viewsets.ModelViewSet):
    queryset = Emocion_Basica.objects.all()
    serializer_class = EmocionBasicaSerializer

class EmocionViewSet(viewsets.ModelViewSet):
    queryset = Emocion_Combinada.objects.all()
    serializer_class = EmocionCombinadaSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_user_palylists(self, request, pk=None, *args, **kwargs):
        playlists = Playlist.objects.filter(usuario_id=pk)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)
        
    def get_canciones(self, request, pk=None, *args, **kwargs):
        canciones = Canciones_Playlist.objects.filter(playlist_id= pk)
        serializer = CancionesPlaylistSerializer(canciones, many=True)
        return Response(serializer.data)
   

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RastreadorViewSet(viewsets.ModelViewSet):
    queryset = Rastreador_Emocional.objects.all()
    serializer_class = RastreadorEmocionalSerializer

    def get_user_tracker(self, request, pk=None, *args, **kwargs):
        rastreadores = Rastreador_Emocional.objects.filter(usuario_id = pk)
        serializer = RastreadorEmocionalSerializer(rastreadores, many=True)
        return Response(serializer.data)

class SearchViewSet(views.APIView):
    serializer_class = SearchSerializer

    def get(self, request): 
        cancion = self.request.query_params.get('cancion', None)
        artista = self.request.query_params.get('artista', None)
        letra_url = search.get_song_lyrics(cancion, artista)
        letra_completa = search.scrape_song_lyrics(letra_url)
        cancion_info = search.get_spotify_data(cancion, artista)
        cancion_info['letra_url'] = letra_url
        cancion_info['letra_completa'] = letra_completa
        serializer = SearchSerializer(cancion_info)
        return Response(serializer.data)

    def post(self, request):
        datos = request.data
        spotify_id = datos['spotify_id']
        cancion_name = datos['cancion_name']
        try:
            #Verifica si el album ya está en la base de datos
            album_id = Album.objects.get(spotify_id=datos['album_id']).id
        except Album.DoesNotExist:
            #Si no lo está se inserta 
            album_spotify_id = datos['album_id']
            album_name = datos['album_name']
            image_url = datos['image_url']
            
            try:
                #Verifica si el artista ya está en la base de datos
                artista_id = Artista.objects.get(spotify_id=datos['artista_id']).id
            except Artista.DoesNotExist:
                #Si no lo está se inserta
                artista_spotify_id = datos['artista_id']
                artista_name = datos['artista_name']

                artista_dict = {'id': 1, 'spotify_id': artista_spotify_id, 'artista_name': artista_name}
                artista = Artista.objects.create(**artista_dict)
                artista_id = Artista.objects.get(spotify_id=datos['artista_id']).id

            album_dict = {'id': 1, 'spotify_id': album_spotify_id, 'album_name': album_name, 'image_url': image_url, 'artista_id':artista_id}
            album = Album.objects.create(**album_dict)
            album_id = Album.objects.get(spotify_id=datos['album_id']).id
        release_date = datos['release_date']
        duration_ms = datos['duration_ms']
        letra_url = datos['letra_url']
        letra_completa = datos['letra_completa']

        cancion = {'id': 1, 'spotify_id': spotify_id, 'cancion_name': cancion_name, 'album_id': album_id, 'release_date': release_date,
        'duration_ms': duration_ms, 'letra_url': letra_url, 'letra_completa': letra_completa}

        serializer = CancionSerializer(data=cancion)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Consulta:
    def __init__(self, cancion, spotify_id, album_id, artista_id, artista, letra_completa, letra_url):
        self.cancion = cancion
        self.spotify_id = spotify_id
        self.album_id = album_id 
        self.artista_id = artista_id
        self.artista = artista
        self.letra_completa = letra_completa
        self.letra_url = letra_url
