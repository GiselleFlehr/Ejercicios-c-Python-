poligonos = ["Triángulo","Cuadrilátero","Pentágono","Hexágono","Heptágono"]
lados = 0

print("Programa para clasificar polígonos según la cantidad de lados.")

def clas_poligonos (lados):
    lados = int(input("Ingrese cantidad de lados: "))
    while (lados >= 3) and (lados <= 7):
        if lados == 3:
            print("El polígono es: " + poligonos[0])
        elif lados == 4:
            print("El polígono es: " + poligonos[1])
        elif lados == 5:
            print("El polígono es: " + poligonos[2])
        elif lados == 6:
            print("El polígono es: " + poligonos[3])
        elif lados == 7:
            print("El polígono es: " + poligonos[4])
        else:
            print("ERROR - Valor fuera de rango!")
        break 

clas_poligonos (lados)