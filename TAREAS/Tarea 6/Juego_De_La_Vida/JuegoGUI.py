# gui.py
import tkinter as tk
from Juego import Juego

class JuegoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de la Vida")
        self.game = Juego()
        self.cell_size = 20  # Tamaño de las celdas aumentado a 20x20 píxeles
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.toggle_cell)
        
        self.start_button = tk.Button(root, text="Iniciar", command=self.start_game)
        self.start_button.pack(side=tk.LEFT)
        
        self.pause_button = tk.Button(root, text="Pausar", command=self.pause_game)
        self.pause_button.pack(side=tk.LEFT)
        
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_grid)
        self.clear_button.pack(side=tk.LEFT)
        
        self.running = False
        self.draw_grid()  # Dibujar la rejilla al iniciar la aplicación

    def toggle_cell(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        current_value = self.game.grid.get_cell(x, y)
        new_value = 1 if current_value == 0 else 0
        self.game.grid.set_cell(x, y, new_value)
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for x in range(25):  # Ajustado para el nuevo tamaño de las celdas
            for y in range(25):
                value = self.game.grid.get_cell(x, y)
                color = "green" if value == 1 else "white"
                self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size, x*self.cell_size+self.cell_size, y*self.cell_size+self.cell_size, fill=color, outline="black")

    def start_game(self):
        self.running = True
        self.update_grid()

    def pause_game(self):
        self.running = False

    def clear_grid(self):
        self.game = Juego()
        self.draw_grid()

    def update_grid(self):
        if self.running:
            self.game.next_generation()
            self.draw_grid()
            self.root.after(200, self.update_grid)  # Transiciones más lentas (200 ms)

if __name__ == "__main__":
    root = tk.Tk()
    gui = JuegoGUI(root)
    root.mainloop()
