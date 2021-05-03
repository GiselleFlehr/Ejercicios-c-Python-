def temp_min_max():
    print("Ingreso de temp min y max de 5 días")
    temperaturas=[]
    for i in range(1,6):
        temp = []
        temp.append(int(input("Día %d. Mínima: " % i)))
        temp.append(int(input("Día %d. Máxima: " % i)))
        temperaturas.append(temp)

    print("Temperaturas medias.")
    tempmedia=[]
    media=0
    indice = 1
    for temp in temperaturas:
        media = sum(temp)/len(temp)
        tempmedia.append(media)
        print("Día %d.: %f" %(indice,media))
        indice += 1

    print("Menor temperatura.")
    tempmedia.sort()
    print("Media de: %d" %tempmedia[0])

temp_min_max()
