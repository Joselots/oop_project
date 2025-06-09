from video import Video
class Serie(Video):

    def __init__(self, id: int, titulo: str,duracion:float, genero: str):
        super().__init__(id, titulo, duracion, genero)
        self.Temporadas = []
    def agregar_Temporada(self, temporada):
        self.Temporadas.append(temporada)

    def mostrar_Info(self):
        print(f"ID: {self.ID}")
        print(f"Título: {self.Titulo}")
        print(f"Duración: {self.Duracion} horas")
        print(f"Género: {self.Genero}")
        print(f"Promedio de calificación: {self.promedio_Calif():.2f}")