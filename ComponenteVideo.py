from abc import ABC, abstractmethod

class ComponenteVideo(ABC):
    @abstractmethod
    def mostrar_Info(self):
        pass

    @abstractmethod
    def agregar_Calif(self, calificacion: float):
        pass

    @abstractmethod
    def promedio_Calif(self):
        pass
