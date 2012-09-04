
import gametypes

class Message(object):
    def serialize(self):
        raise NotImplementedError

class Spawn(Message):
    def __init__(self, entity):
        self.entity = entity
    def serialize(self):
        return [gametypes.Messages.SPAWN].extend(self.entity.get_state())

class Despawn(Message):
    def __init__(self, entity):
        self.entity = entity
    def serialize(self):
        return [gametypes.Messages.DESPAWN, self.entity.id]

class Chat(Message):
    def __init__(self, player, message):
        self.player = player
        self.message = message
    def serialize(self):
        return (gametypes.Messages.CHAT, self.player.id, self.message)
