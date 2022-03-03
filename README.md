Displays QRcode for devices (phones, tablets) to quickly connect to a wifi network. 
Written for/tested on Circuity Python 7.1

Code is quick and dirty but works. Currently assumes WPA/2 network. 

Also displays the following optional values:
 - ssid 
 - password
 - internet IP (uses https://ifconfig.co to get the internet IP)
 - magtag IP

Required Libraries:
 - adafruit_bitmap_font
 - adafruit_display_text
 - adafruit_magtag
 - adafruit_portalbase
 - adafruit_fakerequests
 - adafruit_miniqr
 - adafruit_pixelbuf
 - adafruit_requests
 - neopixel
 - simpleio
 
Requires following fonts in /fonts/ 
 - Arial-Bold-12.pcf
 - Arial-12.bdf
 or sub you own in following adafruit instructions for font prep https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display/convert-to-pcf).

secrets.py file should be populated with wifi info.

To MAYBE do someday:
 - Add some try excepts and error messages if it cannot connect to the internet or network.
 - Add more data or other data screens with additonal network info(ip/cidr/subnetmask,gateway,channel, secuity mode)? 
 - Add options for open networks and non-wpa/2 networks. 
 - Use another file or source for network info aside from secrets.py, to possibly display one network and use another.
