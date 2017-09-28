from point import Point

class Robot(Point):

    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Action not allowed')

    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Action not allowed')

    def move_left(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Action not allowed')

    def move_right(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Action not allowed')
