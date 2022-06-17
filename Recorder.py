class Recorder:
    def record(self, name, score):
        top = self.records_list()
        file = open("records.txt", "w")
        for pos in range(len(top)):
            if top[pos][0] < score:
                top.insert(pos, [score, name])
                break
        if len(top) < 10 and not ([score, name] in top):
            top.append([score, name])
        for el in top:
            file.write(str(el[0]) + " " + el[1] + "\n")
        file.close()

    @staticmethod
    def records_list():
        file = open("records.txt", "r")
        top = []
        for line in file:
            pair = line.split()
            name = pair[1] if len(pair) == 2 else ""
            top.append([int(pair[0]), name])
        file.close()
        return top
