# Problema uno de recursividad 
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def tamaño(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def sacar_elemento_del_medio_recursivo(pila, contador, medio):
    if contador == medio:
        return pila.pop()
    temp = pila.pop()
    elemento_medio = sacar_elemento_del_medio_recursivo(pila, contador + 1, medio)
    pila.push(temp)
    return elemento_medio

# Crear pila
pila = Pila()
elementos = [8, 9, 23, 4, 5, 2, 1]
for elemento in elementos:
    pila.push(elemento)

# Imprimir la pila original
print("Pila original:", pila)

# Calcular el medio
medio = pila.tamaño() // 2

# Sacar el elemento del medio de forma recursiva
elemento_medio = sacar_elemento_del_medio_recursivo(pila, 0, medio)

# Imprimir el elemento del medio y la pila sin ese elemento
print("Elemento del medio:", elemento_medio)
print("Pila sin el elemento del medio:", pila)

# Imprimir division de los problemas

print ("\n SEGUNDO PROBLEMA \n")

def printRev(n):
    if n > 0:
        print(n)
        printRev(n - 1)

n = 4
printRev(n)
