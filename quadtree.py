from aabb import AABB


class QuadTree:
    def __init__(self, b, max_points=4):
        self.__boundary = b
        self.__max_points = max_points
        self.__n_west = None
        self.__s_west = None
        self.__n_east = None
        self.__s_east = None
        self.__points = []

    # Split quadtree into 4 quadrants and set children
    def split(self):
        half_w = self.__boundary.w / 2
        half_h = self.__boundary.h / 2
        x, y = self.__boundary.x, self.__boundary.y
        self.__n_west = QuadTree(AABB(x, y, half_w, half_h))
        self.__n_east = QuadTree(AABB(x + half_w, y, half_w, half_h))
        self.__s_west = QuadTree(AABB(x, y + half_h, half_w, half_h))
        self.__s_east = QuadTree(AABB(x + half_w, y + half_h, half_w, half_h))

    # Search region bounded by an AABB and return points
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
            points.extend(self.__n_east.get_all())
            points.extend(self.__n_west.get_all())
            points.extend(self.__s_east.get_all())
            points.extend(self.__s_west.get_all())

        return points

    def get_points(self):
        return self.__points

    # Insert point recursively into the QuadTree. Splits if __max_points is exceeded
    def insert(self, pt):
        if self.__boundary.contains(pt):
            if self.__n_west is None and len(self.__points) < self.__max_points:
                self.__points.append(pt)
                return True
            else:
                if len(self.__points) >= self.__max_points:

                    self.split()

                    for p in self.__points:
                        self.__n_west.insert(p)
                        self.__n_east.insert(p)
                        self.__s_west.insert(p)
                        self.__s_east.insert(p)
                    self.__points = []

                self.__n_west.insert(pt)
                self.__n_east.insert(pt)
                self.__s_west.insert(pt)
                self.__s_east.insert(pt)

                return True
        else:
            return False

    def get_boundary(self):
        return self.__boundary

    def get_children(self):
        return self.__n_west, self.__n_east, self.__s_west, self.__s_east
