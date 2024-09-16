# juego.py
from Array2D import Array2d

class Juego:
    def __init__(self):
        self.grid = Array2d()

    def next_generation(self):
        new_grid = Array2d()
        cells_to_check = set(self.grid.grid.keys())
        for (x, y) in list(cells_to_check):
            cells_to_check.update([(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)])
        
        for (x, y) in cells_to_check:
            neighbors = self.grid.get_neighbors(x, y)
            live_neighbors = sum(neighbors)
            if self.grid.get_cell(x, y) == 1:
                if live_neighbors in [2, 3]:
                    new_grid.set_cell(x, y, 1)
                else:
                    new_grid.set_cell(x, y, 0)
            else:
                if live_neighbors == 3:
                    new_grid.set_cell(x, y, 1)
                else:
                    new_grid.set_cell(x, y, 0)
        self.grid = new_grid

