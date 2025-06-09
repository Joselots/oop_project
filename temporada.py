class Temporada:
    def __init__(self, numero: int):
        self.Numero = numero
        self.Episodios = []
        
    def agregar_Episodio(self, episodio):
        self.Episodios.append(episodio)

    