# Test playground for functions
if __name__ == "__main__":
    import p5_vis
    import random
    import datetime
    from p5 import *
    from aabb import AABB
    from point2d import Point2D
    from quadtree import QuadTree

    # 1000 x 1000 QuadTree
    q = QuadTree(AABB(0, 0, 1000, 1000))

    random.seed(datetime.datetime.now().utcoffset())

    vis_qt = p5_vis.VisQuadTree(q)
    # Insert 100000 points into QuadTree with gaussian distribution
    for x in range(0, 100000):
        p = Point2D(random.gauss(500, 100), random.gauss(500, 100))
        q.insert(p)

    # p5py setup function
    def setup():
        vis_qt.setup()

    # p5py run function
    run(sketch_draw=vis_qt.draw())

    pts = q.get_all()

    xtotal = 0
    ytotal = 0
    for pt in pts:
        xtotal += pt.x
        ytotal += pt.y

    print(xtotal/len(pts))
    print(ytotal/len(pts))
