import json, util
from housepy import config, log
from tweeter import t

def send(id):
    user = t.users.show(user_id=id)
    print(json.dumps(user, indent=4))
    # user['screen_name']
    # user['followers_count']
    # user['entities']['url']['urls'][0]['expanded_url']

if __name__ == "__main__":
    from twitter import Twitter, OAuth
    t = Twitter(auth=OAuth(config['twitter']['access_token'], config['twitter']['access_token_secret'], config['twitter']['consumer_key'], config['twitter']['consumer_secret']))
    id = 5452482
    send(t, id)