def tabla_diagonal():
    diagonal = []
    print("Programa para crear una tabla de números enteros, de 5 x 5")
    #Creo la tabla con valores ingresados por teclado
    for f in range (0,5):
        fila=[]
        for c in range (0,5):
            fila.append(int(input("Elemento %d, %d: " % (f,c))))
        diagonal.append(fila)

    #Imprimo tabla por pantalla
    print(diagonal[0])
    print(diagonal[1])
    print(diagonal[2])
    print(diagonal[3])
    print(diagonal[4])

tabla_diagonal()
