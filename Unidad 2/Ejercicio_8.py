#Ejercicio 8

print("Identificar palabras plurales y singulares")

palabra=""

def plural_sing (palabra):
	palabra=input("Ingrese una palabra: ")
	if (palabra[-1]) == "s":
		print("Es Plural!")
	else:
		print("Es singular!")

plural_sing(palabra)			
