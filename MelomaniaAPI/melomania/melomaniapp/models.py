from django.db import models

# Create your models here.

class Cancion(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    spotify_id = models.CharField(max_length=30)
    cancion_name = models.CharField(max_length=100)
    album_id = models.CharField(max_length=22)
    release_date = models.DateField()
    duration_ms = models.IntegerField()
    letra_url = models.CharField(max_length=100)
    letra_completa = models.TextField()

    def __str__(self):
        return self.cancion_name

class Album(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    spotify_id = models.CharField(max_length=30)
    album_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    artista_id = models.CharField(max_length=22)

    def __str__(self):
        return self.album_name

class Artista(models.Model):
    id =  models.CharField(max_length=22, primary_key=True)
    spotify_id = models.CharField(max_length=30)
    artista_name = models.CharField(max_length=100)

    def __str__(self):
        return self.artista_name

class Genero(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    genero_name = models.CharField(max_length=100)
    popularidad = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.genero_name

class Emocion_Basica(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    emocion_name = models.CharField(max_length=50)

    def __str__(self):
        return self.emocion_name

class Emocion_Combinada(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    emocion_name = models.CharField(max_length=50)
    emocion_letra = models.CharField(max_length=6)
    emocion_melodia = models.CharField(max_length=6)

    def __str__(self):
        return self.emocion_name

class Playlist(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    spotify_id = models.CharField(max_length=30)
    playlist_name = models.CharField(max_length=100)
    imagen_url = models.CharField(max_length=100)
    usuario_id = models.UUIDField()

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True)
    spotify_id = models.CharField(max_length=30)
    display_name = models.CharField(max_length=50)
    ponderacion_letra = models.IntegerField()
    ponderacion_melodia = models.IntegerField()

class Artistas_Genero(models.Model):
    id = models.BinaryField(max_length=16, primary_key=True)
    genero_id = models.CharField(max_length=10)
    artista_id = models.CharField(max_length=22)

class Analisis_Cancion(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    conteo_general = models.SmallIntegerField()
    conteo_clave = models.SmallIntegerField()
    densidad_lexica = models.FloatField()
    indice_emocion = models.FloatField()
    emocion_combinada = models.CharField(max_length=6)
    indice_melodia = models.FloatField()
    emocion_melodia = models.CharField(max_length=6)
    indice_letra = models.FloatField()
    emocion_letra = models.CharField(max_length=6)
    top_palabras = models.TextField()
    cancion_id = models.CharField(max_length=22)

class Canciones_Album(models.Model):
    id = models.UUIDField(primary_key=True)
    album_id = models.CharField(max_length=22)
    cancion_id = models.CharField(max_length=22)
    track_number = models.SmallIntegerField()

class Canciones_Artista(models.Model):
    id = models.UUIDField(primary_key=True)
    cancion_id = models.CharField(max_length=22)
    artista_id = models.CharField(max_length=22)

class Canciones_Playlist(models.Model):
    id = models.UUIDField(primary_key=True)
    playlist_id = models.CharField(max_length=22)
    cancion_id = models.CharField(max_length=22)
    seccion_name = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField()

class Emociones_Artista(models.Model):
    id = models.UUIDField(primary_key=True)
    artista_id = models.CharField(max_length=22)
    emocion_id = models.CharField(max_length=6)

class Metadatos_Album(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    album_id = models.CharField(max_length=22)
    energy = models.FloatField()
    valence = models.FloatField()
    acousticness = models.FloatField()
    danceability = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    speechiness = models.FloatField()
    key = models.SmallIntegerField()
    mode = models.SmallIntegerField()
    tempo = models.FloatField()

class Metadatos_Artista(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    artista_id = models.CharField(max_length=22)
    energy = models.FloatField()
    valence = models.FloatField()
    acousticness = models.FloatField()
    danceability = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    speechiness = models.FloatField()
    key = models.SmallIntegerField()
    mode = models.SmallIntegerField()
    tempo = models.FloatField()
    densidad_lexica = models.FloatField()

class Metadatos_Cancion(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    cancion_id = models.CharField(max_length=22)
    energy = models.FloatField()
    valence = models.FloatField()
    acousticness = models.FloatField()
    danceability = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    speechiness = models.FloatField()
    key = models.SmallIntegerField()
    mode = models.SmallIntegerField()
    tempo = models.FloatField()
    
class Rastreador_Emocional(models.Model):
    id = models.UUIDField(primary_key=True)
    week_number = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    usuario_id = models.UUIDField()