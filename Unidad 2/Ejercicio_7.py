#Ejercicio 7

print("Repetir puntos suspensivos")

cant=0
def pto_suspensivo (cant):
	cant=int(input("Ingrese la cantidad de veces: "))
	for i in range (1,cant+1):
		print("...", end=" ")

pto_suspensivo (cant)		
