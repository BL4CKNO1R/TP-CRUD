# Creamos una lista vacía donde vamos a guardar todos los alumnos registrados
alumnos = []

# Preguntamos cuántos alumnos quiere registrar el usuario
cantidad = int(input("¿Cuántos alumnos desea registrar? "))

# Utilizamos un bucle for para repetir el proceso la cantidad de veces indicada por el usuario
for i in range(cantidad):

    # Mostramos qué alumno estamos registrando
    print(f"Alumno {i + 1}")

    # Pedimos los datos del alumno
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = int(input("Ingrese el DNI: "))
    promedio = float(input("Ingrese el promedio: "))

    # Creamos un diccionario con los datos ingresados
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "promedio": promedio
    }

    # Agregamos el diccionario a la lista general
    alumnos.append(alumno)

# Una vez terminado el ciclo, mostramos todos los alumnos que fueron registrados
print("Lista completa de alumnos:")

for alumno in alumnos:
    print(alumno)