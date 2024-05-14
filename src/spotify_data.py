import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import config


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.CLIENT_ID,
                                                           client_secret=config.CLIENT_SECRET))

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def extract_track_data(tracks):
    track_data = []
    for item in tracks:
        track = item['track']
        track_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'popularity': track['popularity'],
            'duration_ms': track['duration_ms']
        }
        track_data.append(track_info)
    return pd.DataFrame(track_data)


playlist_id = '555WmBTB8tro8uiOiqm3ap'
tracks = get_playlist_tracks(playlist_id)
track_df = extract_track_data(tracks)
track_df.to_csv('spotify_tracks.csv', index=False)
