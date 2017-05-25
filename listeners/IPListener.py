import socket
import urllib2

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
ipAddr = s.getsockname()[0]
s.close()

urllib2.urlopen('http://sh.zark.in/config/setremote?value=' + ipAddr)
