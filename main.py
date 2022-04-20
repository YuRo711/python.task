# code partially based on aqeelanwar's Dots and Boxes solution
# https://github.com/aqeelanwar/Dots-and-Boxes/blob/17bc03559cba5007e7103d3f1889c478bb28b61b/main.py#L51

from tkinter import *
import numpy as np

board_size = 600
dots_in_row = 6
symbol_size = (board_size / 3 - board_size / 8) / 2
symbol_thickness = 50
dot_color = '#808080'
player1_color = '#0492CF'
player2_color = '#EE4035'
dot_width = 0.25 * board_size / dots_in_row
edge_width = 0.1 * board_size / dots_in_row
distance_between_dots = board_size / dots_in_row


class Dots:

    # Функции инициализации

    def __init__(self):
        self.window = Tk()
        self.window.title('Dots')
        self.canvas = Canvas(self.window, width=board_size, height=board_size)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        self.grid = [[-1] * dots_in_row for i in range(dots_in_row)]
        self.player2_move = False
        self.new_game()

    def mainloop(self):
        self.window.mainloop()

    def new_game(self):
        self.player2_move = False
        self.grid = [[-1] * dots_in_row for i in range(dots_in_row)]
        self.refresh_board()

    def refresh_board(self):
        for i in range(dots_in_row):
            x = i * distance_between_dots + distance_between_dots / 2
            self.canvas.create_line(x, distance_between_dots / 2, x,
                                    board_size - distance_between_dots / 2,
                                    fill='gray', dash=(2, 2))
            self.canvas.create_line(distance_between_dots / 2, x,
                                    board_size - distance_between_dots / 2, x,
                                    fill='gray', dash=(2, 2))

        for i in range(dots_in_row):
            for j in range(dots_in_row):
                start_x = i * distance_between_dots + distance_between_dots / 2
                end_x = j * distance_between_dots + distance_between_dots / 2
                self.canvas.create_oval(start_x - dot_width / 2, end_x - dot_width / 2, start_x + dot_width / 2,
                                        end_x + dot_width / 2, fill=dot_color,
                                        outline=dot_color)

    # Функционал игры

    def click(self, event):
        event_x = (event.x - 50) % 100
        event_y = (event.y - 50) % 100
        if (dot_width >= event_x or event_x >= 100 - dot_width) and \
                (dot_width >= event_y or event_y >= 100 - dot_width):
            grid_y = (event.y - 50) // 100 + (event.y - 50) % 100 // 50
            grid_x = (event.x - 50) // 100 + (event.x - 50) % 100 // 50
            if self.grid[grid_y][grid_x] == -1:
                self.update_board(grid_x, grid_y)

    def update_board(self, x, y):
        start_x = x * distance_between_dots + distance_between_dots / 2
        start_y = y * distance_between_dots + distance_between_dots / 2
        color = player1_color
        if self.player2_move:
            color = player2_color
        self.canvas.create_oval(start_x - dot_width / 2, start_y - dot_width / 2, start_x + dot_width / 2,
                                start_y + dot_width / 2, fill=color, outline=color)
        self.grid[y][x] = int(self.player2_move)
        self.player2_move = not self.player2_move


game_instance = Dots()
game_instance.mainloop()
