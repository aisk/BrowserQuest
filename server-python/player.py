import logging
from cgi import escape

import gametypes
import message
from character import Character
from util import register_callback

class Player(Character):
    def __init__(self, connection, world):
        connection.connect_callback = self.on_connect
        connection.message_callback = self.on_message
        connection.close_callback = self.on_close
        self.connection = connection
        self.world = world
        Character.__init__(self, connection.id, 'player', gametypes.Entities.WARRIOR, 0, 0)
        self.has_entered_game = False
        self.is_dead = False

    def send(self, msg):
        self.connection.send(msg)

    def on_connect(self):
        self.connection.write_message('go')

    @register_callback(name='message_callback')
    def on_message(self, msg):
        action = msg[0]
        logging.debug('Received: %s' %msg)

        if action == gametypes.Messages.HELLO:
            self.name = escape(msg[1][:15]) if msg[1] else 'lorem ipsum'
            self.kind = gametypes.Entities.WARRIOR
            self.equip_armor = msg[2]
            self.equip_weapon = msg[3]

            # TODO

            self.send([gametypes.Messages.WELCOME, self.id, self.name,44,212,80])

            self.has_entered_game = True
            self.is_dead = False

        if action == gametypes.Messages.CHAT:
            content = msg[1]
            if content:
                content = escape(content[:60])
                print message.Chat(self, content).serialize()

        if action == gametypes.Messages.MOVE:
            self.x = msg[1]
            self.y = msg[2]

    def on_close(self):
        pass


