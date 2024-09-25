class Pila:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()
        return None

    def balancear(self, texto):
        pares = {'(': ')', '{': '}', '[': ']'}
        pila = []

        for simbolo in texto:
            if simbolo in pares:  # Si es apertura
                pila.append(simbolo)
            elif simbolo in pares.values():  # Si es cierre
                if not pila:
                    return "Error: Encontrado un cierre sin su correspondiente apertura."
                top = pila.pop()
                if pares[top] != simbolo:
                    return "Error: Cierre no coincide con la apertura."

        if not pila:
            return "Todo está bien: Los símbolos están correctamente balanceados."
        else:
            return "Advertencia: Quedaron símbolos de apertura sin cerrar."
