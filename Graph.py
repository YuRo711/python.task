from Loop import Loop


class Graph:
    def __init__(self, grid):
        self.graph = Graph.convert_grid_to_graph(grid)

    @staticmethod
    def convert_grid_to_graph(grid):
        adjoining_nodes = dict()
        for i in range(grid.height):
            for j in range(grid.width):
                adjoining_nodes[Graph.node(i, j)] = grid.get_adjoining_nodes(i, j)
        return adjoining_nodes

    def find_paths(self, start, stop, visited):
        neighbors = self.graph[start]
        paths = []
        if start == stop:
            if stop in visited:
                return [[stop]]
            visited.add(stop)
        for neighbor in neighbors:
            if neighbor == stop:
                paths.append([start, stop])
            if neighbor not in visited:
                visited.add(neighbor)
                cropped_paths = self.find_paths(neighbor, stop, visited)
                paths += [[start] + cropped_path for cropped_path in cropped_paths]

        return paths

    def find_loops(self, start):
        loops = self.find_paths(start, start, set())
        return [Loop(loop) for loop in loops] if loops else []

    @staticmethod
    def node(x, y):
        return tuple([x, y])
