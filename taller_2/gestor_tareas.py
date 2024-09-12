# Ejercicio 2: Gestión de lista de tareas
# Enunciado: Desarrolla un programa en Java que permita gestionar una lista de tareas. El programa debe permitir al usuario realizar las siguientes operaciones:
# 	•	Agregar una nueva tarea a la lista.
# 	•	Marcar una tarea como completada.
# 	•	Mostrar todas las tareas pendientes.
# 	•	Salir del programa.
# Ejemplo de Entrada:
# 1. Agregar tarea
# 2. Marcar tarea como completada
# 3. Mostrar tareas pendientes
# 4. Salir
# Seleccione una opción: 1
# Ingrese la descripción de la tarea: Terminar el reporte
# Seleccione una opción: 1
# Ingrese la descripción de la tarea: Llamar a Juan
# Seleccione una opción: 2
# Ingrese el número de la tarea completada: 1
# Seleccione una opción: 3

# Ejemplo de Salida: Tareas pendientes:
# 1. Llamar a Juan


# profe, en este caso mis compañeros y yo intentamos utilizar una clase para comprenderla y no usamos un map
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

def mostrar_menu():
    print("\nGestión de Tareas")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas pendientes")
    print("4. Salir")

def agregar_tarea(lista_tareas):
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = Tarea(descripcion)
    lista_tareas.append(tarea)
    print("Tarea agregada con éxito.")

def marcar_tarea_completada(lista_tareas):
    if not lista_tareas:
        print("No hay tareas en la lista.")
        return

    mostrar_tareas_pendientes(lista_tareas)
    numero = int(input("Ingrese el número de la tarea completada: ")) - 1

    if 0 <= numero < len(lista_tareas):
        lista_tareas[numero].completada = True
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

def mostrar_tareas_pendientes(lista_tareas):
    print("\nTareas pendientes:")
    tareas_pendientes = [tarea for tarea in lista_tareas if not tarea.completada]

    if tareas_pendientes:
        for i, tarea in enumerate(tareas_pendientes, start=1):
            print(f"{i}. {tarea.descripcion}")
    else:
        print("No hay tareas pendientes.")


lista_tareas = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_tarea(lista_tareas)
    elif opcion == '2':
        marcar_tarea_completada(lista_tareas)
    elif opcion == '3':
        mostrar_tareas_pendientes(lista_tareas)
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")


