import time
import supervisor
import alarm
import json
import wifi
from adafruit_magtag.magtag import MagTag
from secrets import secrets

#Show additional netwwork information: internet IP and MagTag IP
showMoreNetinfo = True
#show the SSID and Password on display. 
showSSID = True
showPass = True

magtag = MagTag()

#Put the WiFi info from secrets into a bytearry to made into a QR code. 
wifiqrdata = b"WIFI:T:WPA;S:"+secrets['ssid']+";P:"+secrets['password']+";;"

xPos = 120 #so we can have these all line up nicely and move together for tweaks. 
#Title/header
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(xPos, 10),
)
#ssid
magtag.add_text(
    text_font="/fonts/Arial-12.bdf",
    text_position=(xPos, 30),
)
#password
magtag.add_text(
    text_font="/fonts/Arial-12.bdf",
    text_position=(xPos, 50),
)
#Internet info header
magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(xPos, 70),
)
#internet IP
magtag.add_text(
    text_font="/fonts/Arial-12.bdf",
    text_position=(xPos, 90),
)
#Device IP:
magtag.add_text(
    text_font="/fonts/Arial-12.bdf",
    text_position=(xPos, 110),
)

if showMoreNetinfo:
    magtag.url='http://ifconfig.co/json'
    rawData = json.loads(magtag.fetch(auto_refresh=False))

#QR code and wifi info:
magtag.graphics.qrcode(wifiqrdata, qr_size=4, x=4, y=4)
if showSSID or showPass:
    magtag.set_text('Wifi Info:',0,False)
else:
    magtag.set_text('<-- Scan to join wifi',0,False)
if showSSID:
    magtag.set_text('SSID : ' +secrets['ssid'],1,False)
else:
    magtag.set_text('',1,False)
if showPass:
    magtag.set_text('Pass : ' + secrets['password'],2,False) 
else: 
    magtag.set_text('',2,False)

#extra network info here.
if showMoreNetinfo:
    magtag.set_text('Network info:',3,False)
    magtag.set_text('inet IP: '+rawData['ip'],4,False)
    magtag.set_text('my IP:' + str(wifi.radio.ipv4_address),5,False)

#Update the display.
magtag.refresh()

time.sleep(2) # let screen update

#wait a long time and update.
#really you should just turn the thing off after runs/updates. 
#maybe switch to a button alarm to update? 
magtag.exit_and_deep_sleep(1000000)
