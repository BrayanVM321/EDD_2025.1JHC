from Paciente import Paciente
from ColaADT import ColaADT

def main():
    cola = ColaADT()

    paciente1 = Paciente(1, "Brayan Velazco")
    paciente2 = Paciente(2, "Maria Morales")
    paciente3 = Paciente(3, "Ian Tapia")

    cola.encolar(paciente1)
    cola.encolar(paciente2)
    cola.encolar(paciente3)

    # Mostrar el contenido de la cola
    print("Contenido de la cola:")
    for paciente in cola.mostrar_cola():
        print(paciente)

    # Mostrar el siguiente paciente (sin sacarlo de la cola)
    print("\nSiguiente paciente en la cola:")
    print(cola.siguiente_paciente())

    # Atender al siguiente paciente
    paciente_atendido = cola.desencolar()
    print(f"\nPaciente atendido: {paciente_atendido}")

    # Mostrar el contenido de la cola después de atender a uno
    print("\nContenido de la cola después de atender a uno:")
    for paciente in cola.mostrar_cola():
        print(paciente)

    # Pedir Agregar 2 nuevos pacientes
    for i in range(4, 6):
        nombre = input(f"\nIngrese el nombre del paciente {i}: ")
        paciente = Paciente(i, nombre)
        cola.encolar(paciente)

    print("\nContenido de la cola después de agregar dos pacientes nuevos:")
    for paciente in cola.mostrar_cola():
        print(paciente)

    # Atender al siguiente paciente
    paciente_atendido = cola.desencolar()
    print(f"\nPaciente atendido: {paciente_atendido}")

    # Mostrar el contenido de la cola después de atender a otro paciente
    print("\nContenido de la cola después de atender a otro paciente:")
    for paciente in cola.mostrar_cola():
        print(paciente)

if __name__ == "__main__":
    main()
