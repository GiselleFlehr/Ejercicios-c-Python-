#Ejercicio 4

print("Suma de números pares e impares")

num=0

def numeros (num):
	num=input("Ingrese una lista de números: ").split()
	pares=[]
	impares=[]
	
	for n in (num):
		if (n % 2) == 0:
			pares.append(n)
		else:
			impares.append(n)
	print("Suma de números pares: ", sum(pares))
	print("Suma de números impares: ", sum(impares))	

numeros (num)	
