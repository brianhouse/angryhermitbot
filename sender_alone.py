import random, util
from tweeter import t

def send():
    if random.random() < (1/288) * 3:
        message = util.get_message('messages/alone.txt')
        log.info("Sending \"%s\"" % message)
        t.statuses.update(status=message)
