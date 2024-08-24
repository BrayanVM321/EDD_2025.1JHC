class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def cambiar_valor(self, posicion, nuevo_valor):
        actual = self.cabeza
        contador = 1
        while actual:
            if contador == posicion:
                actual.valor = nuevo_valor
                return
            actual = actual.siguiente
            contador += 1

    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

# Crear la lista enlazada y agregar nodos
lista = ListaEnlazada()
lista.insertar_al_final(100)
lista.insertar_al_final(200)
lista.insertar_al_final(300)
lista.insertar_al_final(400)
lista.insertar_al_final(600)

# Imprimir la lista
print("Lista original:")
lista.imprimir_lista()

# cambio valor tercer nodo de 300 a 333
lista.cambiar_valor(3, 333)
print("\nLista después de cambiar el valor del 3er nodo:")
lista.imprimir_lista()

# ingreso de un nodo 700 después del nodo 600 (al final)
lista.insertar_al_final(700)
print("\nLista después de insertar 700 al final:")
lista.imprimir_lista()

# agregar un nodo con valor 50 al principio
lista.insertar_al_principio(50)
print("\nLista después de insertar 50 al principio:")
lista.imprimir_lista()
