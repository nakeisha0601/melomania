# Generated by Django 3.1.1 on 2020-09-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melomaniapp', '0004_auto_20200910_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analisis_Cancion',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('conteo_general', models.SmallIntegerField()),
                ('conteo_clave', models.SmallIntegerField()),
                ('densidad_lexica', models.FloatField()),
                ('indice_emocion', models.FloatField()),
                ('emocion_combinada', models.CharField(max_length=6)),
                ('indice_melodia', models.FloatField()),
                ('emocion_melodia', models.CharField(max_length=6)),
                ('indice_letra', models.FloatField()),
                ('emocion_letra', models.CharField(max_length=6)),
                ('top_palabras', models.TextField()),
                ('cancion_id', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('spotify_id', models.CharField(max_length=30)),
                ('artista_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artistas_Genero',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('genero_id', models.CharField(max_length=10)),
                ('artista_id', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Canciones_Album',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('album_id', models.CharField(max_length=22)),
                ('cancion_id', models.CharField(max_length=22)),
                ('track_number', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Canciones_Artista',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('cancion_id', models.CharField(max_length=22)),
                ('artista_id', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Canciones_Playlist',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('playlist_id', models.CharField(max_length=22)),
                ('cancion_id', models.CharField(max_length=22)),
                ('seccion_name', models.CharField(max_length=100)),
                ('position', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emocion_Basica',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('emocion_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emocion_Combinada',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('emocion_name', models.CharField(max_length=50)),
                ('emocion_letra', models.CharField(max_length=6)),
                ('emocion_melodia', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Emociones_Artista',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('artista_id', models.CharField(max_length=22)),
                ('emocion_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('genero_name', models.CharField(max_length=100)),
                ('popularidad', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Metadatos_Album',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('album_id', models.CharField(max_length=22)),
                ('energy', models.FloatField()),
                ('valence', models.FloatField()),
                ('acousticness', models.FloatField()),
                ('danceability', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('liveness', models.FloatField()),
                ('loudness', models.FloatField()),
                ('speechiness', models.FloatField()),
                ('key', models.SmallIntegerField()),
                ('mode', models.SmallIntegerField()),
                ('tempo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Metadatos_Artista',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('artista_id', models.CharField(max_length=22)),
                ('energy', models.FloatField()),
                ('valence', models.FloatField()),
                ('acousticness', models.FloatField()),
                ('danceability', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('liveness', models.FloatField()),
                ('loudness', models.FloatField()),
                ('speechiness', models.FloatField()),
                ('key', models.SmallIntegerField()),
                ('mode', models.SmallIntegerField()),
                ('tempo', models.FloatField()),
                ('densidad_lexica', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Metadatos_Cancion',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('cancion_id', models.CharField(max_length=22)),
                ('energy', models.FloatField()),
                ('valence', models.FloatField()),
                ('acousticness', models.FloatField()),
                ('danceability', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('liveness', models.FloatField()),
                ('loudness', models.FloatField()),
                ('speechiness', models.FloatField()),
                ('key', models.SmallIntegerField()),
                ('mode', models.SmallIntegerField()),
                ('tempo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('spotify_id', models.CharField(max_length=30)),
                ('playlist_name', models.CharField(max_length=100)),
                ('imagen_url', models.CharField(max_length=100)),
                ('usuario_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Rastreador_Emocional',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('week_number', models.PositiveSmallIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('usuario_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('spotify_id', models.CharField(max_length=30)),
                ('display_name', models.CharField(max_length=50)),
                ('ponderacion_letra', models.IntegerField()),
                ('ponderacion_melodia', models.IntegerField()),
            ],
        ),
        
    ]