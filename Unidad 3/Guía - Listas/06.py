print("Programa para identificar el mes, y la cantidad de días correspondientes")
lista = [["Enero",31],["Febrero",28],["Marzo",31],
               ["Abril",30],["Mayo",31],["Junio",30],
               ["Julio",31],["Agosto",31],["Septiembre",30],
               ["Octubre",31],["Noviembre",30],["Diciembre",30]]
mes = int(input("Ingrese un número de mes: "))
while mes >= 1 and mes <= 12:
    if mes == 1:
        print("Mes: ",lista[0][0], "- Cantidad de días: ",lista[0][1])
    elif mes == 2:
        print("Mes: ",lista[1][0], "- Cantidad de días: ",lista[1][1])
    elif mes == 3:
        print("Mes: ",lista[2][0], "- Cantidad de días: ",lista[2][1])
    elif mes == 4:
        print("Mes: ",lista[3][0], "- Cantidad de días: ",lista[3][1])
    elif mes == 5:
        print("Mes: ",lista[4][0], "- Cantidad de días: ",lista[4][1])
    elif mes == 6:
        print("Mes: ",lista[5][0], "- Cantidad de días: ",lista[5][1])
    elif mes == 7:
        print("Mes: ",lista[6][0], "- Cantidad de días: ",lista[6][1])
    elif mes == 8:
        print("Mes: ",lista[7][0], "- Cantidad de días: ",lista[7][1])
    elif mes == 9:
        print("Mes: ",lista[8][0], "- Cantidad de días: ",lista[8][1])
    elif mes == 10:
        print("Mes: ",lista[9][0], "- Cantidad de días: ",lista[9][1])
    elif mes == 11:
        print("Mes: ",lista[10][0], "- Cantidad de días: ",lista[10][1])
    elif mes == 12:
        print("Mes: ",lista[11][0], "- Cantidad de días: ",lista[11][1])
    break
