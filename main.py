from plataforma import Plataforma
from video import Video
from pelicula import Pelicula

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


plataforma1.mostrar_videos()
