from Gemini import GeminiGateway
from Spotify import SpotifyGateway
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/')
def index():
    spotify_gateway = SpotifyGateway()
    img_elements = spotify_gateway.get_covers_div()
    return f"<p>Here are your saved albums:</p> {img_elements}"


@app.route('/artist')
def artist_albums():
    search = sp.search(q='artist:Drake', type='album')

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


