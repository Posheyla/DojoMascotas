from Personas.Ninja import Ninja
from Mascotas.Mascota import mascota

ninja1 = Ninja("Luisa","Chavez","galletas","pollo")
ninja1.mascotas= mascota("Pimienta","perro","galleta sabor a cordero")

ninja1.caminar().alimentar().bañar()