import re 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(playlist_link):

    client_id = '52bf760c5edd4c20af3151535e1be982'
    client_secret = 'cb5052bf33eb4c99ad8c76f8f39f5f99'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlist_id = re.search(r'playlist/([\w\d]+)', playlist_link).group(1)
    playlist_id2 = re.search(r'playlist/([\w\d]+)', playlist_link2).group(1)
    playlist_id3 = re.search(r'playlist/([\w\d]+)', playlist_link3).group(1)



    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    results2 = sp.playlist_tracks(playlist_id2)
    tracks2 = results2['items']
    results3 = sp.playlist_tracks(playlist_id3)
    tracks3 = results3['items']

    
    playlist_data = []
    playlist_data2 = []
    playlist_data3 = []
    match = []

    for track in tracks:
        song_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        playlist_data.append({'song': song_name, 'artist': artist_name})

    for track in tracks2:
        song_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        playlist_data2.append({'song': song_name, 'artist': artist_name})
    
    for track in tracks3:
        song_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        playlist_data3.append({'song': song_name, 'artist': artist_name})

    for track in playlist_data :
        for track3 in playlist_data3 :
            if track == track3 :
                match.append(track)
    print(match,"\n")

    #for clave in playlist_data:
        #print(clave,"\n")

    return playlist_data

playlist_link = "https://open.spotify.com/playlist/3p73OoG1M7g6P7nvvnxE9u?si=43838f58a6644185"
playlist_link2 = "https://open.spotify.com/playlist/2sp2E0AvNdTebffMc5vrI9?si=aaff9fec506843b2"
playlist_link3 = "https://open.spotify.com/playlist/6ZCBSITwjMHKRDhs82Xeoo?si=4b8e23672e85441c&nd=1"
#playlist_link4 = 
get_playlist_tracks(playlist_link)