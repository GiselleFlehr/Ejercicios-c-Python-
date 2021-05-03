import random
lista=[]
pos=0
num=0
posicion=0

for i in range(0,20):
    lista.append(random.randint(1,100))

print("""Menú
*************************************
1- Añadir un número a la lista
2- Añadir un número en una posición
3- Longitud de la lista
4- Eliminar el último número
5- Eliminar un número de una posición
6- Contar números
7- Posición de un número
8- Mostrar número de la lista
9- Salir
*************************************""")

opcion=int(input("Ingrese una opción: "))
while opcion != 9:
    if opcion >= 1 and opcion <=9:
        if opcion == 1:
            lista.append(int(input("Ingrese número a agregar: ")))
    
        elif opcion == 2:
            num=int(input("Ingrese un número: "))
            pos=int(input("Ingrese posición: "))
            if pos >= len(lista):
                print("Posción incorrecta")
            else:
               lista.insert(pos-1,num)

        elif opcion == 3:
            print("Longitud: %d" %len(lista))

        elif opcion == 4:
            print("Se eliminó el número: %d" %lista.pop())

        elif opcion == 5:
            pos=int(input("Ingrese posición: "))
            lista.pop(pos-1)
            print(lista)

        elif opcion == 6:
            num=int(input("Ingrese un número: "))
            print("El número %d aparece %d veces en la lsita." %(num,lista.count(num)))

        elif opcion == 7:
            num=int(input("Ingrese un número: "))
            posicion=lista.index(num)
            print("El numero %d se encuentra en la posición %d" %(num,posicion))

        elif opcion == 8:
            print(lista)
    
        elif opcion == 9:
            print("Usted salió del sistema")
    else:
        print("ERROR - Opción incorrecta")
    opcion=int(input("Ingrese una opción: "))
