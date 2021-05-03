def alumnos_edad():
    nombre = []
    edad = []
    print("Programa para la carga de alumnos y su edad. Para salir del sistema ingrese * ")
    n = input("Ingrese nombre del alumno: ")
    while n != "*":
        nombre.append(n)
        edad.append(int(input("Ingrese edad del alumno: ")))
        n = input("Ingrese nombre del alumno: ")

    for i in range (0, len(nombre)):
        if edad[i] >= 18 and edad[i] <= 21:
            print(nombre[i].upper(), "es mayor de edad.")

    for i in range (0, len(nombre)):
        if edad[i] > 21:
            print(nombre[i].upper(), "es mayor de 21 años.")

alumnos_edad()
