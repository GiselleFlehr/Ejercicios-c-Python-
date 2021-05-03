def tabla_enteros ():
    matriz = []
    print("Programa para crear una tabla de números enteros, de 5 x 5")
    #Creo la tabla con valores ingresados por teclado
    for f in range (0,5):
        fila=[]
        for c in range (0,5):
            fila.append(int(input("Elemento %d, %d: " % (f,c))))
        matriz.append(fila)

    #Sumo los valores de cada fila
    indice = 1
    for fila in matriz:
        print("Fila %d: %d" %(indice,sum(fila)))
        indice = indice + 1

    #Sumo los valores de cada columna
    columna1=0
    columna2=0
    columna3=0
    columna4=0
    columna5=0
    
    columna1 = matriz[0][0] + matriz[1][0] + matriz[2][0] + matriz[3][0] + matriz[4][0]
    print("Columna 1: ", columna1)
    columna2 = matriz[0][1] + matriz[1][1] + matriz[2][1] + matriz[3][1] + matriz[4][1]
    print("Columna 2: ", columna2)
    columna3 = matriz[0][2] + matriz[1][2] + matriz[2][2] + matriz[3][2] + matriz[4][2]
    print("Columna 3: ", columna3)
    columna4 = matriz[0][3] + matriz[1][3] + matriz[2][3] + matriz[3][3] + matriz[4][3]
    print("Columna 4: ", columna4)
    columna5 = matriz[0][4] + matriz[1][4] + matriz[2][4] + matriz[3][4] + matriz[4][4]
    print("Columna 5: ", columna5)

    #Imprimo matriz por pantalla
    print(matriz)
    
tabla_enteros()
