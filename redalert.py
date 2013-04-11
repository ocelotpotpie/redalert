from twitter import *
import socket
import struct
import os
from time import strftime

##########################################
# be sure to `pip install Twitter` first #
##########################################

# Add your stuff hurr
OAUTH_TOKEN = ""
OAUTH_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
mcip = "mau5ville.com"
port = "25565"

# Setup
magic = "\xFE"
time = strftime("%H:%M:%S")
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# borrowed from https://gist.github.com/barneygale/1209061
def ping(host=mcip, port=port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Send 0xFE
    s.send('\xfe\x01')
    
    d = s.recv(1024)
    s.close()
    
    # Check for 0xFF
    assert d[0] == '\xff'
    
    # Remove the packet ident (0xFF) and the short containing the length of the string
    # Decode UCS-2 string
    d = d[3:].decode('utf-16be')
    
    # Check the first 3 characters of the string are what we expect
    assert d[:3] == u'\xA7\x31\x00'

    if d[:3] = u'\xA7\x31\x00':
    	up = true


while 1:
	# Determine whether the server is up or down
	ping(host=mcip, port=port)
	if up = true:
		# Alert !
		t.statuses.update(status="Server is down as of " + time)
	time.sleep(60)