class Paciente:
    def __init__(self, nombre, id_paciente):
        self.nombre = nombre
        self.id_paciente = id_paciente

    def __str__(self):
        return f"Paciente(Nombre: {self.id_paciente}, Numero: {self.nombre})"
