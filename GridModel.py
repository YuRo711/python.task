from Graph import *
from enum import Enum
from Logger import *


class GridModel:

    class Colors(Enum):
        player1 = 0
        player2 = 1
        default = -1

    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.last_changed_points_count = 0
        self.last_step_loops = []
        self.total_loops = []
        self.taken = {GridModel.Colors.player1: [], GridModel.Colors.player2: []}
        self.logger = Logger()
        self.logger.write(self.grid, self.total_loops)

    @staticmethod
    def from_int_grid(int_grid):
        height = len(int_grid)
        width = len(int_grid[0])
        grid = [[GridModel.Colors.default] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                grid[i][j] = GridModel.Colors(int_grid[i][j])
        return GridModel(grid)

    @property
    def graph(self):
        return Graph(self)

    def count_points(self, color):
        result = sum(line.count(color) for line in self.grid)
        return result

    def update(self, line, cell):
        color = self.grid[line][cell]
        self.last_changed_points_count = 0
        for i, j in self.filling_points(line, cell):
            if self.grid[i][j] != color:
                self.last_changed_points_count += 1
            self.grid[i][j] = color
        self.logger.write(self.grid, self.last_step_loops)
        # self.graph = Graph(self)

    def filling_points(self, line, cell):
        points = set()
        loops = self.loops(line, cell)
        self.last_step_loops = loops
        self.total_loops.append(loops)
        for i in range(self.height):
            for j in range(self.width):
                for loop in loops:
                    point = self.node(i, j)
                    color = GridModel.Colors.default
                    if self.grid[i][j] != -1:
                        color = GridModel.Colors.player1 if self.grid[i][j] == 1 else GridModel.Colors.player2
                    if loop.is_point_inside(point):
                        if color != GridModel.Colors.default:
                            if not (point in self.taken[color]):
                                self.taken[color].append(point)
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
                if self.is_valid_node(new_i, new_j) and not (dx == dy == 0):
                    if self.grid[i][j] == self.grid[new_i][new_j] and self.grid[i][j] != self.Colors.default:
                        adjoining_nodes.add(self.node(new_i, new_j))
        return adjoining_nodes

    def is_valid_node(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    @staticmethod
    def node(x, y):
        return tuple([x, y])
