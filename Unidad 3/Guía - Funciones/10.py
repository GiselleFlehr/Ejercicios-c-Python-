horas = 0
minutos = 0
seg = 0

def convertir_hms(horas,minutos,seg):
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    seg = int(input("Segundos: "))
    seg = (horas * 3600) + (minutos * 60) + seg
    print("Segundos totales: %d" %seg)

def convertir_segundos(seg):
    seg = int(input("Segundos: "))
    horas = (seg // 60) // 60
    minutos = (seg // 60) % 60
    seg = seg % 60
    print("Horas: %d - Minutos: %d - Segundos: %d" %(horas,minutos,seg))

print("""Conversor H-M-S
Menú:
1- Convertir a Segundos
2- Convertir a Horas-Minutos-Segundos
3- Salir""")
opcion = int(input("Opción: "))

if opcion == 1:
    convertir_hms(horas,minutos,seg)
elif opcion == 2:
    convertir_segundos(seg)
elif opcion == 3:
    print("Salió del menú principal")

