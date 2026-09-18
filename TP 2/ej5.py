# Creamos una función que se encargará de registrar un nuevo alumno
def registrar_nuevo_alumno():

    # Pedimos los datos que son de tipo texto
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    # Utilizamos try para intentar convertir los datos numéricos
    try:

        # Pedimos el DNI y lo convertimos a entero
        dni = int(input("Ingrese el DNI: "))

        # Pedimos la edad y la convertimos a entero
        edad = int(input("Ingrese la edad: "))

    # Si el usuario escribe letras en lugar de números, se produce un ValueError
    except ValueError:

        # Mostramos un mensaje indicando el error
        print("Error: el DNI y la edad deben ser números.")

        # Terminamos la función sin crear el alumno
        return

    # Si los datos numéricos fueron correctos, creamos el diccionario del alumno.
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad
    }

    # Abrimos el archivo alumnos.txt en modo "a" y "a" significa append, es decir, agregar al final sin borrar los registros anteriores
    with open("alumnos.txt", "a", encoding="utf-8") as archivo:

        # Escribimos los datos del alumno en el archivo
        archivo.write(
            f"Nombre: {alumno['nombre']}"
            f"Apellido: {alumno['apellido']}"
            f"DNI: {alumno['dni']}"
            f"Edad: {alumno['edad']}"
            "-------------------------"
        )

    # Informamos que el alumno fue guardado correctamente
    print("Alumno registrado y guardado correctamente.")

# Llamamos a la función para ejecutar el proceso de registro
registrar_nuevo_alumno()