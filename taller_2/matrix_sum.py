# Ejercicio 4: Suma de matrices
# Enunciado: Desarrolla un programa en JAVA que permita al usuario ingresar dos matrices bidimensionales de tamaño n x m.
# El programa debe sumar ambas matrices y mostrar el resultado en una nueva matriz.
# Si las matrices no tienen las mismas dimensiones, el programa debe mostrar un mensaje de error.
# Ejemplo de Entrada:
# Ingrese el número de filas: 2
# Ingrese el número de columnas: 2
# Ingrese la primera matriz:
# 1 2
# 3 4
# Ingrese la segunda matriz:
# 5 6
# 7 8

# Ejemplo de Salida:
# Matriz resultante:
# 6 8
# 10 12

def ingresar_matriz(filas, columnas, nombre):
    print(f"Ingrese la {nombre} matriz (numeros separados por espacio):")
    matriz = []
    for i in range(filas):
        fila = list(map(int, input().split()))
        if len(fila) != columnas:
           print(f"La fila debe tener exactamente {columnas} columnas.")
           ingresar_matriz(filas, columnas, nombre)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        fila_resultado = [matriz1[i][j] + matriz2[i][j] for j in range(columnas)]
        resultado.append(fila_resultado)
    return resultado

def imprimir_matriz(matriz):
    print("resultado de la suma de matrices:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz1 = ingresar_matriz(filas, columnas, "primera")
matriz2 = ingresar_matriz(filas, columnas, "segunda")

resultado = sumar_matrices(matriz1, matriz2)

imprimir_matriz(resultado)






