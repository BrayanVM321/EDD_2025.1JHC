from ClienteBanco import ClienteBanco
from ColaConPrioridadAcotada import ColaConPrioridadAcotada

def main():
    cola = ColaConPrioridadAcotada()

    # Llegan 2 clientes nuevos
    cliente1 = ClienteBanco("Roberto Martinez", "Cliente nuevo")
    cliente2 = ClienteBanco("Gustavo Hernandez", "Cliente nuevo")
    cola.agregar_cliente(cliente1)
    cola.agregar_cliente(cliente2)

    # Llegan 3 personas que no son clientes
    cliente3 = ClienteBanco("Carlos Rodriguez", "No es cliente")
    cliente4 = ClienteBanco("Alfonso Peña", "No es cliente")
    cliente5 = ClienteBanco("Ximena Lopez", "No es cliente")
    cola.agregar_cliente(cliente3)
    cola.agregar_cliente(cliente4)
    cola.agregar_cliente(cliente5)

    # Llega una celebridad
    celebridad = ClienteBanco("Juan Gabriel", "Celebridad")
    cola.agregar_cliente(celebridad)

    # Imprime el estado de la cola con prioridad acotada
    cola.imprimir_estado()

    # Atiende al siguiente cliente
    cliente_atendido = cola.atender_cliente()
    if cliente_atendido:
        print(f"Se atiende a: {cliente_atendido.nombre}. Deposita $8,500 a su cuenta.")

    # Llegan dos clientes más, uno frecuente y uno premium
    cliente6 = ClienteBanco("Luis Morales", "Cliente frecuente")
    cliente7 = ClienteBanco("Raul Perez", "Cliente premium")
    cola.agregar_cliente(cliente6)
    cola.agregar_cliente(cliente7)

    # Atiende al siguiente cliente
    cliente_atendido = cola.atender_cliente()
    if cliente_atendido:
        print(f"Se atiende a: {cliente_atendido.nombre}. Retira $3,000 de su cuenta.")

    # Imprime el estado de la cola con prioridad acotada
    cola.imprimir_estado()

    # Atiende todos los clientes restantes con acciones variadas
    while (cliente_atendido := cola.atender_cliente()) is not None:
        if cliente_atendido.perfil == "Cliente frecuente":
            print(f"Se atiende a: {cliente_atendido.nombre}. Realiza una transferencia de $500.")
        elif cliente_atendido.perfil == "Cliente premium":
            print(f"Se atiende a: {cliente_atendido.nombre}. Solicita un préstamo de $10,000.")
        elif cliente_atendido.perfil == "Celebridad":
            print(f"Se atiende a: {cliente_atendido.nombre}. Recibe tratamiento especial.")
        else:
            print(f"Se atiende a: {cliente_atendido.nombre}. Deposita $1,350 a su cuenta.")

    # Imprime el estado final de la cola
    cola.imprimir_estado()

if __name__ == "__main__":
    main()
