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