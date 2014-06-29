import util
from tweeter import t
from housepy import config, log

def send(user_id):
    message = util.get_message('messages/new.txt')        
    user = t.users.show(user_id=user_id)
    message = message.replace("SCREENNAME", user['screen_name'])
    log.info("Sending \"%s\"" % message)    
    t.statuses.update(status=message)
