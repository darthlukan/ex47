class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
        
class Weapons(object):

    def __init__(self, name):
        self.name = name
        self.weapon_list = {}
        
    def weapon_list(self, weapons):
        self.weapons.update(weapons)
