import util, random
from tweeter import t

def send(id):
    message = util.get_message('messages/new.txt')        
    user = t.users.show(user_id=id)
    message.replace("SCREENNAME", user['screen_name'])
    t.tweet(message)

