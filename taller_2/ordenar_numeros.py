# Ejercicio 3: Ordenamiento de números pares e impares en listas separadas
# Enunciado: Escribe un programa en python que solicite al usuario ingresar un número n de números enteros. Luego, el programa debe solicitar al usuario ingresar cada número y almacenarlos en un vector. Una vez que se hayan ingresado todos los números, el programa debe separar los números pares de los impares en dos listas diferentes y mostrar ambas listas.
# Ejemplo de Entrada:
# Ingrese el número de enteros: 5
# Ingrese el entero 1: 12
# Ingrese el entero 2: 7
# Ingrese el entero 3: 9
# Ingrese el entero 4: 4
# Ingrese el entero 5: 16

# Ejemplo de Salida: Números pares: [12, 4, 16]
# Números impares: [7, 9]



numeros_pares = []
numeros_impares = []

n = int(input("Ingrese el número de enteros: "))

for i in range(1, n + 1):
    numero = int(input(f"Ingrese el entero {i}: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("\nNúmeros pares:", numeros_pares)
print("Números impares:", numeros_impares)


