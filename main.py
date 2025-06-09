from plataforma import Plataforma
from video import Video
from pelicula import Pelicula
from episodio import Episodio
from serie import Serie
from temporada import Temporada

plataforma1 = Plataforma("SEBASDIOR CALVO")

pelicula1 = Pelicula(101, "EL AUTISMO DE DIEGO GARCIA", 1.7, "Realidad")
pelicula2 = Pelicula(102, "El pelo de Dior", 2.8, "Ciencia Ficción")

pelicula1.agregar_Calif(5.0)
pelicula1.agregar_Calif(4.5)

pelicula2.agregar_Calif(4.0)
pelicula2.agregar_Calif(4.2)
pelicula2.agregar_Calif(3.9)

plataforma1.agregar_video(pelicula1)
plataforma1.agregar_video(pelicula2)

serie1 = Serie(200, "Suits", 300, "Drama") 
temporada1=Temporada(1)
episodio1=Episodio(212,"Harvey Spectre el cabron", 0.5,1)
episodio1.agregar_Calif(5.0)
serie1.agregar_Calif(5.0)
temporada1.agregar_Episodio(episodio1)
serie1.agregar_Temporada(temporada1)
plataforma1.agregar_video(serie1)

plataforma1.mostrar_videos()