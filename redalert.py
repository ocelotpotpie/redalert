from twitter import *
import socket
import struct
import os
from time import strftime
from time import sleep
from config import *

##########################################
# be sure to `pip install Twitter` first #
##########################################

# Add your stuff in config.py

# Setup
magic = "\xFE"
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))


while 1:
    # Determine whether the server is up or down
    try:      
        time = strftime("%H:%M:%S")
    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((mcip, port))
        s.send(magic)
        data = s.recv(1024)
        s.close()
        print str(time) + " > " + data
        # server is running fine! print MOTD 
    except Exception, e:
        # assume server is down
        print str(time) + " > " + str(e)
    sleep(interval)