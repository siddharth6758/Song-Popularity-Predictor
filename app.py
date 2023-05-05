from flask import Flask, request, render_template
from features import extract_features
import pickle as pk
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import spotipy
import cred
from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__)

le = LabelEncoder()
auth_manager = SpotifyClientCredentials(client_id = cred.client_ID, client_secret = cred.client_SECRET)
sp = spotipy.Spotify(auth_manager = auth_manager)
    
def preprocess(url):
    category = url.split('/')[-2]
    id = url.split('/')[-1]
    info = ['artists','album_name','track_name']
    get_info = dict()
    if category == "track":
        tid = id
        track = sp.track(tid)
        get_info = dict()
        get_info['track_name'] = track["name"]
        get_info['artists'] = track["artists"][0]["name"]
        get_info['album_name'] = track["album"]["name"] 
    elif category == "album":
        aid = id
        album = sp.album(aid)
        newid = album['tracks']['items'][0]['id']
        track = sp.track(newid)
        get_info = dict()
        get_info['track_name'] = track["name"]
        get_info['artists'] = track["artists"][0]["name"]
        get_info['album_name'] = track["album"]["name"]
        print(get_info)
    test_feat = extract_features(url)
    df = pd.DataFrame(test_feat,index=[0])
    df['explicit'] = le.fit_transform(df['explicit'])
    df = df.iloc[:,[12,0,1,2,3,4,5,6,7,8,9,10,11,13]]
    print(get_info)
    return df,test_feat,get_info
    

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit.html', methods=['POST','GET'])
def submit():
    url = request.form['url']
    test_vals,test_feat,info = preprocess(url)
    model = pk.load(open("flaskmodel.pkl","rb"))
    otp = model.predict(test_vals)
    return render_template('submit.html',popularity = otp[0],features = test_feat,info = info)

if __name__ == '__main__':
    app.run(port=5500)
