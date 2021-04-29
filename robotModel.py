# Constants
BOUNDARY = 5
DIRECTIONS = [ 'EAST', 'SOUTH', 'WEST', 'NORTH' ]
POSITION_INCREATMENTS = [ [1,0], [0,-1], [-1,0], [0,1] ]


class RobotModel(object):
    def __init__(self):
        self.isPlaced = False

    def place(self, x, y, f):
        if type(x) is int and type(y) is int and self.isValidPosition(x, y) and f in DIRECTIONS:
            self.direction = DIRECTIONS.index(f)
            self.x = x
            self.y = y
            self.isPlaced = True

    def move(self):
        if self.isPlaced:
            nextX = self.x + POSITION_INCREATMENTS[self.direction][0]
            nextY = self.y + POSITION_INCREATMENTS[self.direction][1]
            if self.isValidPosition(nextX, nextY):
                self.x = nextX
                self.y = nextY

    def turnLeft(self):
        if self.isPlaced:
            self.direction = (self.direction +3) %4

    def turnRight(self):
        if self.isPlaced:
            self.direction = (self.direction +1) %4

    def report(self):
        if self.isPlaced:
            return (self.x, self.y, DIRECTIONS[self.direction])
        return None

    @staticmethod
    def isValidPosition(x, y):
        return 0 <= x and x < BOUNDARY and 0 <= y and y < BOUNDARY
