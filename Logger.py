import os.path


class Logger:
    def __init__(self):
        self.mp_mode = False
        self.player2_move = False

    def write(self, grid):
        self.rewrite("prev2.txt", "prev.txt")
        self.rewrite("prev.txt", "log.txt")
        log = open("log.txt", "w+")
        if self.mp_mode:
            log.write("1\n")
        else:
            log.write("0\n")
        if self.player2_move:
            log.write("player2\n")
        else:
            log.write("player1\n")
        for line in grid:
            for cell in line:
                log.write(str(cell) + " ")
            log.write("\n")
        log.close()

    @staticmethod
    def rewrite(prev_name, log_name):
        prev = open(prev_name, "w")
        if os.path.isfile(log_name):
            with open(log_name, "r") as log1:
                log1.seek(0)
                prev.write(log1.read())
                log1.close()
                prev.close()

    @staticmethod
    def read(file):
        grid = []
        mp_mode = True
        player2_move = False
        for line in file:
            grid.append([])
            for cell in line.split():
                if cell == "Colors.default":
                    grid[-1].append(-1)
                elif cell == "Colors.player1":
                    grid[-1].append(0)
                elif cell == "Colors.player2":
                    grid[-1].append(2)
                elif cell == "player2":
                    player2_move = True
                elif cell == "player1":
                    player2_move = False
                else:
                    mp_mode = cell
        file.close()
        return grid, int(mp_mode), player2_move

    @staticmethod
    def compare():
        log = open("log.txt", "r")
        prev = open("prev.txt", "w")
