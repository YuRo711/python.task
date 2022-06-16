from tkinter import *

font = ('Helvetica', 16)
player1_color = '#0492CF'
player2_color = '#EE4035'


class GameOver:
    def __init__(self, start_window, winner):
        self.window = Tk()
        self.window.title('Dots')
        self.start_window = start_window
        start_window.clear_logs()
        self.canvas = Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        restart_btn = Button(self.window, text='Заново', width=10, height=1, bd='5', font=font,
                             command=self.restart)
        restart_btn.place(x=180, y=400)
        result = "Ничья!"
        color = 'black'
        if winner == 1:
            result = "Победил игрок 1!"
            color = player1_color
        if winner == 2:
            result = "Победил игрок 2!"
            color = player2_color
        self.canvas.create_text(300, 50, text=result, fill=color, font=font)

    def restart(self):
        self.window.destroy()
        self.start_window.restart()
