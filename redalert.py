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

if not os.path.exists('config.py'):
    open('config.py', 'w').write(inspect.cleandoc(
        r'''
        # make a new app here: https://dev.twitter.com/apps/new
        # fill in all the data :)

        OAUTH_TOKEN = ""
        OAUTH_SECRET = ""
        CONSUMER_KEY = ""
        CONSUMER_SECRET = ""
        mcip = "yourserver.com"
        port = 25565
        ''') + '\n')

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