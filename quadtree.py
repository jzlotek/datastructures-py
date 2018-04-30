from point2d import Point2D


class AABB:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point: Point2D):
        if not typeof(point, Point2D):
            return False

        return self.x <= point.x and point.x <= self.x + self.w and self.y <= point.y and point.y <= self.y + self.h


class QuadTree:
    def __init__(self, b, max_points=4):
        self.__boundary = b
        self.__max_points = max_points
        self.__n_west = None
        self.__s_west = None
        self.__n_east = None
        self.__s_east = None
        self.__points = []

    def split(self):
        half_w = self.__boundary.w / 2
        half_h = self.__boundary.h / 2
        x, y = self.__boundary.x, self.__boundary.y
        self.__n_west = QuadTree(AABB(x, y, half_w, half_h))
        self.__n_east = QuadTree(AABB(x+half_w, y, half_w, half_h))
        self.__s_west = QuadTree(AABB(x, y+half_h, half_w, half_h))
        self.__s_east = QuadTree(AABB(x+half_w, y+half_h, half_w, half_h))

        for pt in self.__points:
            self.__n_west.insert(pt)
            self.__n_east.insert(pt)
            self.__s_west.insert(pt)
            self.__s_east.insert(pt)

        self.__points = []


    def insert(self, pt):
        if self.__boundary.contains(pt):
            if self.__n_west is None and len(self.__points) < self.__max_points:
                self.__points.append(pt)
                return True
            else:
                if len(self.__points) >= self.__max_points:
                    self.split()
                self.__n_west.insert(pt)
                self.__n_east.insert(pt)
                self.__s_west.insert(pt)
                self.__s_east.insert(pt)
                return True
        else:
            return False


