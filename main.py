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
    print("\n--- MENÚ DE USUARIO ---")
    print("1. Mostrar videos")
    print("2. Mostrar peliculas")
    print("3. Mostrar series")
    print("4. Calificar pelicula")
    print("5. Calificar temporada")
    print("6. Calificar episodio")
    print("7. Salir")

while True:
    mostrar_menu()
    op = input("Elige una opción: ")

    if op == "1":
        plataforma1.mostrar_videos()

    elif op == "2":
        plataforma1.mostrar_peliculas()

    elif op == "3":
        plataforma1.mostrar_series()

    elif op == "4":
        for video in plataforma1.obtener_videos():
            if isinstance(video, Pelicula):
                print(f"{video.ID} - {video.Titulo}")
        id_peli = int(input("ID película: "))
        cal = float(input("Calificación: "))
        for video in plataforma1.obtener_videos():
            if isinstance(video, Pelicula) and video.ID == id_peli:
                video.agregar_Calif(cal)

    elif op == "5":
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie):
                print(f"{video.ID} - {video.Titulo}")
        id_serie = int(input("ID serie: "))
        cal = float(input("Calificación: "))
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie) and video.ID == id_serie:
                video.agregar_Calif(cal)

    elif op == "6":
        print("\nSeries disponibles:")
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie):
                print(f"{video.ID} - {video.Titulo}")
        
        id_serie = int(input("Elige el ID de la serie: "))
        
        serie_seleccionada = None
        for video in plataforma1.obtener_videos():
            if isinstance(video, Serie) and video.ID == id_serie:
                serie_seleccionada = video
                break
        
        if serie_seleccionada:
            print("\nTemporadas disponibles:")
            for temp in serie_seleccionada.temporadas:
                print(f"Temporada {temp.numero}")
            num_temp = int(input("Elige el número de temporada: "))
            temporada = serie_seleccionada.obtener_temporada(num_temp)
            
            if temporada:
                print("\nEpisodios disponibles:")
                for ep in temporada.episodios:
                    print(f"Episodio {ep.numero}: {ep.Titulo}")
                
                num_epi = int(input("Elige el número de episodio: "))
                ep = temporada.obtener_episodio(num_epi)
                
                if ep:
                    cal = float(input("Calificación: "))
                    ep.agregar_Calif(cal)
                    print("Calificación agregada.")
                else:
                    print("Episodio no encontrado.")
            else:
                print("Temporada no encontrada.")
        else:
            print("Serie no encontrada.")
    elif op=="7":
        break