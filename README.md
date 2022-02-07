Displays QRcode for devices (phones, tablets) to quickly connect to a wifi network. 

Code is quick and dirty but works.

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
 
To maybe do someday:
 - Add some try excepts and error messages if it cannot connect to the internet or network.
 - Add more data or other data screens with additonal network info?
