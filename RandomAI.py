import random
from GridModel import *


class RandomAI:
    def __init__(self, game):
        self.game = game
        self.board_size = game.board_size // 100

    def move(self):
        x, y = self.random()
        while self.game.grid_model.grid[y][x] != self.game.grid_model.Colors.default:
            x, y = self.random()
        self.game.update_dots(x, y, True)

    def random(self):
        return random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
