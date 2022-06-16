import os.path


class Logger:
    def __init__(self):
        self.mp_mode = False

    def write(self, grid):
        prev = open("prev.txt", "w")
        if os.path.isfile("log.txt"):
            with open("log.txt", "r") as log1:
                log1.seek(0)
                prev.write(log1.read())
                log1.close()
                prev.close()
        log = open("log.txt", "w+")
        if self.mp_mode:
            log.write("1\n")
        else:
            log.write("0\n")
        for line in grid:
            for cell in line:
                log.write(str(cell) + " ")
            log.write("\n")
        log.close()

    @staticmethod
    def read(file):
        grid = []
        mp_mode = True
        for line in file:
            grid.append([])
            for cell in line.split():
                if cell == "Colors.default":
                    grid[-1].append(-1)
                elif cell == "Colors.player1":
                    grid[-1].append(0)
                elif cell == "Colors.player2":
                    grid[-1].append(2)
                else:
                    mp_mode = cell
        file.close()
        return grid, int(mp_mode)

    @staticmethod
    def compare():
        log = open("log.txt", "r")
        prev = open("prev.txt", "w")
