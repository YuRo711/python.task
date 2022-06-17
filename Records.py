from tkinter import *

font = ('Helvetica', 15)


class Records:
    def __init__(self, start):
        self.window = Tk()
        self.window.title('Dots')
        self.canvas = Canvas(self.window, width=500, height=600)
        self.canvas.pack()
        self.start_window = start
        plus_btn = Button(self.window, text='Назад', width=20, height=1, bd='5', font=font,
                          command=self.back)
        plus_btn.place(x=120, y=530)
        file = open("records.txt", "r")
        y = 100
        for line in file:
            pair = line.split()
            self.canvas.create_text(60, y, text=pair[0], font=font)
            if len(pair) > 1:
                self.canvas.create_text(130, y, text=pair[1], font=font)
            y += 30

    def mainloop(self):
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        self.start_window.restart()
