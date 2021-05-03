print("Programa para averiguar MCD de 2 números, con método Euclides")

def calculo_MCD(num1, num2):
    if num1 > num2:
        while True:
            resto = num1 % num2
            if resto == 0:
                return num2
            else:
                num1 = num2
                num2 = resto

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número menor al anterior: "))
print("El MCD es: ",calculo_MCD(num1, num2))
