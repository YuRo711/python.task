class Loop:
    def __init__(self, path):
        self.path = path
        self.points_by_line = self.make_dict_points_by_line()
        self.opening_boundary_points_by_line = dict()
        self.closing_boundary_points_by_line = dict()
        #self.fill_boundary_points()

    @property
    def edges(self):
        edges = []
        for i in range(len(self.path) - 1):
            edges.append([self.path[i], self.path[i + 1]])
        return edges

    # лажа
    def fill_boundary_points(self):
        for line, points in self.points_by_line.items():
            points.sort()
            self.opening_boundary_points_by_line[line] += [points[i] for i in range(0, len(points), 2)]
            self.closing_boundary_points_by_line[line] += [points[i] for i in range(1, len(points), 2)]

    def make_dict_points_by_line(self):
        points_by_line = dict()
        for point in self.path:
            line, cell = point
            if line not in points_by_line.keys():
                points_by_line[line] = []
            points_by_line[line].append(cell)
        return points_by_line

    @property
    def filling_points(self):
        points = set()
        for line in self.opening_boundary_points_by_line.keys():
            quantity = len(self.opening_boundary_points_by_line[line])
            for i in range(quantity):
                for j in range(self.opening_boundary_points_by_line[line][i],
                               self.closing_boundary_points_by_line[line][i] + 1):
                    points.add(self.node(line, j))
        return points

    @staticmethod
    def node(x, y):
        return tuple([x, y])
