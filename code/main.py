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


if __name__ == '__main__':
    a = Aufgabe()
    for i in range(0, 4):

        out = a.neighbour(63, i)
        print(out)
