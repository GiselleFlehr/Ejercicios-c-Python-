num1 = 0
num2 = 0
n1 = 0
d1 = 0
n2 = 0
d2 = 0
num =0
denom = 0

def leer_fraccion(num1,num2):
    num1=int(input("Ingrese numerador: "))
    num2=int(input("Ingrese denominador: "))
    if num2 == 1:
        print(num1)
    else:
        fraccion = 0.0
        fraccion = (num1/num2)
        print("Fracción: %d/%d - %d"%(num1,num2,fraccion))

def calculo_MCD(num1, num2):
    if num1 > num2:
        while True:
            resto = num1 % num2
            if resto == 0:
                return num2
            else:
                num1 = num2
                num2 = resto
                
def sumar_fracciones(n1,d1,n2,d2):
    n1=int(input("Numerador: "))
    d1=int(input("Denominador: "))
    n2=int(input("Numerador: "))
    d2=int(input("Denominador: "))
    num=(n1*d2)+(d1*n2)
    denom=d1*d2
    print("Resultado: %d/%d"%(num,denom))

def restar_fracciones(n1,d1,n2,d2):
    n1=int(input("Numerador: "))
    d1=int(input("Denominador: "))
    n2=int(input("Numerador: "))
    d2=int(input("Denominador: "))
    num=(n1*d2)-(d1*n2)
    denom=d1*d2
    print("Resultado: %d/%d"%(num,denom))

def multiplicar_fracciones(n1,d1,n2,d2):
    n1=int(input("Numerador: "))
    d1=int(input("Denominador: "))
    n2=int(input("Numerador: "))
    d2=int(input("Denominador: "))
    num=n1*n2
    denom=d1*d2
    print("Resultado: %d/%d"%(num,denom))

def dividir_fracciones(n1,d1,n2,d2):
    n1=int(input("Numerador: "))
    d1=int(input("Denominador: "))
    n2=int(input("Numerador: "))
    d2=int(input("Denominador: "))
    num=n1*d2
    denom=d1*n2
    print("Resultado: %d/%d"%(num,denom))

print("""Operaciones artméticas con Fracciones.
Menú:
1- Sumar 
2- Restar
3- Multiplicar
4- Dividir
5- Salir
***************************************""")
opcion=int(input("Ingrese una opción: "))

if opcion >=1 and opcion<=5:
    if opcion == 1:
        sumar_fracciones(n1,d1,n2,d2)
    elif opcion ==2:
        restar_fracciones(n1,d1,n2,d2)
    elif opcion == 3:
        multiplicar_fracciones(n1,d1,n2,d2)
    elif opcion == 4:
        dividir_fracciones(n1,d1,n2,d2)
    else:
        print("Fin del programa")
else:
    print("ERROR - opción no válida")
