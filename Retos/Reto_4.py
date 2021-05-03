ang1 = 0
ang2 = 0
ang3 = 0
ang4 = 0
ang5 = 0
cant_lado = 0

print("Programa para identificar polígonos regulares, de 3,4 y 5 lados.")

def poligono (cant_lado):
    cant_lado = int(input("Ingrese cantidad de lados del polígono: "))
    if cant_lado == 3:
        ang1, ang2, ang3 = input("Ingrese los ángulos del polígono, separados por un espacio: ").split()
        if ang1 == ang2 == ang3:
            print("Es regular")
        else:
            print("Indeterminado")
    elif cant_lado == 4:
        ang1, ang2, ang3, ang4 = input("Ingrese los ángulos del polígono, separados por un espacio: ").split()
        if ang1 == ang2 == ang3 == ang4:
            print("Es regular")
        else:
            print("Indeterminado")
    elif cant_lado == 5:
        ang1, ang2, ang3, ang4, ang5 = input("Ingrese los ángulos del polígono, separados por un espacio: ").split()
        if ang1 == ang2 == ang3 == ang4:
            print("Es regular")
        else:
            print("Indeterminado")
    else:
        print("Cantidad de ángulos fuera de rango!")

poligono (cant_lado)
