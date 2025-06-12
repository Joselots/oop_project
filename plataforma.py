from pelicula import Pelicula
from serie import Serie
class Plataforma:
    def __init__(self, nombrePlataforma: str):
        self.__nombrePlataforma = nombrePlataforma
        self.__videos = []  

    def agregar_video(self, video):
        self.__videos.append(video)

    def mostrar_videos(self):
        for video in self.__videos:
            video.mostrar_Info()

    def mostrar_peliculas(self):
        print(f"\n--- Películas ---")
        for video in self.__videos:
            if isinstance(video, Pelicula):
                video.mostrar_Info()

    def mostrar_series(self):
        print(f"\n--- Series ---")
        for video in self.__videos:
            if isinstance(video, Serie):
                video.mostrar_Info()

    def obtener_nombre(self):
        return self.__nombrePlataforma

    def obtener_videos(self):
        return self.__videos
