num1 = 0
num2 = 0

print("Programa para identificar si un número es múltpiplo de otro")
def EsMultiplo(num1,num2):
    num1,num2 = input("Ingrese 2 números, separados por un espacio: ").split()
    if (int(num1) % int(num2)) == 0:
        print(num1," es múltiplo de ",num2)
    else:
        print("Los números ingresados no son múltiplos")

EsMultiplo(num1,num2)
