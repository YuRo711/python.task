from tkinter import *
from Dots import *

font = ('Helvetica', 15)


class Start:
    def __init__(self):
        self.window = Tk()
        self.window.title('Dots')
        self.canvas = Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.size = 6
        load_btn = Button(self.window, text='Загрузить', width=20, height=1, bd='5', font=font,
                          command=self.new_solo_game)
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

        exit_btn = Button(self.window, text='Выход', width=20, height=1, bd='5', font=font,
                          command=quit)
        exit_btn.place(x=120, y=440)

    def mainloop(self):
        self.window.mainloop()

    def size_plus(self):
        self.size += 1
        self.canvas.delete(self.size_text)
        self.size_text = self.canvas.create_text(300, 330, text=str(self.size), font=font)

    def size_minus(self):
        self.size -= 3
        if self.size == 0:
            self.size = 3
        self.canvas.delete(self.size_text)
        self.size_text = self.canvas.create_text(300, 330, text=str(self.size), font=font)

    def new_solo_game(self):
        game_instance = Dots(self.size, self)
        self.window.destroy()
        game_instance.mp_mode = False
        game_instance.mainloop()

    def new_multi_game(self):
        game_instance = Dots(self.size, self)
        self.window.destroy()
        game_instance.mp_mode = True
        game_instance.mainloop()

    def restart(self):
        self.__init__()


start_instance = Start()
start_instance.mainloop()
