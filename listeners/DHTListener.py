import time
import urllib2
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 18)
    data = "temperature=%.1f&humidity=%.1f" % (temperature, humidity)
    urllib2.urlopen('http://sh.zark.in/dht/set?' + data)
    time.sleep(2)
