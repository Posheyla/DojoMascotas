class mascota:
    energia=50
    salud=50

    def __init__(self, name="N/A",tipo="N/A",golosinas="N/A"):
        self.name=name 
        self.tipo=tipo
        self.golosinas=golosinas

    def domir(self):
        mascota.energia += 25

    def comer(self):
        mascota.energia += 5
        mascota.salud += 10

    def jugar(self):
        mascota.salud += 5

    def ruido(self):
        if self.tipo == "perro":
            print("Guau guau !!")
        elif self.tipo == "gato":
            print("Miuau miuau !!")
        else:
            print("Mascota no reconocida")