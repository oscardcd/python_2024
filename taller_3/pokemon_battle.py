from pokemon import Pokemon
from ataque import AtaqueFisico


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
