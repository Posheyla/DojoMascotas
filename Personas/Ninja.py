from Mascotas.Mascota import mascota

class Ninja:

    def __init__(self,nombre="N/A",apellido="N/A",premio="N/A",comida_mascota="N/A"):
        self.nombre=nombre
        self.apellido=apellido
        self.premio=premio
        self.comida_mascota=comida_mascota
        self.mascotas= mascota()

    def caminar(self):
        print("Sacando a pasear a {}".format(self.mascotas.name))
        self.mascotas.jugar()
        return self

    def alimentar(self):
        print("Darle de comer {} a {} ".format(self.comida_mascota,self.mascotas.name))
        self.mascotas.comer()
        return self

    def bañar(self):
        print("Darle un baño a {}".format(self.mascotas.name))
        self.mascotas.ruido()
        return self

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Apellido:",self.apellido)
        print("Mascota:",self.mascotas.name)
        return self

