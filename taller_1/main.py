import os

def ejecutar_tabla_multiplicar():
    import multiplication_table

def ejecutar_descuento():
    import validate_discount

def ejecutar_promedio():
    import average

def ejecutar_clasificacion_triangulo():
    import triangle_type

def ejecutar_anio_bisiesto():
    import validate_leap_year

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Tabla de multiplicar")
    print("2. Cálculo de descuento")
    print("3. Cálculo de promedio")
    print("4. Clasificación de triángulos")
    print("5. Año bisiesto")
    print("6. Salir \n")


while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        ejecutar_tabla_multiplicar()
    elif opcion == '2':
        ejecutar_descuento()
    elif opcion == '3':
        ejecutar_promedio()
    elif opcion == '4':
        ejecutar_clasificacion_triangulo()
    elif opcion == '5':
        ejecutar_anio_bisiesto()
    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
