import csv
import spotipy
import os
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from pprint import pprint
import pandas as pd

# Load env file and env vars
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
# init the spotipy client 
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

albums_of_2019 = "albums_of_2019.csv"

def get_tracks_from_albums(listOfAlbums) :
    '''
    Input: listOfAlbums
    Output: set of track ids 
    '''    
    tracks = set()
    with open(listOfAlbums, newline='', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        # Reading all artists/albums in csv
        for row in csv_reader:
            # searching albums based on artist name and album name
            result = sp.search(q = 'album:'+ row[1]+ ' artist:'+ row[0], type='album')
            album_songs = []
            if result['albums']['items']:
                album_songs = sp.album_tracks(result['albums']['items'][0]['id'], limit, offset)
            if album_songs:
                for track in album_songs['items']:
                    tracks.add(track['id'])
    print("DONE GETTING TRACKS")
    return tracks

def get_audio_features(tracks):
    '''
    Input: set of playlist ids 
    Output: dict with format: {'track_id': {audio_features: {}}}
    '''    
    audio_features = dict()
    keys_to_remove = ['id', 'track_href', 'type', 'uri', 'analysis_url']
    for track_id in tracks: 
        a_f = (sp.audio_features(track_id))[0]
        # remove unneeded features 
        for key in keys_to_remove:
            a_f.pop(key)
        audio_features[track_id] = {'audio_features': a_f}
    print("Done audio features")
    return audio_features

def get_popularity(audio_features_dict): 
    '''
    Input: audio_features_dict
    Output: audio_features_dict with popularity score
    '''    
    new_a_f_dict = audio_features_dict
    for track_id in audio_features_dict.keys(): 
        popularity = (sp.track(track_id))['popularity']
        new_a_f_dict[track_id]['popularity'] = popularity
    # Format {track_id: {audio_features: {}, popularity: {}}}
    print("Popularity")
    return new_a_f_dict

def get_data_as_dict(): 
    '''
    Input: none
    Output: get all audio feature data and popularity scores as a dict 
    '''    
    tracks = get_tracks_from_albums(albums_of_2019)
    audio_features = get_audio_features(tracks)
    data = get_popularity(audio_features)
    return data

def get_data_as_csv(dict_data): 
    '''
    Input: audio features/popularity score dict 
    Output: dictionary data as csv for reusability
    ''' 
    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        # Create the headers 
        writer.writerow(['Track ID','accousticness','danceability', 'duration', 'energy', 
        'instrumentalness', 'key', 'liveness', 
        'loudness', 'mode', 
        'speechiness', 'tempo', 
        'time_signature', 'valence',
        'popularity'])
        # Write the rows 
        for track_id, data in dict_data.items(): 
            # for features
            # data.append()
            a_f = data['audio_features']
            acousticness = a_f['acousticness']
            danceability = a_f['danceability']
            duration = a_f['duration_ms']
            energy = a_f['energy']
            instrumentalness = a_f['instrumentalness']
            key = a_f['key']
            liveness = a_f['liveness']
            loudness = a_f['loudness']
            mode = a_f['mode']
            speechiness = a_f['speechiness']
            tempo = a_f['tempo']
            time_signature = a_f['time_signature']
            valence = a_f['valence']
            # append to array
            writer.writerow([track_id, acousticness, danceability, 
            duration, energy, 
            instrumentalness, key, liveness, 
            loudness, mode, 
            speechiness, tempo, 
            time_signature, valence, data['popularity']])

# NOTE: Uncomment me to execute me! 
# Only need to run once to get the csv, which we already have 
#    get_data_as_csv(get_data_as_dict())

csv_file = 'dataset.csv'
def get_df(csv_file): 
    '''
    Input: csv file with all track data 
    Output: pandas data frames for input, output 
    ''' 
    df = pd.read_csv(csv_file) 
    target_column = ['popularity']
    # Don't include track ID as a predictor 
    predictors = list(set(list(df.columns))-set(target_column) - set(['Track ID']))
    print(predictors)
    X = df[predictors].values
    Y = (df[target_column].values)
    print(Y)
    return (X, Y)

X,Y = get_df(csv_file)




