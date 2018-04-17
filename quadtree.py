from point_2d import Point_2D

class AABB:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def contains(self, point: Point_2D):
        if not typeof(point, Point_2D):
            return False

        return self.x <= point.x and point.x <= self.x + self.w and self.y <= point.y and point.y <= self.y + self.h
