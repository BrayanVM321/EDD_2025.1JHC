# lista_ligada.py
from nodo import Nodo

class ListaLigada:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Nodo(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current:
                current = current.next
            else:
                return None
        return current
