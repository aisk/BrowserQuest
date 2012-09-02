from tornado.ioloop import IOLoop
from tornado.ioloop import PeriodicCallback

class World(object):
    def __init__(self, id, wsserver):
        self.id = id
        self.server = wsserver
        self.outgoing_queues = []#[[1,5780,'huk',44,212,80], [1,5780,'huk',44,212,80]]

    def on_player_connect(self, player):
        pass

    def on_player_enter(self, player):
        pass

    def process_queues(self):
        if not IOLoop.instance().running():
            print 'not running!'
            return
        while self.outgoing_queues:
            self.server.send(self.outgoing_queues.pop())

    def run(self):
        PeriodicCallback(self.process_queues(), 1000)
