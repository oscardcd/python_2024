
import random;

# Clase para gestionar la defensa (SRP: Solo maneja la lógica de defensa)
class Defensa:
    def __init__(self, stats_defensa):
        self.stats_defensa = stats_defensa

    def defender(self):
        multiplicador = random.choice([1, 0.5])
        return self.stats_defensa * multiplicador
