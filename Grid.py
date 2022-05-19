from Graph import *


class Grid:
    default_color_value = -1

    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.graph = Graph(self)

    def update(self, line, cell):
        color = self.grid[line][cell]
        for i, j in self.filling_points(line, cell):
            self.grid[i][j] = color

    def filling_points(self, line, cell):
        points = []
        loops = self.loops(line, cell)
        for i in range(self.height):
            for j in range(self.width):
                for loop in loops:
                    point = self.node(i, j)
                    if loop.is_point_inside(point):
                        points.append(self.node(i, j))
        return points

    def loops(self, line, cell):
        loops = self.graph.find_loops(self.node(line, cell))
        return loops

    def find_loops_edges(self, x, y):
        loops_edges = [edge for loop in self.loops(x, y) for edge in loop.edges]
        return loops_edges

    def get_adjoining_nodes(self, i, j):
        adjoining_nodes = set()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_i = i + dx
                new_j = j + dy
                if self.is_valid_node(new_i, new_j) \
                        and not (dx == dy == 0) \
                        and self.grid[i][j] == self.grid[new_i][new_j] \
                        and self.grid[i][j] != self.default_color_value:
                    adjoining_nodes.add(self.node(new_i, new_j))
        return adjoining_nodes

    def is_valid_node(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    @staticmethod
    def node(x, y):
        return tuple([x, y])







    # не работает

    def update0(self, x, y):
        loops = self.loops(x, y)
        filling_points = self.filling_points(loops)
        color_value = self.grid[x][y]
        for i, j in filling_points:
            if self.grid[i, j] != color_value:
                self.grid[i, j] = color_value
                self.updated_points.add(self.node(i, j))
                self.update_occurred = True
        if self.update_occurred:
            self.graph = Graph(self)

    @staticmethod
    def filling_points_0(loops):
        points = set()
        for loop in loops:
            points.union(loop.filling_points)
        return points
    #
    # не надо

    def find_point_outside_polygon(self, point, polygon):
        for contour_point in self.contour:
            if contour_point not in polygon:
                return contour_point
        else:
            return None

    @property
    def contour(self):
        contour = [[0, j] for j in range(self.width)] \
                  + [[i, self.width - 1] for i in range(self.height)] \
                  + [[self.height - 1, j] for j in range(self.width, -1, -1)] \
                  + [[i, 0] for i in range(self.height, -1, -1)]
        return contour
