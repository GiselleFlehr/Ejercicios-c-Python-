lista1 = []
lista2 = []
def listas(lista1):
    for i in range(1,6):
        lista1.append(input("Cadena de caracteres: "))
    lista2 = lista1[::-1]
    print(lista2)

print("Ingrese 5 cadenas de caracteres")
listas(lista1)
