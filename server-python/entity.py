

class Entity(object):
    def __init__(self, id, type, kind, x, y):
        self.id = id
        self.type = type
        self.kind = kind
        self.x = x
        self.y = y

    def destroy(self):
        pass

    def _get_base_state(self):
        return (self.id, self.kind, self.x, self.y)

    def get_state(self):
        return self._get_base_state()

    def spawn(self):
        pass #TODO

    def despawn(self):
        pass #TODO

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position_nextto(entity):
        pass  #TODO
