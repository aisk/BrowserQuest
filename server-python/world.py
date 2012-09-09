import logging
from tornado.ioloop import IOLoop
from tornado.ioloop import PeriodicCallback

from stage import Stage

class World(object):
    def __init__(self, id, wsserver):
        self.id = id
        self.server = wsserver
        self.groups = {}
        self.outgoing_queues = []#[[1,5780,'huk',44,212,80], [1,5780,'huk',44,212,80]]
        self.connect_callback = self.on_player_connect
        self.enter_callback = self.on_player_enter

    def on_player_connect(self, player):
        pass

    def on_player_enter(self, player):
        logging.info('%s is joined %s' %(player.name, self.id))
        @player.register_callback('broadcastzone_callback')
        def on_broadcast_to_zone(msg, ignore_self):
            ignored_players = [player.id] if ignore_self else []
            #self.push_to_group(player.group, msg, ignored_players)


    def process_queues(self):
        if not IOLoop.instance().running():
            return
        while self.outgoing_queues:
            self.server.send(self.outgoing_queues.pop())

    def push_to_player(self): pass

    def push_to_group(self, group_id, msg, ignored_players):
        group = self.groups.get(group_id)
        if group:
            (self.push_to_player(player) for player in group.players if player.id not in ignored_players)
        else:
            logging.error('group id: %s is not a valid group')

    def run(self, map_file_path):
        stage = Stage(map_file_path)


        PeriodicCallback(self.process_queues(), 1000)
