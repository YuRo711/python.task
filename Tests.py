import unittest
from GridModel import *


class GridTestMethods(unittest.TestCase):

    def test_simple_filling_point(self):
        g = [[-1, 0, -1],
             [0, 1, 0],
             [-1, 0, -1]]
        grid_model = GridModel.from_int_grid(g)
        grid_model.update(0, 1)
        new_g = \
            [[-1, 0, -1],
             [0, 0, 0],
             [-1, 0, -1]]
        expected_grid_model = GridModel.from_int_grid(new_g)
        self.assertEqual(expected_grid_model.grid, grid_model.grid)
        self.assertEqual(5, grid_model.count_points(GridModel.Colors.player1))


if __name__ == '__main__':
    unittest.main()
