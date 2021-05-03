precio=[]
cant=[]
articulo=5
sucursales=4
cantidad=[]
total_art=0
total_suc=[]

#Precios
for a in range(0,articulo):
    precio.append(float(input("Precio Articulo %d: " %(a+1))))

#Cantidad articulos
for s in range(0,sucursales):
    cant_art=[]
    for a in range(0,articulo):
        cant_art.append(int(input("Cantidad de art. %d para la sucursal %d: " %((a+1),(s+1)))))
    cantidad.append(cant_art)

#Cantidad total de artículos
total_art=(sum(cantidad[0]))+(sum(cantidad[1]))+(sum(cantidad[2]))+(sum(cantidad[3]))

#Cantidad articulos sucursal 2
print("Total artículos sucursal 2: %d" %sum(cantidad[1]))

#Cantidad de articulo 3 en la sucursal 1
print("Cantidad artículo 3 en sucursal 1: %d" %cantidad[0][2])

#Recaudación de cada sucursal
for s in cantidad:
    total=0
    for p,cantidad in zip(precio,s):
        total=total+(p*cantidad)
    total_suc.append(total)
print("Recaudación sucursal 1: $ %d" %total_suc[0])
print("Recaudación sucursal 2: $ %d" %total_suc[1])
print("Recaudación sucursal 3: $ %d" %total_suc[2])
print("Recaudación sucursal 4: $ %d" %total_suc[3])
                                                                                   
#Recaudación total empresa
recaudacion_t=0
recaudacion_t=total_suc[0]+total_suc[1]+total_suc[2]+total_suc[3]
print("Recaudación total empresa: $ %d" %recaudacion_t)
