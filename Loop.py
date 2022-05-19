from Grid import *


class Loop:
    def __init__(self, path):
        self.path = path

    @property
    def edges(self):
        edges = []
        for i in range(len(self.path) - 1):
            edges.append([self.path[i], self.path[i + 1]])
        return edges

    def is_point_inside(self, point):
        polygon = self.path
        outer_point = [-1, -1]
        connecting_segment = [outer_point, point]
        intersections_counter = 0
        for i in range(len(polygon) - 1):
            segment = [polygon[i], polygon[i+1]]
            intersections_counter += int(self.are_crossed(segment, connecting_segment))
        return intersections_counter % 2 == 1

    def are_crossed(self, segment1, segment2):
        line1 = self.line(*segment1)
        line2 = self.line(*segment2)
        return line1(segment2[0]) * line1(segment2[1]) < 0\
            and line2(segment1[0]) * line2(segment1[1]) < 0

    @staticmethod
    def line(point1, point2):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        a, b = dy, -dx
        return lambda point: a*(point[0] - point1[0]) + b*(point[1] - point1[1])

    @staticmethod
    def node(x, y):
        return tuple([x, y])
