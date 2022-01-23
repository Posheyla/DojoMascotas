from Mascota import mascota

class Perro(mascota):

    def __init__(self,name,tipo,sonido):
        super().__init__(name,tipo)
        self.sonido= sonido
