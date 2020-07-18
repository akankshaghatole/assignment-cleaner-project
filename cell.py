class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if (self.x < other.x):
            return True
        elif (self.x > other.x):
            return False
        elif (self.x == other.x):
            return (self.y < other.y)
            