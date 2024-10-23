from tipos import TipoMultiplicador
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