from Graph import Graph


class Grid:
    default_color_value = -1

    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.graph = Graph(self)
        # не работает
        self.update_occurred = False
        self.updated_points = set()
        #

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
    def update(self, x, y):
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
    def filling_points(loops):
        points = set()
        for loop in loops:
            points.union(loop.filling_points)
        return points
    #
