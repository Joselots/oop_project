from video import Video

class Episodio(Video):
    def __init__(self, id: int, titulo: str, duracion: float, numero_episodio: int, genero: str):
        super().__init__(id, titulo, duracion, genero)
        self.numero = numero_episodio
        print(f"  Episodio {self.numero}: {self.Titulo}...")

    def mostrar_Info(self):
        print(f"  Episodio {self.numero}: {self.Titulo} ({self.Duracion} horas)")
        print(f"    Promedio de calificación: {self.promedio_Calif():.2f}")

