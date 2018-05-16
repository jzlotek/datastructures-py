from p5 import *
from quadtree import QuadTree


class VisQuadTree:

    def __init__(self, qt: QuadTree, scale=100):

        self.w, self.h = qt.get_boundary().w, qt.get_boundary().h
        self.qt = qt
        scaled = False

        if self.w < 100:
            self.w *= scale
            scaled = True

        if self.h < 100:
            self.h *= scale
            scaled = True

    def draw_box(self, qt):
        no_fill()
        stroke(255, 0, 0)
        rect((qt.get_boundary().x, qt.get_boundary().y), qt.get_boundary().w, qt.get_boundary().h)
        fill(0, 255, 0)
        stroke(0, 255, 0)
        if len(qt.get_points()) > 0:
            for pt in qt.get_points():
                ellipse([pt.x, pt.y], 1, 1)
        if qt.get_children()[0] is not None:
            for child in qt.get_children():
                self.draw_box(child)

    def setup(self):
        size(self.w, self.h)
        background(0, 0, 0)

    def draw(self):
        self.draw_box(self.qt)
        no_fill()
