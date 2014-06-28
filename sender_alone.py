import random

def send(t):
    messages = []
    with open('messages/alone.txt', 'r') as f:
        for line in f.readlines():
            messages.append(line.strip()[:140])

    if random.random() < 1/144:
        t.tweet(random.choice(message))     # fix me!


