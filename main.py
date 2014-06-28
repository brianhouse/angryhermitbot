#!/usr/bin/env python3

import json
from housepy import config, log
from twitter import Twitter, OAuth

t = Twitter(auth=OAuth(config['twitter']['access_token'], config['twitter']['access_token_secret'], config['twitter']['consumer_key'], config['twitter']['consumer_secret']))
result = t.followers.ids(screen_name="h0use")
print(json.dumps(result, indent=4))

