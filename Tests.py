import unittest
from Grid import *


class GridTestMethods(unittest.TestCase):

    def test_simple_filling_point(self):
        g = [[-1, 0, -1],
             [0, 1, 0],
             [-1, 0, -1]]
        grid = Grid(g)
        grid.update(0, 1)
        new_grid = \
            [[-1, 0, -1],
             [0, 0, 0],
             [-1, 0, -1]]
        self.assertEqual(new_grid, grid.grid)


if __name__ == '__main__':
    unittest.main()