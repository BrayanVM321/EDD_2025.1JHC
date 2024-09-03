class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.cabeza is None

    def obtener_tamanio(self):
        return self.tamanio

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamanio += 1

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_despues_de(self, referencia, valor):
        nuevo_nodo = Nodo(valor)
        actual = self.cabeza
        while actual and actual.valor != referencia:
            actual = actual.siguiente
        if actual:
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.tamanio += 1

    def eliminar(self, posicion):
        if self.esta_vacia() or posicion >= self.tamanio:
            return
        if posicion == 0:
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            actual.siguiente = actual.siguiente.siguiente
        self.tamanio -= 1

    def eliminar_el_primero(self):
        if not self.esta_vacia():
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1

    def eliminar_el_final(self):
        if self.esta_vacia():
            return
        if self.cabeza.siguiente is None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None
        self.tamanio -= 1

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def actualizar(self, a_buscar, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == a_buscar:
                actual.valor = valor
                return
            actual = actual.siguiente

    def transversal(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

class SmartPhone:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

def main():
    lista = ListaLigada()

    # agregar 5 SmartPhones Samsung
    lista.agregar_al_final(SmartPhone("Samsung", "Galaxy A55"))
    lista.agregar_al_final(SmartPhone("Samsung", "Galaxy S23FE"))
    lista.agregar_al_final(SmartPhone("Samsung", "Galaxy S22 Ultra"))
    lista.agregar_al_final(SmartPhone("Samsung", "Galaxy Note 20 Ultra"))
    lista.agregar_al_final(SmartPhone("Samsung", "Galaxy S21"))

    # imprimir el contenido
    print("Contenido de la lista:")
    lista.transversal()

    # Eliminar el de la posición 2
    lista.eliminar(2)
    print("\nDespués de eliminar el elemento en la posición 2:")
    lista.transversal()

    # Actualizar el segundo elemento
    lista.actualizar(lista.cabeza.siguiente.valor, SmartPhone("Apple", "iPhone 14"))
    print("\nDespués de actualizar el segundo elemento:")
    lista.transversal()

    # Agregar un elemento al inicio y otro al final
    lista.agregar_al_inicio(SmartPhone("Apple", "iPhone SE"))
    lista.agregar_al_final(SmartPhone("Apple", "iPhone 15"))
    print("\nDespués de agregar elementos al inicio y al final:")
    lista.transversal()

    # eliminar el primero
    lista.eliminar_el_primero()
    print("\nDespués de eliminar el primer elemento:")
    lista.transversal()

if __name__ == "__main__":
    main()
