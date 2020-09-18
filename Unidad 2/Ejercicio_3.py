#Ejercicio 3

print("Programa para reconocer si un cuadrilátero es un cuadrado o un rectángulo")

base=0
altura=0

def cuadrilatero (base,altura):
	base,altura=input("Ingrese la base y la altura: ").split()
	print("Base: ",base,". Altura: ",altura)
	if base == altura:
		print("Cuadrado!")
	else:
		print("Rectángulo!")
		
cuadrilatero(base,altura)			
