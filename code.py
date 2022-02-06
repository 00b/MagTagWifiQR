import time
import supervisor
import alarm
import json
from adafruit_magtag.magtag import MagTag
from secrets import secrets

magtag = MagTag()
magtag.url='http://ifconfig.co/json'

rawData = json.loads(magtag.fetch(auto_refresh=False))

wifiqrdata = b"WIFI:T:WPA;S:"+secrets['ssid']+";P:"+secrets['password']+";;"
magtag.graphics.qrcode(wifiqrdata, qr_size=4, x=4, y=4)
rawData = json.loads(magtag.fetch(auto_refresh=False))
print(rawData)

xPos = 120 #so we can have these all match and move together for tweaks. 
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
magtag.set_text('Wifi Info:',0,False)
magtag.set_text('ssid : '+secrets['ssid'],1,False)
magtag.set_text('pass : '+secrets['password'],2,False) 
magtag.set_text('Net info:',3,False)
magtag.set_text('inet ip: '+rawData['ip'],4,False)

magtag.refresh()

time.sleep(2) # let screen update
magtag.exit_and_deep_sleep(10000)
