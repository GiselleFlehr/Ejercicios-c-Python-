#Ejercicio 6

print("Calcular Resistencias en Paralelo.")

n=0
R=0
Req=0

def resist_paralelo(n,R):
	Rt=0
	n=int(input("Cantidad de Resistencias: "))
	for x in range (1,n+1):
		R=float(input("Valor Resistencia: "))
		Rt=Rt+(1/R)
	Req=1/Rt
	print("Resistencia equivalente: ",Req)	

resist_paralelo (n,R)	
