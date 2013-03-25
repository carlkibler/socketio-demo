import logging
import datetime

from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace

@namespace('')
class PingPongNamespace(BaseNamespace):

    def initialize(self):
        """
        Initialize any connection-specific data and configure a logger.
        """
        self.logger = logging.getLogger("socketio.pingpong")
        self.log("Socketio session started")

        # Django session data can be retrieved, just like a normal HTTP request
        self.remote_ip = self.request.META['REMOTE_ADDR']
        self.count = 0
        
    def log(self, message):
        """
        Simple helper function to output session-unique log messages.
        """
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))
    
    def on_ping(self, message):
        """
        Catch a 'ping' emitted by client JS code. Increment counter and reply.
        """
        now = datetime.datetime.now()
        self.log("%s - Ping %s from %s" % (now.ctime(), message,self.remote_ip))
        self.emit('pong', self.count)
        self.count += 1

    def recv_disconnect(self):
        """
        Fire on client disconnect. Just log a notice in this case.
        """
        self.log('Disconnected')
        self.disconnect(silent=True)
        return True

