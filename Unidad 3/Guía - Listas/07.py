lista1 = []
lista2 = []
lista3 = []

def listas (lista1, lista2):
    #creo la 1° lista
    print("Ingrese valores enteros para la primera lista")
    for i in range(1,6):
        lista1.append(int(input("Ingrese un número: ")))
    #creo la 2° lista
    print("Ingrese valores enteros para la segunda lista")
    for i in range(1,6):
        lista2.append(int(input("Ingrese un número: ")))
    #sumo ambas listas
    for i in range(0,5):
        lista3.append(lista1[i]+lista2[i])
    print("La suma de ambas listas es: ",lista3)

listas (lista1, lista2)
