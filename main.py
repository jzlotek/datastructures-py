if __name__ == "__main__":
    import p5_vis
    import random
    import datetime
    from p5 import *
    from aabb import AABB
    from point2d import Point2D
    from quadtree import QuadTree

    q = QuadTree(AABB(0, 0, 1000, 1000))

    random.seed(datetime.datetime.now().utcoffset())

    vis_qt = p5_vis.VisQuadTree(q)

    for x in range(0, 100000):
        p = Point2D(random.gauss(500, 100), random.gauss(500, 100))
        q.insert(p)


    def setup():
        vis_qt.setup()


    run(sketch_draw=vis_qt.draw())

    print(len(q.get_all()))
