from twitter import *
import socket
import struct
import os
from time import strftime
from time import sleep

##########################################
# be sure to `pip install Twitter` first #
##########################################

# Add your stuff hurr
OAUTH_TOKEN = ""
OAUTH_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
mcip = "mau5ville.com"
port = 25565

# Setup
magic = "\xFE"
time = strftime("%H:%M:%S")
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))


while 1:
    # Determine whether the server is up or down
    try:
    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((mcip, port))
        s.send(magic)
        data = s.recv(1024)
        s.close()
        print data
    except Exception, e:
        print e
    sleep(60)