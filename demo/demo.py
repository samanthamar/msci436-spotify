"""
This CLI tool gets the audio features and popularity given a trackId 
"""

import spotipy
import os
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load env file and env vars
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
# init the spotipy client 
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# senorita = '0TK2YIli7K1leLovkQiNik'

def get_data(track_id): 
    data = dict()
    # First get the audio features
    keys_to_remove = ['id', 'track_href', 'type', 'uri', 'analysis_url']
    a_f = (sp.audio_features(track_id))[0]
    # remove unneeded features 
    for key in keys_to_remove:
        a_f.pop(key)
    data[track_id] = {'audio_features': a_f}
    # Now get the popularity 
    popularity = (sp.track(track_id))['popularity']
    data['popularity'] = popularity
    return data 
    

# Creating the CLI 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("track_id", help="input track id of song", type=str)
args = parser.parse_args()
if args.track_id:
    pprint.pprint(get_data(args.track_id))
parser.parse_args()