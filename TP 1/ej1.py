# Creamos una lista vacía donde vamos a guardar los nombres de los alumnos
alumnos = []

# Pedimos al usuario que ingrese el nombre del primer alumno
nombre = input("Ingrese el nombre del alumno: ")

# Agregamos el nombre ingresado a la lista
alumnos.append(nombre)

# Pedimos el nombre de un segundo alumno.
nombre = input("Ingrese el nombre de otro alumno: ")

# Agregamos el segundo nombre a la lista
alumnos.append(nombre)

# Mostramos en pantalla la lista con los alumnos registrados
print(alumnos)