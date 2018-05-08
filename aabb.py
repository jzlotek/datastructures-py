from point2d import Point2D


class AABB:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point: Point2D):
        if not isinstance(point, Point2D):
            return False

        return self.x <= point.x and point.x <= self.x + self.w and self.y <= point.y and point.y <= self.y + self.h

    def intersects(self, b):
        return not (self.x + self.w < b.x or self.x > b.x + b.w or self.y + self.h < b.y or self.y > b.y + b.h)
