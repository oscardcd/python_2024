# Ejercicio 5: Cálculo del factorial de un número (Python)
# Enunciado: Desarrolla un programa en python que solicite al usuario ingresar un número entero positivo n. El programa debe calcular y mostrar el factorial de n.
# Ejemplo de Entrada:
# Ingrese un número entero positivo: 5

# Ejemplo de Salida:
# El factorial de 5 es: 120

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n < 0:
        print("El número debe ser entero positivo.")
    break
      
factorial = calcular_factorial(n)
print(f"El factorial de {n} es: {factorial}")


