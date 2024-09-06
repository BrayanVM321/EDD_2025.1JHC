class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.head is None

    def get_tamanio(self):
        return self.tamanio

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.head = self.tail = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.head
            self.head.anterior = nuevo_nodo
            self.head = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.head = self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.tail
            self.tail = nuevo_nodo
        self.tamanio += 1

    def agregar_despues_de(self, referencia, valor):
        actual = self.head
        while actual and actual.valor != referencia:
            actual = actual.siguiente
        if actual:
            nuevo_nodo = Nodo(valor)
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            if actual.siguiente:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            if actual == self.tail:
                self.tail = nuevo_nodo
            self.tamanio += 1

    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return None
        actual = self.head
        for _ in range(posicion):
            actual = actual.siguiente
        return actual.valor

    def eliminar_el_primero(self):
        if not self.esta_vacia():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.siguiente
                self.head.anterior = None
            self.tamanio -= 1

    def eliminar_el_final(self):
        if not self.esta_vacia():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.anterior
                self.tail.siguiente = None
            self.tamanio -= 1

    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return
        if posicion == 0:
            self.eliminar_el_primero()
        elif posicion == self.tamanio - 1:
            self.eliminar_el_final()
        else:
            actual = self.head
            for _ in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamanio -= 1

    def buscar(self, valor):
        actual = self.head
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def actualizar(self, a_buscar, valor):
        actual = self.head
        while actual:
            if actual.valor == a_buscar:
                actual.valor = valor
                return True
            actual = actual.siguiente
        return False

    def transversal(self, direccion='izquierda'):
        elementos = []
        if direccion == 'izquierda':
            actual = self.head
            while actual:
                elementos.append(actual.valor)
                actual = actual.siguiente
        else:
            actual = self.tail
            while actual:
                elementos.append(actual.valor)
                actual = actual.anterior
        return elementos

# Ejemplo práctico
if __name__ == "__main__":
    lista = DoubleLinkedList()
    lista.agregar_al_inicio(50)
    lista.agregar_al_final(60)
    lista.agregar_al_final(65)
    lista.agregar_al_final(70)
    lista.agregar_al_final(80)
    lista.agregar_al_final(90)
    print("Contenido de la lista:", lista.transversal())
    lista.eliminar(2)
    print("Contenido después de eliminar el elemento en la posición 2:", lista.transversal())
    lista.actualizar(70, 88)
    print("Contenido después de actualizar el cuarto elemento a 88:", lista.transversal())
    posicion = lista.buscar(80)
    print(f"El valor 80 se encuentra en la posición: {posicion}")
