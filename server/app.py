import pandas as pd
from flask import Flask, request 
from ANN import train, predict
from flask_cors import CORS 

app = Flask(__name__) 
CORS(app)
nn = train()

@app.route('/')
def default(): 
    return {"success": 200}

@app.route('/predict', methods=['GET'])
def predict_popularity():
    if request.method == 'GET':
        # Get features from form data 
        acousticness = request.form['acousticness']
        danceability = request.form['danceability']
        duration = request.form['duration_ms']
        energy = request.form['energy']
        instrumentalness = request.form['instrumentalness']
        key = request.form['key']
        liveness = request.form['liveness']
        loudness = request.form['loudness']
        mode = request.form['mode']
        speechiness = request.form['speechiness']
        tempo = request.form['tempo']
        time_signature = request.form['time_signature']
        valence = request.form['valence']    
        # from these features, create a pd dataframe (X) 
        # Note: remember to transpose the data
        X = pd.DataFrame([acousticness, danceability, duration, 
        energy, instrumentalness, key, 
        liveness, loudness, mode, 
        speechiness, tempo, 
        time_signature, valence]).T
        # Predict the popularity bin
        pop = predict(nn, X)
        return {"success": 200, "popularity_bin": pop}

if __name__ == '__main__':
    app.debug = True
    app.run()