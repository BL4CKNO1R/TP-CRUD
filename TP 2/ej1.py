# Pedimos el nombre del alumno
nombre = input("Ingrese el nombre: ")

# Pedimos el apellido del alumno
apellido = input("Ingrese el apellido: ")

# Pedimos el DNI y lo convertimos a número entero
dni = int(input("Ingrese el DNI: "))

# Pedimos el promedio y lo convertimos a número decimal
promedio = float(input("Ingrese el promedio: "))

# Creamos un diccionario para guardar todos los datos correspondientes al alumno
alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "dni": dni,
    "promedio": promedio
}

# Mostramos el diccionario completo por pantalla
print("Datos del alumno:")
print(alumno)