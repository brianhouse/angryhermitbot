import json, util, random
from housepy import config, log
from tweeter import t

def send(user_id):
    if not (random.random() < (1/288) * 5):
        return
    message = util.get_message('messages/persisting.txt')
    user = t.users.show(user_id=user_id)
    message = message.replace("SCREENNAME", user['screen_name'])
    message = message.replace("FOLLOWERS", str(user['followers_count']))
    if "HOMEPAGE" in message:
        try:
            message = message.replace("HOMEPAGE", user['entities']['url']['urls'][0]['expanded_url'])
        except IndexError as e:
            return
    log.info("Sending \"%s\"" % message)
    t.statuses.update(status=message)

if __name__ == "__main__":
    from twitter import Twitter, OAuth
    t = Twitter(auth=OAuth(config['twitter']['access_token'], config['twitter']['access_token_secret'], config['twitter']['consumer_key'], config['twitter']['consumer_secret']))
    user_id = 5452482
    send(user_id)