from point import Point

class Reward(Point):

    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name

    def __str__(self):
        return '<%s, %s>: %s' % (self.x, self.y, self.name)