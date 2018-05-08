from point2d import Point2D
from aabb import AABB
from p5 import *


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
        self.__n_east = QuadTree(AABB(x + half_w, y, half_w, half_h))
        self.__s_west = QuadTree(AABB(x, y + half_h, half_w, half_h))
        self.__s_east = QuadTree(AABB(x + half_w, y + half_h, half_w, half_h))

        for pt in self.__points:
            self.__n_west.insert(pt)
            self.__n_east.insert(pt)
            self.__s_west.insert(pt)
            self.__s_east.insert(pt)

        self.__points = []

    def query(self, b: AABB):
        points = []
        if not self.__boundary.intersects(b):
            return points

        for pt in self.__points:
            if b.contains(pt):
                points.append(pt)

        if self.__n_west is None:
            return points

        points.append(self.__n_east.query(b))
        points.append(self.__n_west.query(b))
        points.append(self.__s_east.query(b))
        points.append(self.__s_west.query(b))

        return points

    def get_all(self):
        points = []
        for pt in self.__points:
            points.append(pt)

        if self.__n_west is not None:
            points.append(self.__n_east.get_all())
            points.append(self.__n_west.get_all())
            points.append(self.__s_east.get_all())
            points.append(self.__s_west.get_all())

        return points

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


if __name__ == "__main__":

    q = QuadTree(AABB(0, 0, 10, 10))
    q.insert(Point2D(1, 1))

    pts = q.query(AABB(0, 0, 1, 1))
    for pt in pts:
        print(str(pt))


    def setup():
        size(1000, 1000)
        background(0)


    try:
        run()
    except:
        pass