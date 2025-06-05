class Video:
    def __init__(self, id: int, titulo: str, duracion: float, genero: str):
        self.ID = id
        self.Titulo = titulo
        self.Duracion = duracion
        self.Genero = genero
        self.Calificacion = []  

    def agregar_Calif(self, calificacion: float):
        self.Calificacion.append(calificacion)

    def mostrar_Calif(self):
        print("Calificaciones:", self.Calificacion)

    def promedio_Calif(self):
        if not self.Calificacion:
            return 0
        return sum(self.Calificacion) / len(self.Calificacion)

    def mostrar_Info(self):
        print(f"ID: {self.ID}")
        print(f"Título: {self.Titulo}")
        print(f"Duración: {self.Duracion} horas")
        print(f"Género: {self.Genero}")
        print(f"Promedio de calificación: {self.promedio_Calif():.2f}")

    def __reproducir_Video(self): 
        print(f"Reproduciendo '{self.Titulo}'...")
