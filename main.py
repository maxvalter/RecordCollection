import flask
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, dotenv_values

load_dotenv()
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id= os.getenv('client-id'), client_secret=os.getenv('client-secret'), redirect_uri="http://localhost:5000/callback"))

app = flask.Flask(__name__)

@app.route('/')
def index():

    results = sp.current_user_saved_albums(limit=50)
    album_objects = list(map(lambda item: [item['album']['images'][0]['url'], item['album']['release_date']], results['items']))
    album_objects.sort(key=lambda x: x[1], reverse=True)

    img_elements = list(map(lambda item: f"<img src='{item[0]}'/><a> '{item[1]}' </a>", album_objects))

    return "<p>Your record collection, sorted by time of release.</p> <a href='/about'>About</a>" + "".join(img_elements)


@app.route('/about')
def about():
    return "<p>About Page</p> <a href='/'>Home</a>"

if __name__ == '__main__':
    app.run(debug=True, port=5050)



def get_saved_tracks():
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

def get_followed_artists():
    response = sp.current_user_followed_artists()
    for item in response['artists']['items']:
        print(item['name'], item['genres'])

def get_followed_artists_images():
    response = sp.current_user_followed_artists()

    return map(lambda item: item['images'][0]['url'], response['artists']['items'])

def get_saved_albums():
    results = sp.current_user_saved_albums()
    return map(lambda item: [item['album']['images'][0]['url'], item['album']['release_date']], results['items'])

