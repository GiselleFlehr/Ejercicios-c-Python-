tempmin = 0.0
tempmax = 0.0

print("Programa para calcular la temperatura media, de x cantidad de días")

def temperatura_media(tempmin,tempmax):
    dias = 0
    dias = int(input("Cantidad de días a evaluar: "))
    for i in range (0,dias):
        tempmin,tempmax = input("Ingrese temperatura mínima y máxima, separados por un espacio: ").split()
        tempmedia = 0.0
        tempmedia = (float(tempmin)+float(tempmax))/2
        print("La temperatura media es: %d" %tempmedia)

temperatura_media(tempmin,tempmax)
