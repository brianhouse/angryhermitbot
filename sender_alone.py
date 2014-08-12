import json, util, random
from housepy import config, log
from tweeter import t


def send():
    if not(random.random() < (1/288) * 3):
        return
    message = util.get_message('messages/alone.txt')
    log.info("Sending \"%s\"" % message)
    t.statuses.update(status=message)

if __name__ == "__main__":
    from twitter import Twitter, OAuth
    t = Twitter(auth=OAuth(config['twitter']['access_token'], config['twitter']['access_token_secret'], config['twitter']['consumer_key'], config['twitter']['consumer_secret']))
    user_id = 5452482
    send(user_id)
