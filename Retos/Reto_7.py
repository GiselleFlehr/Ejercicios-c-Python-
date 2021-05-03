print("Programa para identificar el valor de N, según 3 números dados")

num1 = 0
num2 = 0
num3 = 0

def numero_N (num1, num2, num3):
    modulo = 0
    num_n = 1
    for num_n in range (1,101):
        modulo = num_n % int(num3)
        while (num_n > int(num1)) and (num_n < int(num2)) and (modulo == 0):
            return num_n
    
num1, num2, num3 = input("Ingrese 3 números: ").split()
if (int(num1) >= 1 and int(num1) <= 100) and (int(num2) >= 1 and int(num2) <= 100) and (int(num3) >= 1 and int(num3) <= 100):
    numero_N (num1, num2, num3)
    if (numero_N (num1, num2, num3)) == None:
        print("0")
    else:
        print("El valor de N es: ", numero_N (num1, num2, num3)) 
else:
        print("Valor fuera de rango")
