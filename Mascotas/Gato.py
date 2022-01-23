from Mascota import mascota

class Gato(mascota):

    def __init__(self,name,tipo,sonido):
        super().__init__(name,tipo)
        self.sonido= sonido