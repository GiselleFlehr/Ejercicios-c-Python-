pila = str
lista = []
cadena = bool

pila = (input("Ingrese una cadena de caracteres: "))

def longitud_pila(pila):
    pila.split()
    print("La cadena posee: ", len(pila), "elementos")

def pila_vacia(pila):
    if len(pila) == 0:
        print("Pila vacía")
        cadena = True

def pila_llena(pila):
    if len(pila) != 0:
        print("Pila llena")
        cadena = True

def add_pila(pila):
    lista = input("Ingrese una pila: ")
    pila_vacia(pila)
    if cadena == True:
        pila.append(lista)
    else:
        print("ERROR - Lista llena")

def sacar_pila(pila):
    pila.split()
    print("Primer elemento: ",pila[0])

def escribir_pila(pila):
    for i in pila:
        print(i)

print("""Menú:
1- Añadir elemento a la pila.
2- Sacar 1° elemento a la pila.
3- Longitud de la pila.
4- Mostrar pila:
5- Salir""")

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    add_pila(pila)
elif opcion == 2:
    sacar_pila(pila)
elif opcion == 3:
    longitud_pila(pila)
elif opcion == 4:
    escribir_pila(pila)
else:
    print("Usted salió del sistema")
