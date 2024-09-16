class ClienteBanco:
    def __init__(self, nombre, perfil):
        self.nombre = nombre
        self.perfil = perfil
        self.prioridad = self.asignar_prioridad(perfil)

    def asignar_prioridad(self, perfil):
        prioridades = {
            "Celebridad": 0,           # Prioridad más alta
            "Cliente premium": 1,
            "Cliente frecuente": 2,
            "Cliente nuevo": 3,
            "No es cliente": 4         # Prioridad más baja
        }
        return prioridades.get(perfil, 4)  # Prioridad por defecto si no está en el diccionario

    def __lt__(self, otro):
        return self.prioridad < otro.prioridad

    def __repr__(self):
        return f"{self.nombre} ({self.perfil})"
