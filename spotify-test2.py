import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys
import json


client_id='00a9dbf9b38c43cab7af45948c50bffd'
client_secret='b5169129acbb4ad1b574ffd2e113c1f0'
scope = 'user-library-read user-read-currently-playing user-read-playback-state'
username = '11128384099'
redirect_uri = 'http://localhost/'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    track = sp.current_user_playing_track()
    trackname = track["item"]["name"]

    print(trackname)
    lengthTrackName = len(trackname)
    print(lengthTrackName)
    splitTrackName = trackname.split()
    #print(splitTrackName)

    newList = []

    if lengthTrackName > 16:
        print("Longer")
        list1 = list(trackname)
        splitTrackName
        for words in splitTrackName:
            print(words)
            lenWords = len(words)
            if lenWords < 16:
                pass
                            
    


else:
    print("Can't get token for", username)