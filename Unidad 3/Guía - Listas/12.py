def tabla_marco():
    marco = []
    print("Programa para crear un marco, de 5 x 15")
    for f in range (1,6):
        fila=[]
        for c in range (1,16):
            fila.append(int(input("Fila: %d, Columna: %d: " % (f,c))))
        marco.append(fila)

    #Imprimo tabla por pantalla
    print(marco[0])
    print(marco[1])
    print(marco[2])
    print(marco[3])
    print(marco[4])

tabla_marco()
