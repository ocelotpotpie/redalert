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

print "\n"
print "########################################"
print "# savi's server downtime tweeter thing #"
print "########################################"
print "\n"

# assume server is up
down = False
while 1:
    # Determine whether the server is up or down
    try:      
        time = strftime("%H:%M")
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
        alreadyTweeted = False
    except Exception, e:
        # server must be down
        time = strftime("%H:%M")
        # Log
        print str(time) + " > " + str(e)
        down = True
        # If the server is down
        if down and not alreadyTweeted:
            if DM_ME:
                # Send DM
                t.direct_messages.new(user=DM_USER,text="Hey, " + SERVER_NAME + " is down!")
            if TWEET_DOWNTIME:
                # Send tweet
                t.statuses.update(status=PREFIX + " The server is down as of " + time + " EST. :(")
                alreadyTweeted = True
    sleep(interval)