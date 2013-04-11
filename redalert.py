from twitter import *
import socket
import struct
import os
from time import strftime
from time import sleep
from config import *

##########################################
# be sure to `pip install twitter` first #
##########################################

# Add your stuff in config.py

# Setup
magic = "\xFE"
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))


while 1:
    # Determine whether the server is up or down
    try:      
        time = strftime("%H:%M:%S")
        # Connect to server
    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # actually connect to server
        s.connect((mcip, port))
        # Send the magic code
        s.send(magic)
        # Open our present
        data = s.recv(1024)
        # Bye!
        s.close()
        # server is running fine! print MOTD 
        print str(time) + " > " + data
        # caching
        down = False
    except Exception, e:
        down = True
        # assume server is down
        time = strftime("%H:%M:%S")
        # Log
        print str(time) + " > " + str(e)
        # If the server is down
        if down:
            if DM_ME:
                # Send DM
                t.direct_messages.new(user=DM_USER,text="Oh no, the server is down!")
            if TWEET_DOWNTIME:
                # Send tweet
                t.statuses.update(status="[AutoTweet] The server is down as of " + time + ". :(")
        # caching
        down = True
    sleep(interval)