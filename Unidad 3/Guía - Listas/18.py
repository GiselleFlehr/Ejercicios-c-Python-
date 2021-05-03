lista=[]
print("Crea una lista de palabras. Finaliza la carga con 0")
cadena=input("Cadena: ")
while cadena != "0":
    lista.append(cadena)
    cadena = input("Cadena: ")

print("""Menú:
1. Contar
2. Modificar
3. Eliminar
4. Mostrar
5. Salir
**************""")

opcion = int(input("Introduce una opción: "))
if opcion == 5:
    print("Usted salió del sistema")

while opcion != 5:
    if opcion >= 1 and opcion <=5:
        if opcion == 1:
            cadena=input("Cadena: ")
            print("La cadena aparece %d veces" %lista.count(cadena))
    
        elif opcion == 2:
            cadena=input("Cadena a modificar: ")
            cadena2=input("Cadena nueva: ")
            i=0
            for x in lista:
                if x == cadena:
                    lista[1]=cadena2
                i=i+1
            
        elif opcion == 3:
            cadena=input("Cadena a eliminar: ")
            for y in lista:
                if cadena in lista:
                    lista.remove(cadena)

        elif opcion == 4:
            print(lista)

    else:
        print("ERROR - Opción incorrecta")
    opcion=int(input("Ingrese una opción: "))
