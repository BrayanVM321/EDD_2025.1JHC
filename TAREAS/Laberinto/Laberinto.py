import tkinter as tk
import time

# Clase Pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def meter(self, item):
        self.items.append(item)

    def sacar(self):
        return self.items.pop()

    def tope(self):
        return self.items[-1]

    def tamaño(self):
        return len(self.items)

# Clase Array2D
class Array2D:
    def __init__(self, filas, columnas):
        self.datos = [[0] * columnas for _ in range(filas)]

    def num_filas(self):
        return len(self.datos)

    def num_columnas(self):
        return len(self.datos[0])

    def __getitem__(self, indice):
        fila, columna = indice
        return self.datos[fila][columna]

    def __setitem__(self, indice, valor):
        fila, columna = indice
        self.datos[fila][columna] = valor

# Inicializar el laberinto con las paredes y pasillos especificados
laberinto = Array2D(6, 7)
laberinto.datos = [
    [1, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 2],
    [2, 2, 2, 2, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 2],
    [2, 2, 0, 0, 0, 0, 2],
    [5, 0, 0, 2, 2, 0, 0]
]

inicio = (0, 0)
fin = (5, 0)
modo = "pared"  
# Interfaz gráfica
def crear_interfaz(laberinto):
    root = tk.Tk()
    root.title("Resolver Laberintos")

    canvas = tk.Canvas(root, width=700, height=600)
    canvas.pack()

    for i in range(laberinto.num_filas()):
        for j in range(laberinto.num_columnas()):
            if laberinto[i, j] == 1:
                color = "green"  # Entrada
            elif laberinto[i, j] == 5:
                color = "red"  # Salida
            elif laberinto[i, j] == 2:
                color = "black"  # Pared
            elif laberinto[i, j] == 0:
                color = "white"  # Pasillo
            canvas.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill=color, outline="gray")

    return root, canvas

# Funciones para manipular caminos, inicio y fin
def manipular_caminos(event):
    x, y = event.x // 100, event.y // 100

    if modo == "pared":
        laberinto[y, x] = 2 if laberinto[y, x] == 0 else 0
        color = "black" if laberinto[y, x] == 2 else "white"
        canvas.create_rectangle(x*100, y*100, (x+1)*100, (y+1)*100, fill=color, outline="gray")

def establecer_modo(nuevo_modo):
    global modo
    modo = nuevo_modo
    print("Modo actual:", modo)

# Resolver el laberinto con visualización en tiempo real usando back tracking y Pilas
def resolver_laberinto_visual(laberinto, inicio, fin):
    pila = Pila()
    pila.meter(inicio)
    movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Izquierda, Arriba, Derecha, Abajo
    visitado = set()

    while not pila.esta_vacia():
        root.update()
        x, y = pila.tope()

        if (x, y) == fin:
            canvas.create_rectangle(y*100, x*100, (y+1)*100, (x+1)*100, fill="blue", outline="gray")
            print("Salida encontrada")
            return True

        encontrado = False

        for movimiento in movimientos:
            nx, ny = x + movimiento[0], y + movimiento[1]

            if 0 <= nx < laberinto.num_filas() and 0 <= ny < laberinto.num_columnas() and laberinto[nx, ny] in (0, 5) and (nx, ny) not in visitado:
                pila.meter((nx, ny))
                visitado.add((nx, ny))
                canvas.create_rectangle(ny*100, nx*100, (ny+1)*100, (nx+1)*100, fill="blue", outline="gray")
                time.sleep(0.2) 
                encontrado = True
                break

        if not encontrado:
            x, y = pila.sacar()
            if laberinto[x, y] != 1 and laberinto[x, y] != 5:
                laberinto[x, y] = 4
                canvas.create_rectangle(y*100, x*100, (y+1)*100, (x+1)*100, fill="red", outline="gray")
                time.sleep(0.2)  

    print("Salida no encontrada")
    return False

def limpiar_laberinto():
    global laberinto
    laberinto = Array2D(6, 7)
    laberinto.datos = [
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0]
    ]
    for i in range(laberinto.num_filas()):
        for j in range(laberinto.num_columnas()):
            if laberinto[i, j] == 1:
                color = "green"  
            elif laberinto[i, j] == 5:
                color = "red"  
            elif laberinto[i, j] == 2:
                color = "black"  
            elif laberinto[i, j] == 0:
                color = "white" 
            canvas.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill=color, outline="gray")
    print("Laberinto limpio")
    
def main():
    global canvas, root
    root, canvas = crear_interfaz(laberinto)

    canvas.bind("<Button-1>", manipular_caminos)

    btn_pared = tk.Button(root, text="Colocar Pared", command=lambda: establecer_modo("pared"))
    btn_pared.pack(side=tk.LEFT)

    btn_resolver = tk.Button(root, text="Resolver Laberinto", command=lambda: resolver_laberinto_visual(laberinto, inicio, fin))
    btn_resolver.pack(side=tk.LEFT)

    btn_limpiar = tk.Button(root, text="Limpiar Laberinto", command=limpiar_laberinto)
    btn_limpiar.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
