# Ejercicio 6: Cifrado César (Python)
# Enunciado: Implementa un programa en python que permite cifrar un mensaje utilizando el cifrado César. El programa debe solicitar al usuario ingresar un mensaje y un valor de desplazamiento k. Luego debe cifrar el mensaje moviendo cada letra k posiciones hacia la derecha en el alfabeto.
# Ejemplo de Entrada:
# Ingrese un mensaje: Hola Mundo
# Ingrese el valor de desplazamiento: 3
# Ejemplo de Salida:
# Mensaje cifrado: Krod Pxqgr

def cifrar_cesar(mensaje, desplazamiento):
    resultado = []
    for char in mensaje:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado.append(nuevo_char)
        else:
            resultado.append(char)
    return ''.join(resultado)


mensaje = input("Ingrese un mensaje: ")
desplazamiento = int(input("Ingrese el valor de desplazamiento para crifrar: "))

mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)

print("Mensaje cifrado:", mensaje_cifrado)


