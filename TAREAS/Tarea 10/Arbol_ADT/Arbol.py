class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.derecha)

    def imprimir_en_orden(self, nodo):
        if nodo is not None:
            self.imprimir_en_orden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.imprimir_en_orden(nodo.derecha)

class NodoGeneral:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class ArbolGeneral:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def agregar_hijo(self, nodo_padre, hijo_valor):
        nuevo_hijo = NodoGeneral(hijo_valor)
        nodo_padre.hijos.append(nuevo_hijo)
        return nuevo_hijo

    def imprimir_arbol(self, nodo, nivel=0):
        if nodo is not None:
            print('  ' * nivel + str(nodo.valor))
            for hijo in nodo.hijos:
                self.imprimir_arbol(hijo, nivel + 1)

# Crear el árbol de numeros
arbol = ArbolBinario()
arbol.agregar(10)
arbol.agregar(5)
arbol.agregar(15)
arbol.agregar(1)
arbol.agregar(25)

# Imprimir en orden
print("Árbol Binario:")
arbol.imprimir_en_orden(arbol.raiz)
print()

# Crear el árbol de nombres
raiz = NodoGeneral("Diego")
arbol_general = ArbolGeneral(raiz)
nodo_pedro = arbol_general.agregar_hijo(raiz, "Pedro")
nodo_mario = arbol_general.agregar_hijo(raiz, "Mario")
arbol_general.agregar_hijo(nodo_pedro, "Susan")
arbol_general.agregar_hijo(nodo_pedro, "Diana")

# Imprimir el árbol de nombres
print("Árbol General:")
arbol_general.imprimir_arbol(raiz)
