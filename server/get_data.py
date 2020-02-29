import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from pprint import pprint

# Load env file and env vars
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
# init the spotipy client 
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# NOTE; we need to diversify these lists 
# Populate list of playlists to get data from:
# global top 50, today's top hits, canada top 50 (these are all the same songs...)
# playlists = ['37i9dQZEVXbMDoHDwVN2tF', '37i9dQZF1DXcBWIGoYBM5M', '37i9dQZEVXbKj23U1GF4IR']
# global top 50, old school metal
playlists = ['37i9dQZEVXbMDoHDwVN2tF', '37i9dQZF1DX2LTcinqsO68']

def get_tracks(playlists):
    '''
    Input: list of playlist ids 
    Output: set track_ids 
    '''
    # use a set to avoid duplicate ids
    tracks = set() 
    offset = 0 
    for pl_id in playlists:
        p = []
        while True:
            response = sp.playlist_tracks(pl_id,
                                  offset=offset,
                                  fields='items.track.id,total')
            for track in response['items']:
                tracks.add(track['track']['id'])
            offset = offset + len(response['items'])
            if len(response['items']) == 0:
                break
    
    return tracks

def get_audio_features(tracks):
    '''
    Input: set of playlist ids 
    Output: list of dicts of audio_features 
    '''    
    # format: {'p_id': [{audio_features}]}
    audio_features = dict()
    for track in tracks: 
        # pprint(a_f)
        audio_features[track] = sp.audio_features(track)
    return audio_features

def get_popularity(audio_features_dict): 
    '''
    Input: audio_features_dict
    Output: audio_features_dict with popularity score
    '''    
    new_a_f_dict = audio_features_dict
    for track_id in audio_features_dict.keys(): 
        popularity = (sp.track(track_id))['popularity']
        new_a_f_dict[track_id].append({'popularity': popularity}) 
    # Format {track_id: [{audio_features}, {popularity}]}
    return new_a_f_dict

def get_data(): 
    tracks = get_tracks(playlists)
    audio_features = get_audio_features(tracks)
    data = get_popularity(audio_features)
    pprint(data)
    return data

get_data()