#!/usr/bin/env python3

import json, os
import sender_new, sender_exit, sender_persisting
from housepy import config, log
from tweeter import t

# initialize Twitter and retrieve followers
try:
    result = t.followers.ids(screen_name="angryhermitbot")
except Exception as e:
    log.debug(log.exc(e))
    exit()
current_ids = result['ids']

# we are so happy
if not len(current_ids):
    log.info("No followers! So happy.")
    sender_alone.send()
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
#put run info into log file
log.debug(json.dumps({'new_ids': new_ids, 'exit_ids': exit_ids, 'persisting_ids': persisting_ids}, indent=4))

# send out tweets
for user_id in new_ids:
    sender_new.send(user_id)     # add try/except?
for user_id in exit_ids:
    sender_exit.send(user_id)
for user_id in persisting_ids:
    sender_persisting.send(user_id)

# save followers
with open('followers.txt', 'w') as f:
    for user_id in (new_ids + persisting_ids):
        f.write("%s\n" % user_id)
