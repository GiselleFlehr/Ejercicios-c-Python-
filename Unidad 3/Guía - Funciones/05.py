print("Programa para identificar números máximos y mínimos de una lista")

numero = []
def calcularMaxMin(numero):
    return (max(numero),min(numero))

cant_num = 0
cant_num = int(input("Cantidad de número a ingresar: "))
for i in range(0,cant_num):
    numero.append(int(input("Ingrese número: ")))
calcularMaxMin(numero)
print("Número máximo: %d - Número mínimo: %d" %(max(numero),min(numero)))

