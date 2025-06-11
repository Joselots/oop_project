from video import Video
class Serie(Video):

    def __init__(self, id: int, titulo: str,duracion:float, genero: str):
        super().__init__(id, titulo, duracion, genero)
        self.Temporadas = []
    def agregar_Temporada(self, temporada):
        self.Temporadas.append(temporada)

    def mostrar_Info(self):
        super().mostrar_Info()
        print(f"Número de temporadas: {len(self.Temporadas)}")
        for temporada in self.Temporadas:
            print(f" Temporada {temporada.Numero}:")
        for episodio in temporada.Episodios:
            episodio.mostrar_Info()