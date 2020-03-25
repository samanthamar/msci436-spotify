Python3 Package Requirements 
- Listed in `requirements.txt` 
- To install these packages, run: `pip3 install -r requirements.txt`

To run server: `python3 app.py` 
To run the frontend: `npm start` 

Note for local dev:
- Need to provide a dotenv in /server with the client_id and client_secret (ask Sam)

Routes: 
- Get prediction: `http://127.0.0.1:5000/predict`

Demo Data 
- Use the CLI tool in `/demo` 
- `python3 demo.py <track_id>` 
- Returns audio features and popularity given a track id