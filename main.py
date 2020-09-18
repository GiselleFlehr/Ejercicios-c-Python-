#Ejercicio 1

print("Programa para determinar el objeto de mayor medida") 
medidas=0.0

def mayor_medida (medidas):
	medidas=input("Ingrese las medidas cúbicas de cada objeto: ").split()
	mayor=max(medidas)
	print("Mayor medida cúbica: ", mayor)

mayor_medida(medidas)