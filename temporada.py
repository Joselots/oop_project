class Temporada:
    def __init__(self, numero: int):
        self.numero = numero
        self.episodios = []
        
    def agregar_Episodio(self, episodio):
        self.episodios.append(episodio)

    def obtener_episodio(self, numero):
        for ep in self.episodios:
            if ep.numero == numero:
                return ep
        return None


    