from video import Video

class Episodio(Video):
     def __init__(self, id: int, titulo: str, duracion: float, numero_episodio: int):
        super().__init__(id,titulo, duracion, numero_episodio)
        self.Numero = numero_episodio
     def mostrar_Info(self):
        print(f"  Episodio {self.Numero}: {self.Titulo} ({self.Duracion} horas)")
        print(f"    Promedio de calificación: {self.promedio_Calif():.2f}")
