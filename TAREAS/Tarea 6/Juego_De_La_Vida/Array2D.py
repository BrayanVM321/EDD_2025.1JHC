# array2d.py
from LIstaLigada import ListaLigada

class Array2d:
    def __init__(self):
        self.grid = {}

    def get_cell(self, x, y):
        if (x, y) not in self.grid:
            self.grid[(x, y)] = 0
        return self.grid[(x, y)]

    def set_cell(self, x, y, value):
        self.grid[(x, y)] = value

    def get_neighbors(self, x, y):
        neighbors = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),           (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]
        return [self.get_cell(nx, ny) for nx, ny in neighbors]
