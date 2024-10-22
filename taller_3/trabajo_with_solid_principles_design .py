import random

# Clase para gestionar los tipos y multiplicadores (SRP: Solo maneja los multiplicadores de tipo)
class TipoMultiplicador:
    tabla_tipos = {
        ('Fire', 'Grass'): 2.0,  
        ('Fire', 'Water'): 0.5,  
        ('Water', 'Fire'): 2.0,  
        ('Water', 'Grass'): 0.5,  
        ('Grass', 'Water'): 2.0,  
        ('Grass', 'Fire'): 0.5,   
        ('Fire', 'Fire'): 1.0,
        ('Water', 'Water'): 1.0,
        ('Grass', 'Grass'): 1.0
    }

    
    def obtener_multiplicador(cls, tipo_atacante, tipo_defensor):
        return cls.tabla_tipos.get((tipo_atacante, tipo_defensor), 1.0)


# Clase para gestionar los ataques (SRP: Solo maneja la lógica de ataque)
class AtaqueFisico:
    def __init__(self, nombre, multiplicador):
        self.nombre = nombre
        self.multiplicador = multiplicador

    def ejecutar(self, atacante, oponente):
        tipo_atacante = atacante.tipo
        tipo_oponente = oponente.tipo
        factor_tipo = TipoMultiplicador.obtener_multiplicador(tipo_atacante, tipo_oponente)
        potencia_ataque = atacante.stats['ATTACK'] * self.multiplicador
        ataque_final = potencia_ataque * factor_tipo
        return ataque_final, self.nombre, factor_tipo


# Clase para gestionar la salud (SRP: Solo maneja salud y recibir daño)
class Salud:
    def __init__(self, valor_inicial=100):
        self.valor = valor_inicial

    def recibir_danio(self, danio):
        self.valor -= danio
        if self.valor < 0:
            self.valor = 0
        return self.valor

    def esta_vivo(self):
        return self.valor > 0


# Clase para gestionar la defensa (SRP: Solo maneja la lógica de defensa)
class Defensa:
    def __init__(self, stats_defensa):
        self.stats_defensa = stats_defensa

    def defender(self):
        multiplicador = random.choice([1, 0.5])
        return self.stats_defensa * multiplicador


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
        ataque_elegido = random.choice(self.ataques)
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


# Ejecución del programa principal
if __name__ == '__main__':
    # Crear instancias de ataques
    flamethrower = AtaqueFisico('Flamethrower', 1.5)
    surf = AtaqueFisico('Surf', 1.5)
    vine_whip = AtaqueFisico('Vine Whip', 1.2)

    # Crear instancias de Pokémon
    Charizard = Pokemon('Charizard', 'Fire', [flamethrower], {'ATTACK': 12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', [surf], {'ATTACK': 10, 'DEFENSE': 10})
    Venusaur = Pokemon('Venusaur', 'Grass', [vine_whip], {'ATTACK': 8, 'DEFENSE': 12})

    # Simulación de combate
    print(f"Salud inicial de Charizard: {Charizard.salud.valor}")
    
    ataque = Charizard.atacar(Blastoise)
    defensa = Blastoise.defender()
    danio = ataque - defensa
    if danio > 0:
        Blastoise.recibir_danio(danio)
        print(f"Charizard infligió {danio:.2f} de daño a Blastoise.")
    else:
        print(f"Blastoise bloqueó el ataque de Charizard.")
    
    print(f"Salud final de Blastoise: {Blastoise.salud.valor}")
    
    ataque = Blastoise.atacar(Charizard)
    defensa = Charizard.defender()
    danio = ataque - defensa
    if danio > 0:
        Charizard.recibir_danio(danio)
        print(f"Blastoise infligió {danio:.2f} de daño a Charizard.")
    else:
        print(f"Charizard bloqueó el ataque de Blastoise.")

    print(f"Salud final de Charizard: {Charizard.salud.valor}")
