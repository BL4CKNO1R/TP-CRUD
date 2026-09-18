# Creamos una lista vacía donde vamos a guardar todos los alumnos registrados
alumnos = []

# Creamos un bucle infinito para poder registrar alumnos continuamente
while True:

    # Pedimos al usuario que ingrese el nombre del alumno
    nombre = input("Ingrese el nombre del alumno (o escriba 'salir' para terminar): ")

    # Comprobamos si el usuario escribió "salir"
    if nombre.lower() == "salir":
        # break termina el bucle y permite finalizar el registro de alumnos
        break

    # Creamos un diccionario para representar al alumno que acabamos de registrar
    alumno = {
        "nombre": nombre
    }

    # Agregamos el diccionario del alumno a la lista de alumnos
    alumnos.append(alumno)

# Una vez terminado el bucle, mostramos la cantidad total de alumnos registrados
print("Cantidad de alumnos registrados:", len(alumnos))

# Mostramos también la lista completa con todos los alumnos creados
print("Alumnos registrados:")
print(alumnos)