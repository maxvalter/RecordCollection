from Album import Album
import spotipy
import random
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class SpotifyGateway:
    def __init__(self):
        self.scope = "user-library-read"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('client-id'), client_secret=os.getenv('client-secret'), redirect_uri="http://localhost:5000/callback"))

    def get_current_user_albums(self):
        results = self.sp.current_user_saved_albums(limit=50)
        album_objects = []

        for item in results['items']:
            genre = item['album']['genres'][0] if item['album']['genres'] else "N/A"

            album_entry = Album(item['album']['id'], 
                                item['album']['name'],
                                item['album']['images'][0]['url'], 
                                item['album']['artists'][0]['name'], 
                                item['album']['release_date'], 
                                genre)
            album_objects.append(album_entry)

        album_objects.sort(key=lambda album: album.release_date, reverse=True)
        return album_objects
    
    def get_covers_div(self):
        album_objects = self.get_current_user_albums()
        img_elements = ""
        for album in album_objects:
            img_elements += f"<img src='{album.img}' alt='{album.name}' width='100' height='100'>"
        return img_elements





