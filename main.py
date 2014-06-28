#!/usr/bin/env python3

import json, os
import sender_new, sender_exit, sender_persisting
from housepy import config, log
from twitter import Twitter, OAuth

# initialize Twitter and retrieve followers
t = Twitter(auth=OAuth(config['twitter']['access_token'], config['twitter']['access_token_secret'], config['twitter']['consumer_key'], config['twitter']['consumer_secret']))
try:
    result = t.followers.ids(screen_name="angryhermitbot")
except Exception as e:
    log.debug(log.exc(e))
    exit()
current_ids = result['ids']

# we are so happy
if not len(current_ids):
    log.info("No followers! So happy.")
    sender_alone.send(t)
    exit()

# sort followers
past_ids = []
if os.path.isfile('followers.txt'):
    with open('followers.txt', 'r') as f:
        for line in f.readlines():
            past_ids.append(int(line.strip()))
new_ids = list(set(current_ids) - set(past_ids))
exit_ids = list(set(past_ids) - set(current_ids))
persisting_ids = list(set(current_ids) - set(new_ids))
log.debug(json.dumps({'new_ids': new_ids, 'exit_ids': exit_ids, 'persisting_ids': persisting_ids}, indent=4))

# do the thing
for id in new_ids:
    sender_new.send(id)     # add try/except?
for id in exit_ids:
    sender_exit.send(id)
for id in persisting_ids:    
    sender_persisting.send(id)

# save followers
with open('followers.txt', 'w') as f:
    for id in (new_ids + persisting_ids):
        f.write("%s\n" % id)
