from tkinter import *
from Dots import *
from Logger import *
from Records import *
import os.path

font = ('Helvetica', 15)


class Start:
    def __init__(self):
        self.window = Tk()
        self.window.title('Dots')
        self.canvas = Canvas(self.window, width=500, height=550)
        self.canvas.pack()
        self.size = 6
        self.logger = Logger()
        if os.path.isfile("log.txt"):
            load_btn = Button(self.window, text='Загрузить', width=20, height=1, bd='5', font=font,
                          command=self.load)
            load_btn.place(x=120, y=70)
        solo_btn = Button(self.window, text='Новая одиночная игра', width=30, height=1, bd='5', font=font,
                          command=self.new_solo_game)
        solo_btn.place(x=65, y=170)
        multi_btn = Button(self.window, text='Новая игра на двоих', width=30, height=1, bd='5', font=font,
                           command=self.new_multi_game)
        multi_btn.place(x=65, y=240)

        self.canvas.create_text(130, 330, text='Размер поля:', font=font)
        minus_btn = Button(self.window, text='-', width=2, height=1, bd='5', font=font,
                           command=self.size_minus)
        minus_btn.place(x=220, y=310)
        self.size_text = self.canvas.create_text(300, 330, text=str(self.size), font=font)
        plus_btn = Button(self.window, text='+', width=2, height=1, bd='5', font=font,
                          command=self.size_plus)
        plus_btn.place(x=350, y=310)

        record_btn = Button(self.window, text='Таблица рекордов', width=30, height=1, bd='5', font=font,
                            command=self.records)
        record_btn.place(x=65, y=420)
        exit_btn = Button(self.window, text='Выход', width=20, height=1, bd='5', font=font,
                          command=quit)
        exit_btn.place(x=120, y=490)

    def mainloop(self):
        self.window.mainloop()

    def size_plus(self):
        self.size += 1
        self.canvas.delete(self.size_text)
        self.size_text = self.canvas.create_text(300, 330, text=str(self.size), font=font)

    def size_minus(self):
        self.size -= 1
        if self.size <= 2:
            self.size = 3
        self.canvas.delete(self.size_text)
        self.size_text = self.canvas.create_text(300, 330, text=str(self.size), font=font)

    def new_solo_game(self):
        game_instance = Dots(self.size, self)
        self.window.destroy()
        game_instance.mp_mode = False
        game_instance.grid_model.logger.mp_mode = False
        self.clear_logs()
        game_instance.mainloop()

    def new_multi_game(self):
        game_instance = Dots(self.size, self)
        self.window.destroy()
        game_instance.mp_mode = True
        game_instance.grid_model.logger.mp_mode = True
        self.clear_logs()
        game_instance.mainloop()

    def load(self):
        state, mp_mode, player2_move, loops = self.logger.read(open("log.txt", "r"))
        size = len(state)
        game_instance = Dots(size, self)
        self.window.destroy()
        game_instance.mp_mode = mp_mode
        game_instance.player2_move = player2_move
        grid_model = game_instance.grid_model
        grid_model.logger.mp_mode = mp_mode
        grid_model.grid = state
        grid_model.last_step_loops = loops
        grid_model.logger.write(grid_model.grid, grid_model.total_loops)
        for y in range(size):
            for x in range(size):
                if state[y][x] != -1:
                    game_instance.update_dots(x, y, state[y][x] == 2, True)
        game_instance.mainloop()

    def records(self):
        rec_instance = Records(self)
        self.window.destroy()
        rec_instance.mainloop()

    @staticmethod
    def clear_logs():
        if os.path.isfile("log.txt"):
            os.remove("log.txt")
        if os.path.isfile("prev.txt"):
            os.remove("prev.txt")
        if os.path.isfile("prev2.txt"):
            os.remove("prev2.txt")

    def restart(self):
        self.__init__()


start_instance = Start()
start_instance.mainloop()
