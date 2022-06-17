from tkinter import *
from Recorder import *

font = ('Helvetica', 16)
player1_color = '#0492CF'
player2_color = '#EE4035'


class GameOver:
    def __init__(self, start_window, winner, score=-1):
        self.window = Tk()
        self.window.title('Dots')
        self.start_window = start_window
        start_window.clear_logs()
        self.recorder = Recorder()
        self.canvas = Canvas(self.window, width=500, height=350)
        self.canvas.pack()
        self.score = score
        restart_btn = Button(self.window, text='Готово', width=10, height=1, bd='5', font=font,
                             command=self.restart)
        restart_btn.place(x=180, y=270)
        result = "Ничья!"
        color = 'black'
        if winner == 1:
            result = "Победил игрок 1!"
            color = player1_color
        if winner == 2:
            result = "Победил игрок 2!"
            color = player2_color
        self.canvas.create_text(250, 50, text=result, fill=color, font=font)
        if score != -1:
            self.canvas.create_text(85, 150, text="Ваш счёт:", fill=color, font=font)
            self.canvas.create_text(150, 150, text=score, fill=color, font=font)
            self.canvas.create_text(100, 200, text="Введите имя:", font=font)
            self.entry = Entry(width=25)
            self.entry.pack()
            self.entry.place(x=200, y=190)

    def restart(self):
        if self.score != -1:
            self.recorder.record(self.entry.get(), self.score)
        self.window.destroy()
        self.start_window.restart()
