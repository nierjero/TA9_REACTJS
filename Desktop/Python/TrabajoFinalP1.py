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
    ultimateplaylist = []
    artistas = {}
    the_goat = []

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
        
    def Its_a_Match(playlist_data,playlist_data2) :
        for track in playlist_data :
            for track2 in playlist_data2 :
                    if track == track2  :
                        match.append(track)
        return match
        
    def Ultimate_Playlist(playlist_data,playlist_data2,playlist_data3):
        for track in playlist_data :
            for track2 in playlist_data2 :
                for track3 in playlist_data3 :
                    if track == track2 and track == track3 :
                        ultimateplaylist.append(track)
        return ultimateplaylist
    
    def The_Artist():
        for diccionarios in playlist_data  : 
            artistas[artist_name]+=1
      
        #for diccionarios2 in playlist_data2  :  
        #for diccionarios3 in playlist_data3  :
                    
        return artistas
    
    #El influnecer (determinar cual playlist tiene las canciones que más aparecen en las otras)
    #El detergente (tiene más canciones diferentes, unicas y detergentes)

    #for clave in playlist_data:

        #print(clave,"\n")
    return playlist_data

playlist_link = "https://open.spotify.com/playlist/6Rm1YAUHyFt3qRjFH6cU5F?si=fd741035d8114407"
playlist_link2 = "https://open.spotify.com/playlist/0D92dR5Z6TAqoqpzsrpQtB?si=e45b517c2433440f"
playlist_link3 = "https://open.spotify.com/playlist/065YLddu0SdgGUSgw4II8O?si=babe47b22c6a4a5f"
get_playlist_tracks(playlist_link)