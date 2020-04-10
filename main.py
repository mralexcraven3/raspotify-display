import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys
import json

import numpy as np


from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime


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


    lengthTrackName = len(trackname)
    splitTrackName = trackname.split()
    #print(splitTrackName)

    if lengthTrackName > 16:
        trackname = trackname.split()
        print(trackname)
    else:
        print(trackname)


else:
    print("Can't get token for", username)

    
def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    while(True):         
        #lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
        lcd.message(trackname +'\n' )# display Track name
        #lcd.message( get_time_now() )   # display the time
        sleep(1)
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

