import random
num = []
def numeros (num):
	for i in range (1,11):
		num.append(random.randint(1,10))
	for x in num:
		print(x, "al cuadrado es: ", x**2, "y, ", x, "al cubo es: ", x**3)
	
numeros(num)