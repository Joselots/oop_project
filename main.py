from plataforma import Plataforma
from video import Video
from pelicula import Pelicula
from episodio import Episodio
from serie import Serie
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
temporada1=Temporada(1)
episodio1=Episodio(212,"Harvey Spectre, el comiezo", 0.5,1)
episodio2=Episodio(213,"El legado del mal",0.55,2)
episodio1.agregar_Calif(5.0)
episodio2.agregar_Calif(3.0)
serie1.agregar_Calif(5.0)
temporada1.agregar_Episodio(episodio1)
temporada1.agregar_Episodio(episodio2)
serie1.agregar_Temporada(temporada1)
plataforma1.agregar_video(serie1)

plataforma1.mostrar_videos()