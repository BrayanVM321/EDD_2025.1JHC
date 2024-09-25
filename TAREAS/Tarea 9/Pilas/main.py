from Pilas import Pila

class Main:
    @staticmethod
    def run():
        texto = input("Introduce un texto para evaluar: ")
        pila = Pila()
        resultado = pila.balancear(texto)
        print(f"Texto ingresado: {texto}")
        print(resultado)


if __name__ == "__main__":
    Main.run()