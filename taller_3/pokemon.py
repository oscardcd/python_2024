
import random;
from salud import Salud
from defensa import Defensa
from ataque import AtaqueFisico

# Clase principal Pokemon (SRP: Solo coordina las otras responsabilidades)

class Pokemon:
    def __init__(self, nombre, tipo, ataques, stats):
        self.nombre = nombre
        self.tipo = tipo
        self.salud = Salud()
        self.ataques = ataques
        self.stats = stats
        self.defensa = Defensa(stats['DEFENSE'])

    def atacar(self, oponente):
        ataque_elegido:AtaqueFisico = random.choice(self.ataques)
        ataque_final, nombre_ataque, factor_tipo = ataque_elegido.ejecutar(self, oponente)

        print(f"{self.nombre} usó {nombre_ataque}!")
        if factor_tipo > 1:
            print(f"¡Es super efectivo!")
        elif factor_tipo < 1:
            print(f"Es poco efectivo.")
        else:
            print(f"El ataque fue neutro.")

        return ataque_final

    def defender(self):
        return self.defensa.defender()

    def recibir_danio(self, danio):
        self.salud.recibir_danio(danio)

    def esta_vivo(self):
        return self.salud.esta_vivo()