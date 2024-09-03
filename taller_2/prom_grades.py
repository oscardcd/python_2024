# Ejercicio 1: Cálculo de promedio de calificaciones

# Enunciado: Escribe un programa en Python que solicite al usuario ingresar un número n de calificaciones.
#  Luego, el programa debe solicitar al usuario ingresar cada calificación y almacenarlas en un vector. 
#  Una vez que se hayan ingresado todas las calificaciones, el programa debe calcular y mostrar el promedio de las 
#  calificaciones. Además, el programa debe indicar si el estudiante aprobó o reprobó, considerando que se
#  aprueba con un promedio igual o mayor a 60.

# Ejemplo de Entrada:
# Ingrese el número de calificaciones: 4
# Ingrese la calificación 1: 75
# Ingrese la calificación 2: 85
# Ingrese la calificación 3: 60
# Ingrese la calificación 4: 70

# Ejemplo de Salida:
# Promedio de calificaciones: 72.5
# Estado: Aprobado


numberGrades:float=float(input('ingrese el numero de notas: '))
notes:int=0
notesSum:list[float]=[]


while notes!=numberGrades:
    notesSum.append(float(input(f"Ingrese la calificación {notes+1}: ")))
    notes+=1

prom:float =sum(notesSum)/numberGrades

studentStatus:str=''
if prom>=60:
    studentStatus='aprobo'
else:
    studentStatus='reprobo'


print(f"Promedio de calificaciones es: {prom:.1f}\n Estado: {studentStatus}")


#hola care chimbo