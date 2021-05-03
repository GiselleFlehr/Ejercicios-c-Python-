año = 0
mes = 0
dia = 0
hora = 0.0
minuto = 0.0
seg = 0.0

def es_bisiesto(año):
    bisiesto = bool
    año = int(input("Ingrese año: "))
    if ((año%4)==0 and (año%100)!=0) or (año%400)==0:
        bisiesto = True
        print("Es bisiesto.")
    else:
        bisiesto = False
        print("No es bisiesto.")

def dia_del_mes(mes,año):
    mes = 0
    mes30 = [4,6,9,11]
    mes31 = [1,3,5,7,8,10,12]
    mes = int(input("Ingrese número del mes: "))
    año = int(input("Ingrese año: "))
    if mes in mes30:
        print("Tiene 30 días.")
    elif mes in mes31:
        print("Tiene 31 días.")
    else:
        es_bisiesto(año)
        if bisiesto == True:
            print("Tiene 29 días")
        else:
            print("Tiene 28 días")

def leer_fecha(dia,mes,año):
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    print("Fecha: %d/%d/%d" %(dia,mes,año))

#Calculo del día Juliano, sacado de Wikipedia
def dia_juliano(dia,mes,año,hora,minuto,seg):
    año = float(input("Ingrese año: "))
    mes = float(input("Ingrese el mes: "))
    dia = float(input("Ingrese el día: "))
    hora = float(input("Ingrese hora: "))
    minuto = float(input("Ingrese minuto: "))
    seg = float(input("Ingrese segundos: "))
    diajul = 0.0

    if (mes == 1) or (mes == 2):
        mes = mes + 1
        año = año - 1
    
    dia = dia + (hora/24.0) + (minuto/1440.0) + (seg/86400.0)
    a = año/100.0
    b = 2 - a + (a/4.0)

    diajul = (float(365.25)*(año+float(4716)))+(float(30.6001)*(mes+1))+dia+b-float(1524.5)
    print("El día Juliano es: %d" %diajul)

print("""Menú:
1- Año bisiesto
2- Día del mes
3- Leer fecha
4- Día Juliano""")
opcion = int(input("Opción: "))

if opcion == 1:
    es_bisiesto(año)
elif opcion == 2:
    dia_del_mes(mes,año)
elif opcion == 3:
    leer_fecha(dia,mes,año)
elif opcion == 4:
    dia_juliano(dia,mes,año,hora,minuto,seg)
