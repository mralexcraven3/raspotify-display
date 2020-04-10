import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 11128384099
client_id='00a9dbf9b38c43cab7af45948c50bffd'
client_secret='b5169129acbb4ad1b574ffd2e113c1f0',
redirect_uri='http://raspotify-display.alexcraven.com/


#if len(sys.argv) > 1:
    #username = sys.argv[1]
#else:
    #print("Usage: %s username" % (sys.argv[0],))
    #sys.exit()

#token = util.prompt_for_user_token(username, scope)

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)