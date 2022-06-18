import unittest
# from parameterized
from GridModel import *


class GridTestMethods(unittest.TestCase):

    def test_simple_filling_point(self):
        grid = [[-1, 0, -1],
                [0, 1, 0],
                [-1, 0, -1]]
        new_point = (0, 1)
        new_grid = \
            [[-1, 0, -1],
             [0, 0, 0],
             [-1, 0, -1]]
        expected_score = 5
        self.assert_correct_updating_new_point(grid, new_grid, new_point, expected_score)

    def test_double_loop(self):
        grid = [[-1, 0, -1],
                [0, 1, 0],
                [-1, 0, -1],
                [0, 1, 0],
                [-1, 0, -1]]
        new_point = (2, 1)
        new_grid = [[-1, 0, -1],
                    [0, 0, 0],
                    [-1, 0, -1],
                    [0, 0, 0],
                    [-1, 0, -1]]
        expected_score_1 = 9
        self.assert_correct_updating_new_point(grid, new_grid, new_point, expected_score_1)

    def test_two_steps_in_crossed_loops(self):
        grid = [[-1, 0, -1],
                [0, 1, 0],
                [-1, 0, -1],
                [-1, 1, 0],
                [-1, 0, -1]]
        new_point_1 = (1, 0)
        new_grid_1 = [[-1, 0, -1],
                      [0, 0, 0],
                      [-1, 0, -1],
                      [-1, 1, 0],
                      [-1, 0, -1]]
        self.assert_correct_updating_new_point(grid, new_grid_1, new_point_1, 7)
        new_grid_1[3][0] = 0
        new_point_2 = (3, 0)
        new_grid_2 = [[-1, 0, -1],
                      [0, 0, 0],
                      [-1, 0, -1],
                      [0, 0, 0],
                      [-1, 0, -1]]
        self.assert_correct_updating_new_point(new_grid_1, new_grid_2, new_point_2, 9)

    def test_difficult_shaped_loop(self):
        grid = [[0, -1, 0, -1, -1],
                [0, 0, 1, 0, -1],
                [0, -1, 1, 0, -1],
                [0, -1, 0, -1, -1],
                [-1, 0, -1, -1, -1]]
        new_point = (1, 1)
        expected_new_grid = [[0, -1, 0, -1, -1],
                             [0, 0, 0, 0, -1],
                             [0, 0, 0, 0, -1],
                             [0, 0, 0, -1, -1],
                             [-1, 0, -1, -1, -1]]
        self.assert_correct_updating_new_point(grid, expected_new_grid, new_point)

    def assert_correct_updating_new_point(self, old_grid, expected_new_grid, changed_point,
                                          expected_score_1=None, expected_score_2=None):
        grid_model = GridModel.from_int_grid(old_grid)
        x, y = changed_point
        grid_model.update(x, y)
        expected_new_grid_model = GridModel.from_int_grid(expected_new_grid)
        self.assertEqual(expected_new_grid_model.grid, grid_model.grid)
        if expected_score_1:
            self.assertEqual(expected_score_1, grid_model.count_points(GridModel.Colors.player1))
        if expected_score_2:
            self.assertEqual(expected_score_2, grid_model.count_points(GridModel.Colors.player2))


if __name__ == '__main__':
    unittest.main()
