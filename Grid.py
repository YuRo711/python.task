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
