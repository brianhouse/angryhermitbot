import util
from tweeter import t
from housepy import config, log

def send(id):
    message = util.get_message('messages/new.txt')        
    user = t.users.show(user_id=id)
    message = message.replace("SCREENNAME", user['screen_name'])
    log.info("Sending %s" % message)    
    t.statuses.update(status=message)
