class ConjuntoADT:
    def __init__(self):
        self.elementos = []

    def longitud(self):
        return len(self.elementos)

    def contiene(self, elemento):
        return elemento in self.elementos

    def agregar(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def eliminar(self, elemento):
        if self.contiene(elemento):
            self.elementos.remove(elemento)

    def equals(self, otroConjunto):
        return sorted(self.elementos) == sorted(otroConjunto.elementos)

    def esSubConjunto(self, otroConjunto):
        return all(elem in otroConjunto.elementos for elem in self.elementos)

    def union(self, otroConjunto):
        nuevoConjunto = ConjuntoADT()
        nuevoConjunto.elementos = list(set(self.elementos + otroConjunto.elementos))
        return nuevoConjunto

    def interseccion(self, otroConjunto):
        nuevoConjunto = ConjuntoADT()
        nuevoConjunto.elementos = [elem for elem in self.elementos if elem in otroConjunto.elementos]
        return nuevoConjunto

    def diferencia(self, otroConjunto):
        nuevoConjunto = ConjuntoADT()
        nuevoConjunto.elementos = [elem for elem in self.elementos if elem not in otroConjunto.elementos]
        return nuevoConjunto

# Ejemplo práctico
if __name__ == "__main__":
    conjunto1 = ConjuntoADT()
    conjunto2 = ConjuntoADT()

    # Agregar elementos
    conjunto1.agregar(1)
    conjunto1.agregar(2)
    conjunto1.agregar(3)
    conjunto2.agregar(3)
    conjunto2.agregar(4)
    conjunto2.agregar(5)

    # Eliminar un elemento
    conjunto1.eliminar(2)

    # Comprobar pertenencia de un elemento 
    print("¿Conjunto1 contiene 1?", conjunto1.contiene(1))  
    print("¿Conjunto2 contiene 2?", conjunto2.contiene(2)) 

    # Comprobar la longitud de los conjuntos
    print("Longitud de Conjunto1:", conjunto1.longitud())  
    print("Longitud de Conjunto2:", conjunto2.longitud())  

    # Comprobar si los conjuntos son iguales
    print("¿Conjunto1 es igual a Conjunto2?", conjunto1.equals(conjunto2))  
    # Comprobar si Conjunto1 es subconjunto de Conjunto2
    print("¿Conjunto1 es subconjunto de Conjunto2?", conjunto1.esSubConjunto(conjunto2))  

    # Operaciones de unión, intersección y diferencia
    union = conjunto1.union(conjunto2)
    interseccion = conjunto1.interseccion(conjunto2)
    diferencia = conjunto1.diferencia(conjunto2)

    print("Conjunto1:", conjunto1.elementos)
    print("Conjunto2:", conjunto2.elementos)
    print("Unión:", union.elementos)
    print("Intersección:", interseccion.elementos)
    print("Diferencia:", diferencia.elementos)
