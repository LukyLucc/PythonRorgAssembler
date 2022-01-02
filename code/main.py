# Pseudocode zur Aufgabe in Modul Rorg
import numpy as np


class Aufgabe:
    n = 8
    array = np.zeros((n, n))

    def neighbour(self, pos, direction):
        """
        Methode zur Berechnung des Nachbarindexes in einer bestimmten Richtung
        :param pos: Index im Array = self.n · y + x
        :param direction: 0,1,2,3
        0 => oben
        1 => links
        2 => unten
        3 => rechts

        :return: index
        """

        index = -1
        y = pos // self.n
        x = pos % self.n

        if direction == 0:  # oben
            if y == 0:
                index = -1
            else:
                index = pos - self.n

        if direction == 1:  # links
            if x == 0:
                index = -1
            else:
                index = pos - 1

        if direction == 2:  # unten
            if y == self.n - 1:
                index = -1
            else:
                index = pos + self.n

        if direction == 3:  # rechts
            if x == self.n - 1:
                index = -1
            else:
                index = pos + 1

        return index

    def trace_back(self, d):
        akt = d
        anzahl = 1
        while self.array[akt] != 1:
            min = 255
            min_pos = akt
            for i in range(0, 4):
                position = self.neighbour(akt, i)
                if self.array[position] < min and self.array[position] != -1:
                    min = self.array[position]
                    min_pos = position

            akt = min_pos
            self.array[akt] = 254
            anzahl += 1

if __name__ == '__main__':
    a = Aufgabe()
    for pos in range(64):
        out = a.neighbour(pos, 0)
        out1 = a.neighbour(pos, 1)
        out2 = a.neighbour(pos, 2)
        out3 = a.neighbour(pos, 3)
        print(pos, out, out1, out2, out3)
    print (a.neighbour(43, 0))

