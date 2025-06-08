class temporada:
    def __init__(self, numero: int):
        self.Numero = numero
        self.Episodios = []
        
    def agregar_episodio(self, episodio):
        self.Episodios.append(episodio)