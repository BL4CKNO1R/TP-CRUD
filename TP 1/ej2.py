# Creamos un diccionario vacío para guardar la información de un alumno
alumno = {}

# Pedimos al usuario el nombre del alumno
nombre = input("Ingrese el nombre del alumno: ")

# Pedimos la edad del alumno
edad = input("Ingrese la edad del alumno: ")

# Pedimos el curso al que pertenece el alumno
curso = input("Ingrese el curso del alumno: ")

# Guardamos el nombre dentro del diccionario, "nombre" es la clave y la variable nombre contiene su valor
alumno["nombre"] = nombre

# Guardamos la edad dentro del diccionario
alumno["edad"] = edad

# Guardamos el curso dentro del diccionario
alumno["curso"] = curso

# Mostramos en pantalla toda la información que guardamos en el diccionario
print("Datos del alumno:")
print(alumno)