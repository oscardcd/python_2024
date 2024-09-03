num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 <= num2 <= num3:
    orden = [num1, num2, num3]
elif num1 <= num3 <= num2:
    orden = [num1, num3, num2]
elif num2 <= num1 <= num3:
    orden = [num2, num1, num3]
elif num2 <= num3 <= num1:
    orden = [num2, num3, num1]
elif num3 <= num1 <= num2:
    orden = [num3, num1, num2]
else:
    orden = [num3, num2, num1]

print("Los números en orden ascendente son:", orden )
