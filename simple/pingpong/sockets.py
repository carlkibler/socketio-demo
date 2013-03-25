import logging
import datetime
import json

from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace

@namespace('')
class PingPongNamespace(BaseNamespace):

    def initialize(self):
        self.count = 0
        self.logger = logging.getLogger("socketio.pingpong")
        self.log("Socketio session started")
        self.remote_ip = self.request.META['REMOTE_ADDR']
        
    def log(self, message):
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))
    
    def on_ping(self, message):
        now = datetime.datetime.now()
        self.log("%s - Ping %s from %s" % (now.ctime(), message,self.remote_ip))
        self.emit('pong', self.count)
        self.count += 1

    def recv_disconnect(self):
        # Remove nickname from the list.
        self.log('Disconnected')
        self.disconnect(silent=True)
        return True

