# code partially based on aqeelanwar's Dots and Boxes solution
# https://github.com/aqeelanwar/Dots-and-Boxes/blob/17bc03559cba5007e7103d3f1889c478bb28b61b/main.py#L51

from tkinter import *
from GridModel import *

dots_in_row = 6
board_size = 600
dot_color = '#808080'
player1_color = '#0492CF'
player2_color = '#EE4035'
dot_width = 0.25 * board_size / dots_in_row
edge_width = 0.1 * board_size / dots_in_row
distance = board_size / dots_in_row
font = ('Helvetica', 16)


class Dots:

    # Функции инициализации

    def __init__(self, size, start):
        self.window = Tk()
        self.window.title('Dots')
        self.start_window = start
        self.board_size = size * 100
        self.dots_in_row = size
        self.canvas = Canvas(self.window, width=self.board_size + 200, height=self.board_size)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        self.grid_model = GridModel([[-1] * self.dots_in_row for i in range(self.dots_in_row)])
        self.player2_move = False
        self.move_info = self.canvas.create_text(0, 0)
        self.score1_info = self.canvas.create_text(0, 0)
        self.score2_info = self.canvas.create_text(0, 0)
        self.AI =
        self.new_game()

    @property
    def grid(self):
        return self.grid_model.grid

    @property
    def score1(self):
        score = self.grid_model.count_points(GridModel.Colors.player1)
        return score

    @property
    def score2(self):
        score = self.grid_model.count_points(GridModel.Colors.player2)
        return score

    def mainloop(self):
        self.window.mainloop()

    def new_game(self):
        self.player2_move = False
        self.grid_model = GridModel([[GridModel.Colors.default] * self.dots_in_row for i in range(self.dots_in_row)])
        self.refresh_board()
        self.update_info()

    def refresh_board(self):
        for i in range(self.dots_in_row):
            x = i * distance + distance / 2
            self.canvas.create_line(x, distance / 2, x,
                                    self.board_size - distance / 2,
                                    fill='gray', dash=(2, 2))
            self.canvas.create_line(distance / 2, x,
                                    self.board_size - distance / 2, x,
                                    fill='gray', dash=(2, 2))

        for i in range(self.dots_in_row):
            for j in range(self.dots_in_row):
                start_x = i * distance + distance / 2
                end_x = j * distance + distance / 2
                self.canvas.create_oval(start_x - dot_width / 2, end_x - dot_width / 2, start_x + dot_width / 2,
                                        end_x + dot_width / 2, fill=dot_color,
                                        outline=dot_color)

        self.canvas.create_text(self.board_size + 20, 50, text='Ходит:', fill='black', font=font)
        self.canvas.create_text(self.board_size + 10, 100, text='Счёт', fill='black', font=font)
        restart_btn = Button(self.window, text='Заново', width=10, height=1, bd='5', font=font,
                             command=self.restart)
        restart_btn.place(x=self.board_size, y=self.board_size - 100)

    def restart(self):
        self.window.destroy()
        self.start_window.restart()

    # Функционал игры

    def click(self, event):
        event_x = (event.x - 50) % 100
        event_y = (event.y - 50) % 100
        if (dot_width >= event_x or event_x >= 100 - dot_width) and \
                (dot_width >= event_y or event_y >= 100 - dot_width):
            grid_y = (event.y - 50) // 100 + (event.y - 50) % 100 // 50
            grid_x = (event.x - 50) // 100 + (event.x - 50) % 100 // 50
            if self.grid[grid_y][grid_x] == GridModel.Colors.default:
                self.update_dots(grid_x, grid_y)

    def update_dots(self, x, y):
        start_x = x * distance + distance / 2
        start_y = y * distance + distance / 2
        color = player2_color if self.player2_move else player1_color
        self.canvas.create_oval(start_x - dot_width / 2, start_y - dot_width / 2, start_x + dot_width / 2,
                                start_y + dot_width / 2, fill=color, outline=color)

        self.grid_model.grid[y][x] = GridModel.Colors.player2 if self.player2_move else GridModel.Colors.player1
        self.grid_model.update(y, x)
        loops = self.grid_model.last_step_loops
        for loop in loops:
            self.canvas.create_polygon(self.screen_points_cords(loop.path), fill=color)
        self.grid_model.update(y, x)
        self.player2_move = not self.player2_move
        self.update_info()

    def update_info(self):
        self.canvas.delete(self.move_info)
        self.canvas.delete(self.score1_info)
        self.canvas.delete(self.score2_info)
        color = player2_color if self.player2_move else player1_color
        player = "Игрок 2" if self.player2_move else "Игрок 1"
        self.move_info = self.canvas.create_text(self.board_size + 100, 50, text=player, fill=color, font=font)
        self.score1_info = self.canvas.create_text(self.board_size + 35, 130, text="Игрок 1: " + str(self.score1),
                                                   fill=player1_color, font=font)
        self.score2_info = self.canvas.create_text(self.board_size + 35, 160, text="Игрок 2: " + str(self.score2),
                                                   fill=player2_color, font=font)

    def draw_cell(self, x, y, color):
        start_x = x * distance + distance / 2
        start_y = y * distance + distance / 2
        self.canvas.create_rectangle(start_x, start_y, start_x + distance, start_y + distance,
                                     fill=color, outline=color)

    @staticmethod
    def screen_coord(grid_coord):
        return grid_coord * distance + distance / 2

    @staticmethod
    def screen_cords(grid_numbers):
        return [Dots.screen_coord(grid_numbers[i]) for i in range(len(grid_numbers))]

    @staticmethod
    def screen_points_cords(points):
        return Dots.screen_cords([point[i] for point in points for i in range(1, -1, -1)])

