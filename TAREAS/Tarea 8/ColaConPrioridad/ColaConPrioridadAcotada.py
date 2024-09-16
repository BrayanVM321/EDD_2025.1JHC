import heapq

class ColaConPrioridadAcotada:
    def __init__(self):
        self.heap = []

    def agregar_cliente(self, cliente):
        heapq.heappush(self.heap, cliente)

    def atender_cliente(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

    def imprimir_estado(self):
        print("Estado de la cola con prioridad:")
        for cliente in self.heap:
            print(cliente)
def imprimir_estado(self):
    if self.esta_vacia():
        print("Estado de la cola: Sin clientes")
    else:
        # Código para imprimir los clientes en la cola
        pass
