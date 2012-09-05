import json
import logging

from tornado.web import Application
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

from world import World
from player import Player
from util import RegisterCallBackMixin

def not_implemented_func(*args, **kwargs):
    raise NotImplementedError

class Connection(WebSocketHandler, RegisterCallBackMixin):
    def __init__(self, application, request, **kwargs):
        WebSocketHandler.__init__(self, application, request, **kwargs)
        self.login = False

    def initialize(self, gameserver):
        gameserver.on_connect(self)

    @property
    def id(self):
        return id(self)

    def send(self, message):
        self.write_message(json.dumps(message))

    def open(self):
        self.connect_callback()

    def on_message(self, msg):
        msg = json.loads(msg)
        self.message_callback(msg)

    def on_close(self):
        self.close_callback()

class GameServer(object):
    def __init__(self):
        self.worlds = []
        for i in xrange(3):
            world = World('world%d' %i, self)
            world.run()
            self.worlds.append(world)
        application = Application([
            ('/', Connection, {'gameserver': self}),
        ])
        http_server = HTTPServer(application)
        http_server.listen(8000)

    def on_connect(self, connection):
        world = self.worlds[0]  # TODO
        world.on_player_connect(Player(connection, world))

    def start(self):
        IOLoop.instance().start()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    server = GameServer()
    server.start()
