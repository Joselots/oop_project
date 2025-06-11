from plataforma import Plataforma
from video import Video
from pelicula import Pelicula
from serie import Serie
from episodio import Episodio
from temporada import Temporada

plataforma1 = Plataforma("MAXSTREAM")

pelicula1 = Pelicula(101, "El vengador", 1.7, "Realidad")
pelicula2 = Pelicula(102, "Sev7n", 2.8, "Ciencia Ficción")

pelicula1.agregar_Calif(5.0)
pelicula1.agregar_Calif(4.5)

pelicula2.agregar_Calif(4.0)
pelicula2.agregar_Calif(4.2)
pelicula2.agregar_Calif(3.9)

plataforma1.agregar_video(pelicula1)
plataforma1.agregar_video(pelicula2)

serie1 = Serie(200, "Suits", 500, "Drama") 
temporada1 = Temporada(1)
episodio1 = Episodio(212, "Harvey Spectre, el comienzo", 0.5, 1, "Drama")
episodio2 = Episodio(213, "El legado del mal", 0.55, 2, "Drama")
episodio1.agregar_Calif(5.0)
episodio2.agregar_Calif(3.0)
serie1.agregar_Calif(5.0)
temporada1.agregar_Episodio(episodio1)
temporada1.agregar_Episodio(episodio2)
serie1.agregar_Temporada(temporada1)
plataforma1.agregar_video(serie1)

plataforma1.mostrar_videos()

def mostrar_menu():
    print("\n--- MENÚ DE USUARIO ---")
    print("1. Mostrar videos")
    print("2. Calificar película")
    print("3. Calificar serie")
    print("4. Calificar episodio")
    print("5. Salir")

while True:
    mostrar_menu()
    op = input("Elige una opción: ")

    if op == "1":
        plataforma1.mostrar_videos()

    elif op == "2":
        for video in plataforma1.obtener_videos():
            if isinstance(video, Pelicula):
                print(f"{video.ID} - {video.Titulo}")
        id_peli = int(input("ID película: "))
        cal = float(input("Calificación: "))
        for video in plataforma1.obtener_videos():
            if isinstance(video, Pelicula) and video.ID == id_peli:
                video.agregar_Calif(cal)

    elif op == "3":
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie):
                print(f"{video.ID} - {video.Titulo}")
        id_serie = int(input("ID serie: "))
        cal = float(input("Calificación: "))
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie) and video.ID == id_serie:
                video.agregar_Calif(cal)

    elif op == "4":
        id_serie = int(input("ID de la serie: "))
        num_temp = int(input("Número de temporada: "))
        num_epi = int(input("Número de episodio: "))
        cal = float(input("Calificación: "))
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie) and video.ID == id_serie:
                temp = video.obtener_temporada(num_temp)
                if temp:
                    ep = temp.obtener_episodio(num_epi)
                    if ep:
                        ep.agregar_Calif(cal)
                    else:
                        print("Episodio no encontrado.")
                else:
                    print("Temporada no encontrada.")

    elif op == "5":
        break
