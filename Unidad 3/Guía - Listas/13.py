def kms_conductores():
    nombre=[]
    kms=[]
    total_kms=[]
    num_c = int(input("Ingrese cantidad de conductores: "))
    
    for c in range(0,num_c):
        nombre.append(input("Nombre conductor: "))
        kmxdia=[]
        print("Ingrese kms recorridos durante 5 días")
        for d in range(1,6):
            kmxdia.append(int(input("Kms realizados el día %d: " %d)))
        kms.append(kmxdia)

    for k in kms:
        total_kms.append(sum(k))

    for nombre,k in zip(nombre,total_kms):
        print(nombre,"ha realizado: %d kms" %k)

    
kms_conductores()
