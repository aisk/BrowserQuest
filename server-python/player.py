import logging
from cgi import escape

import gametypes
from character import Character

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

    def send(self, message):
        self.connection.send(message)

    def on_connect(self):
        self.connection.write_message('go')

    def on_message(self, message):
        action = message[0]
        logging.debug('Received: %s' %message)

        if action == gametypes.Messages.HELLO:
            self.name = escape(message[1][:15]) if message[1] else 'lorem ipsum'
            self.kind = gametypes.Entities.WARRIOR
            self.equip_armor = message[2]
            self.equip_weapon = message[3]

            # TODO

            self.send([gametypes.Messages.WELCOME, self.id, self.name,44,212,80])

            self.has_entered_game = True
            self.is_dead = False

        if action == gametypes.Messages.CHAT:
            msg = message[1]
            if msg:
                msg = escape(msg[:60])
                # TODO

        if action == gametypes.Messages.MOVE:
            self.x = message[1]
            self.y = message[2]

    def on_close(self):
        pass


