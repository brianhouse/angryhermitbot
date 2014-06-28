#!/usr/bin/env python3

import json
from housepy import config, log
from twitter import Twitter, OAuth

t = Twitter(auth=OAuth(config['twitter']['access_token'], config['twitter']['access_token_secret'], config['twitter']['consumer_key'], config['twitter']['consumer_secret']))
try:
    result = t.followers.ids(screen_name="angryhermitbot")
except Exception as e:
    log.debug(log.exc(e))
    exit()
current_ids = result['ids']


past_ids = []
with open('followers.txt', 'r') as f:
    for line in f.readlines():
        past_ids.append(int(line.strip()))
new_ids = list(set(current_ids) - set(past_ids))
exit_ids = list(set(past_ids) - set(current_ids))
persisting_ids = list(set(current_ids) - set(new_ids))


# debug
ids = {'new_ids': new_ids, 'exit_ids': exit_ids, 'persisting_ids': persisting_ids}
print(json.dumps(ids, indent=4))




with open('followers.txt', 'w') as f:
    for id in (new_ids + persisting_ids):
        f.write("%s\n" % id)
