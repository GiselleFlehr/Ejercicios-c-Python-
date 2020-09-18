#Ejercicio 5

print("Clasificación de triángulos según sus lados")
a=0
b=0
c=0

def tipo_triangulo (a,b,c):
	a,b,c=input("Ingrese el valor de los lado A B C: ").split()              
	if a == b and a == c:
		print("Equilatero")
	elif a != b and a != c:
		print("Escaleno")
	else:
		print("Isósceles")

tipo_triangulo (a,b,c)
