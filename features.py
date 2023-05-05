import spotipy
import cred
from spotipy.oauth2 import SpotifyClientCredentials
import appendCSV as acsv

#Extracting features from track using urls
# url = 'https://open.spotify.com/album/0aIy6J8M9yHTnjtRu81Nr9'
# url = 'https://open.spotify.com/album/40jLpWdeDFnV2ir6Su8HGT'
# url = 'https://open.spotify.com/track/1PZZtXR7nsNIyRcqd7UeiF'

def extract_features(url):
    #establishing connection with API
    auth_manager = SpotifyClientCredentials(client_id = cred.client_ID, client_secret = cred.client_SECRET)
    sp = spotipy.Spotify(auth_manager = auth_manager)
    category = url.split('/')[-2]
    id = url.split('/')[-1]
    exdict = ["popularity","duration_ms","explicit","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"]
    allfeat = dict()
    if category == 'track':
        tid = id
        tr = sp.track(tid)
        features = sp.audio_features(tid)[0]
        for (key,value) in features.items():
            for i in exdict:
                if key == i:
                    allfeat[key] = value
                elif i == "explicit":
                    allfeat[i] = tr["explicit"]
    elif category == 'album':
        aid = id
        album = sp.album(aid)
        newid = album['tracks']['items'][0]['id']
        features = sp.audio_features(newid)[0]
        for (key,value) in features.items():
            for i in exdict:
                if key == i:
                    allfeat[key] = value
                elif i == "explicit":
                    allfeat[i] = album["tracks"]["items"][0]["explicit"]  
    # print(allfeat)
    # acsv.appendFunc(allfeat)
    return allfeat
    