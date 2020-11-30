

class Player():
    _id = 0
    def __init__(self, name):
        self.name = name
        Player._id += 1
        self.id = Player._id
