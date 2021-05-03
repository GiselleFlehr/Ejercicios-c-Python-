
lista1=[]
lista2=[]
num=0

print("Ingrese números para crear una lista. Termina ingresando un número negativo")
num=int(input("Número: "))
while num>= 0:
    lista1.append(num)
    num=int(input("Ingrese un número: "))
print("Lista ingresada: ",lista1)
for num in lista1:
    if num not in lista2:
        lista2.append(num)

print("Nueva lista: ",lista2)

