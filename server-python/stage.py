import json
import math
import logging

class Stage(object):
    def __init__(self, filepath):
        self.is_loaded = False
        try:
            stage_file = open(filepath)
            stage_data = json.loads(stage_file.read())
            self.init_stage(stage_data)
        except IOError:
            logging.error('%s doesn\'t exists' %filepath)
            return

    def init_stage(self, stage):
        self.width = stage['width']
        self.height = stage['height']
        self.collisions = stage['collisions']
        self.mobAreas = stage['roamingAreas']
        self.chestAreas = stage['chestAreas']
        self.staticChests = stage['staticChests']
        self.staticEntities = stage['staticEntities']
        self.isLoaded = True

        self.zone_width = 28
        self.zone_height = 12
        self.group_width = math.floor(self.width / self.zone_width)
        self.group_height = math.floor(self.height / self.zone_height)

        #self.ready_callback()

    def tileindex_to_gridposition(self, tile_num):
        x, y = 0, 0
        if tile_num == 0:
            x = 0
        else:
            x = (self.width-1) if (tile_num%self.width==0) else (tile_num%self.width-1)
        tile_num -= 1
        y = math.floor(tile_num / self.width)
        return {'x': x, 'y': y}


