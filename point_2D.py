class Point_2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
