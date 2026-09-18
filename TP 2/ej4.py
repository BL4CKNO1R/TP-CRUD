# Creamos una lista vacía para guardar todos los alumnos registrados
alumnos = []

# Utilizamos while True porque queremos permitir registrar alumnos indefinidamente
while True:

    # Pedimos el nombre del alumno
    nombre = input(
        "Ingrese el nombre del alumno (o escriba SALIR): "
    )

    # Comprobamos si el usuario quiere terminar
    if nombre.upper() == "SALIR":

        # Salimos del bucle
        break

    # Pedimos el resto de los datos del alumno
    apellido = input("Ingrese el apellido: ")
    dni = int(input("Ingrese el DNI: "))
    edad = int(input("Ingrese la edad: "))
    promedio = float(input("Ingrese el promedio: "))

    # Creamos una variable para saber si el DNI ya fue utilizado anteriormente
    dni_existente = False

    # Recorremos todos los alumnos registrados para buscar el DNI ingresado
    for alumno in alumnos:

        # Comparamos el DNI del alumno guardado con el DNI que acaba de ingresar el usuario
        if alumno["dni"] == dni:

            # Encontramos un DNI repetido
            dni_existente = True

            # No necesitamos continuar buscando
            break

    # Comprobamos el resultado de la búsqueda
    if dni_existente:

        # Si el DNI ya existe, rechazamos el registro
        print("Error: ese DNI ya está registrado.")
        print("El alumno no fue agregado.")

    else:

        # Si el DNI no existe, creamos el nuevo alumno
        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "edad": edad,
            "promedio": promedio
        }

        # Agregamos el alumno a la lista
        alumnos.append(alumno)

        print("Alumno registrado correctamente.")

# Cuando termina el while, mostramos todos los alumnos que fueron registrados
print("Alumnos registrados:")

for alumno in alumnos:
    print(alumno)