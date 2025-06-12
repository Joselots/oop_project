from plataforma import Plataforma
from video import Video
from pelicula import Pelicula
from serie import Serie
from episodio import Episodio
from temporada import Temporada

plataforma1 = Plataforma("MAXSTREAM")

pelicula1 = Pelicula(101, "Pulp Fiction", 2.5, "Crimen/Suspenso")
pelicula2 = Pelicula(102, "Se7en", 2.0, "Crimen/Terror")
pelicula3 = Pelicula(103, "Fight Club", 2.2, "Acción/Crimen")
pelicula4 = Pelicula(104, "Bastardos sin gloria", 2.5, "Belico, Acción")
pelicula5 = Pelicula(105, "Baby Driver", 1.9, "Acción/Crimen")

#pelicula1.agregar_Calif(5.0)
#pelicula1.agregar_Calif(4.5)
#pelicula2.agregar_Calif(4.0)
#pelicula2.agregar_Calif(4.2)
#pelicula2.agregar_Calif(3.9)
plataforma1.agregar_video(pelicula1)
plataforma1.agregar_video(pelicula2)
plataforma1.agregar_video(pelicula3)
plataforma1.agregar_video(pelicula4)
plataforma1.agregar_video(pelicula5)

serie1 = Serie(101, "Breaking Bad", 60, "Drama") 
temporada1_BB = Temporada(1)
temporada5_BB = Temporada(5)
episodio1_BB = Episodio(54, "Principio del Fin", 1, 1, "Drama")
episodio14_BB = Episodio(88, "Ozymandias", 0.8, 14, "Drama")
episodio1_BB.agregar_Calif(5.0)
serie1.agregar_Calif(5.0)
temporada1_BB.agregar_Episodio(episodio1_BB)
temporada5_BB.agregar_Episodio(episodio14_BB)
serie1.agregar_Temporada(temporada1_BB)
serie1.agregar_Temporada(temporada5_BB)
plataforma1.agregar_video(serie1)

serie2 = Serie(102, "Dr House", 120, "Drama Médico")
temporada1_House=Temporada(1)
temporada2_House=Temporada(2)
episodio1_House=Episodio(2,"House-Pilot",0.7,1,"Drama Médico")
episodio2_House=Episodio(3,"Paternity",0.67,2,"Drama Médico")
episodio41_House=Episodio(45,"All in",0.8,41,"Drama Médico")
episodio43_House=Episodio(47,"House vs. God", 0.8,43,"Drama Médico")
temporada1_House.agregar_Episodio(episodio1_House)
temporada1_House.agregar_Episodio(episodio2_House)
temporada2_House.agregar_Episodio(episodio41_House)
temporada2_House.agregar_Episodio(episodio43_House)
serie2.agregar_Temporada(temporada1_House)
serie2.agregar_Temporada(temporada2_House)
plataforma1.agregar_video(serie2)


def mostrar_menu():
    print("\nPLATAFORMA FINAL: PROGRAMACION ORIENTADA A OBJETOS")
    print("1. Mostrar videos por calificación o género")
    print("2. Mostrar episodios de una serie por calificación")
    print("3. Mostrar películas por calificación")
    print("4. Calificar un video por título")
    print("0. Salir")

while True:
    mostrar_menu()
    op = input("Elige una opción: ")

    if op == "1":
        filtro = input("¿Filtrar por calificación o por género? (c/g): ").lower()
        if filtro == "c":
            cal_min = float(input("Mostrar videos con calificación mayor o igual a: "))
            for video in plataforma1.obtener_videos():
                if video.promedio_Calif() >= cal_min:
                    video.mostrar_Info()
        elif filtro == "g":
            genero = input("Género a buscar (ej. Acción, Drama): ").lower()
            for video in plataforma1.obtener_videos():
                if genero in video.Genero.lower():
                    video.mostrar_Info()
        else:
            print("Opción inválida.")

    elif op == "2":
        nombre = input("Nombre de la serie: ").lower()
        cal_min = float(input("Mostrar episodios con calificación mayor o igual a: "))
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie) and nombre in video.Titulo.lower():
                for temp in video.temporadas:
                    for ep in temp.episodios:
                        if ep.promedio_Calif() >= cal_min:
                            ep.mostrar_Info()

    elif op == "3":
        cal_min = float(input("Mostrar películas con calificación mayor o igual a: "))
        for video in plataforma1.obtener_videos():
            if isinstance(video, Pelicula) and video.promedio_Calif() >= cal_min:
                video.mostrar_Info()

    elif op == "4":
        titulo = input("Escribe el título del video a calificar: ").lower()
        for video in plataforma1.obtener_videos():
            if titulo in video.Titulo.lower():
                cal = float(input("Calificación: "))
                video.agregar_Calif(cal)
                print("Calificación agregada.")
                break
        else:
            print("Video no encontrado.")

    elif op == "0":
        print("Gracias por usar la plataforma.")
        break

    else:
        print("Opción inválida.")
