dia = 0
mes = 0
año = 0

def validar_fecha(dia,mes,año):
    dia = int(input("Día: "))
    while (dia<=0) or (dia>31):
        dia = int(input("Día: "))
    mes = int(input("Mes: "))
    while (mes<=0) or (mes>12):
        mes = int(input("Mes: "))
    año = int(input("Año: "))
    print("Fecha: %d/%d/%d" %(dia,mes,año))

validar_fecha(dia,mes,año)

