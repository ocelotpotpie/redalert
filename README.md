#redalert
Tweet if your minecraft server is down, optionally DM you.

## Quick setup
	sudo pip install Twitter
	cd /dir/for/this/
	git init 
	git remote add origin https://github.com/savi3000/redalert.git 
	git pull origin master 
	nano config.py

## Usage
    Edit config.py to your liking
    chmod a+x redalert.py
    python -B redalert.py

## Making the twitter app

* Sign into [the twitter app portal](https://dev.twitter.com/apps/new) and make a new app, call it whatever you want.
* Generate yourself an OAuth token.
* Fill in all the proper info in config.py
* Make sure you have "Read, Write and Access direct messages" enabled