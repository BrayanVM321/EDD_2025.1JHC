class ColaADT:
    def __init__(self):
        self.cola = []

    def esta_vacia(self):
        return len(self.cola) == 0

    def encolar(self, paciente):
        self.cola.append(paciente)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía, no se puede desencolar.")
        return self.cola.pop(0)

    def mostrar_cola(self):
        return self.cola

    def siguiente_paciente(self):
        if self.esta_vacia():
            return None
        return self.cola[0]
