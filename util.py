import random

def get_message(filename):
    messages = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            messages.append(line.strip()[:140])
    return random.choice(messages)
