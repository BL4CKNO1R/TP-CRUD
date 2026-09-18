# Creamos una lista vacía para guardar los alumnos que tengan una edad válida
alumnos = []

# Pedimos los datos del alumno
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = int(input("Ingrese el DNI: "))
edad = int(input("Ingrese la edad: "))
promedio = float(input("Ingrese el promedio: "))

# Verificamos si la edad está dentro del rango permitido
if edad >= 17 and edad <= 99:

    # Si la edad es válida, creamos el diccionario
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad,
        "promedio": promedio
    }

    # Guardamos el alumno en la lista
    alumnos.append(alumno)

    # Informamos que el registro fue creado correctamente
    print("\nAlumno registrado correctamente.")
    print(alumno)

else:
    # Si la edad no es válida, no creamos ni guardamos el registro del alumno
    print("\nError: la edad debe estar entre 17 y 99 años.")
    print("El registro fue descartado.")