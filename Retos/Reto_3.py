num = 0
fact = 1

def factorial (num, fact):
    num = int(input("Ingrese un número para calcular su factorial: "))
    for n in range(1, num+1):
        fact = fact * n
    return fact

print(factorial(num,fact))
