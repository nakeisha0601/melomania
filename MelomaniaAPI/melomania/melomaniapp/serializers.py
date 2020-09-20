from rest_framework import serializers
from .models import (Cancion, Album, Artista, Genero, Emocion_Basica,Emocion_Combinada,
Playlist,Usuario,Artistas_Genero,Analisis_Cancion,Canciones_Album,Canciones_Artista,
Canciones_Playlist,Emociones_Artista,Metadatos_Album,Metadatos_Cancion,Metadatos_Artista,Rastreador_Emocional)

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class EmocionBasicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emocion_Basica
        fields = '__all__'

class EmocionCombinadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emocion_Combinada
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ArtistasGeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artistas_Genero
        fields = ['genero_id', 'artista_id']

class AnalisisCancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analisis_Cancion
        fields = '__all__'

class CancionesAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canciones_Album
        fields = '__all__'

class CancionesArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canciones_Artista
        fields = '__all__'

class CancionesPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canciones_Playlist
        fields = '__all__'

class EmocionesArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emociones_Artista
        fields = '__all__'

class MetadatosAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadatos_Album
        fields = '__all__'

class MetadatosArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadatos_Artista
        fields = '__all__'

class MetadatosCancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadatos_Cancion
        fields = '__all__'

class RastreadorEmocionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rastreador_Emocional
        fields = '__all__'

class SearchSerializer(serializers.Serializer):
    spotify_id = serializers.CharField()
    cancion_name = serializers.CharField()
    album_id = serializers.CharField()
    album_name = serializers.CharField()
    image_url = serializers.CharField()
    album_type = serializers.CharField()
    release_date = serializers.DateField()
    artista_id = serializers.CharField()
    artista_name = serializers.CharField()
    duration_ms = serializers.IntegerField()
    letra_url = serializers.CharField()
    letra_completa = serializers.CharField()
    """
    def create(self, validated_data):
        artista_spotify_id = validated_data['artista_id']
        artista_name = validated_data['artista_name']
        artista_dict = {'id': 1, 'spotify_id': artista_spotify_id, 'artista_name': artista_name}
        artista = Artista.objects.create(**artista_dict)
        album_spotify_id = validated_data['album_id']
        album_name = validated_data['album_name']
        image_url = validated_data['image_url']
        artista_id =
    """    