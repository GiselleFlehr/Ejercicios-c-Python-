print("Calcular el factorial de x número")

def factorial(n):
	if n == 1:
	    return 1
	else:
	    return n*factorial(n-1)

n = int(input("Ingrese un número: "))
x = factorial(n)
print("El factorial de ",n,"es ",x)
