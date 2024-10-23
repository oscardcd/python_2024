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
        return cls.tabla_tipos.get([tipo_atacante, tipo_defensor])