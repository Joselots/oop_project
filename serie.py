from video import Video

class Serie(Video):
    def __init__(self, id: int, titulo: str, duracion: float, genero: str):
        super().__init__(id, titulo, duracion, genero)
        self.temporadas = []

    def agregar_Temporada(self, temporada):
        self.temporadas.append(temporada)

    def mostrar_Info(self):
        super().mostrar_Info()
        print(f"Número de temporadas: {len(self.temporadas)}")
        for temporada in self.temporadas:
            print(f" Temporada {temporada.numero}:")
            for episodio in temporada.episodios:
                episodio.mostrar_Info()

    def obtener_temporada(self, numero):
        for temp in self.temporadas:
            if temp.numero == numero:
                return temp
        return None
