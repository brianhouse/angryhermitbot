import random, util
from tweeter import t

def send():
    messages = util.get_message('messages/alone.txt')
    if random.random() < 1/144:
        t.statuses.update(status=random.choice(message))
