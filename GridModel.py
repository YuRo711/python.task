from Graph import *
from enum import Enum


class GridModel:

    class Colors(Enum):
        player1 = 0
        player2 = 1
        default = -1

    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        # self.graph = Graph(self)
        self.last_changed_points_count = 0
        self.last_step_loops = []

    @property
    def graph(self):
        return Graph(self)

    def update(self, line, cell):
        color = self.grid[line][cell]
        self.last_changed_points_count = 0
        for i, j in self.filling_points(line, cell):
            if self.grid[i][j] != color:
                self.last_changed_points_count += 1
            self.grid[i][j] = color
        # self.graph = Graph(self)

    def filling_points(self, line, cell):
        points = set()
        loops = self.loops(line, cell)
        self.last_step_loops = loops
        for i in range(self.height):
            for j in range(self.width):
                for loop in loops:
                    point = self.node(i, j)
                    if loop.is_point_inside(point):
                        points.add(self.node(i, j))
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
                        and self.grid[i][j] != self.Colors.default:
                    adjoining_nodes.add(self.node(new_i, new_j))
        return adjoining_nodes

    def is_valid_node(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    @staticmethod
    def node(x, y):
        return tuple([x, y])
