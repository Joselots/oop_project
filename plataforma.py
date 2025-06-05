class Plataforma:
    def __init__(self, nombrePlataforma: str):
        self.__nombrePlataforma = nombrePlataforma
        self.__videos = []  

    def agregar_video(self, video):
        self.__videos.append(video)

    def mostrar_videos(self):
        for video in self.__videos:
            video.mostrar_Info()

    def obtener_nombre(self):
        return self.__nombrePlataforma

    def obtener_videos(self):
        return self.__videos
