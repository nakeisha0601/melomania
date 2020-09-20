#Este codigo sirve para obtener la letra de una cancion que busques
import requests
import json
from bs4 import BeautifulSoup
import re
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


GENIUS_CLIENT_ACCESS_TOKEN = "8eAjAn5HIlVC38jGEtDUma9g3zmbcV70fXBvapk3R4gQVmehJujM67GQ6x7V8JH9"
GENIUS_BASE_URI = "https://api.genius.com"
SPOTIFY_CLIENT_ID = 'c7946ec1c2fd46508feee5dfbae0f7e2'
SPOTIFY_CLIENT_SECRET = '63a58449e703486881c2d86e4dd11f9f'



def get_spotify_data(cancion, artista):
    client_credentials = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret= SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials)
    consulta = sp.search(q = cancion +' '+ artista, type='track')['tracks']['items'][0]
    spotify_id = consulta['id']
    cancion_name = consulta['name']
    spotify_album_id = consulta['album']['id']
    album_name = consulta['album']['name']
    image_url = consulta['album']['images'][0]['url']
    album_type = consulta['album']['album_type']
    release_date = consulta['album']['release_date']
    spotify_artista_id = consulta['artists'][0]['id']
    artista_name = consulta['artists'][0]['name']
    duration_ms = consulta['duration_ms']

    cancion = {'spotify_id': spotify_id, 'cancion_name': cancion_name, 'album_id': spotify_album_id, 
    'album_name': album_name, 'image_url': image_url, 'album_type': album_type, 'release_date': release_date, 
    'artista_id': spotify_artista_id, 'artista_name': artista_name, 'duration_ms': duration_ms,
    'letra_url': None, 'letra_completa': None }
    
    return cancion

def _get(path, data=None, headers=None):
    url = '/'.join([GENIUS_BASE_URI, path])
    token = "Bearer {}".format(GENIUS_CLIENT_ACCESS_TOKEN)

    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}
    response = requests.get(url=url, data=data, headers=headers)
    response.raise_for_status()

    return response.json()

def get_song_lyrics(cancion, artista):

    data = {'q': cancion + artista}
    path = "search"
    response = _get(path=path, data=data, headers=None)
    song_info = []
    songs = []
    for hit in response['response']['hits']:
        if artista.lower() in hit['result']['primary_artist']['name'].lower():
            song_info.append(hit)

    for song in song_info:
                if (len(songs) < 1):
                    url = song['result']['url']
                    songs.append(url)                  
    return songs[0]

def scrape_song_lyrics(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser') 
    raw_lyrics = None
     
    while raw_lyrics is None:
        raw_lyrics = soup.find("div", {"class": "lyrics"})
        #Si el metodo find() devuelve None, no se puede utilizar get_text()
    lyrics = raw_lyrics.get_text()

    #Se quitan los identificadores como chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    #Hacemos que los \n se muestren como saltos de linea
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
     
    return lyrics
