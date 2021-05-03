sueldo = int(input("Ingrese su sueldo de base: $"))
venta1 = int(input("Ingrese valor 1° venta: $"))
com1 = venta1 * 0.10
venta2 = int(input("Ingrese valor 2° venta: $"))
com2 = venta2 * 0.10
venta3 = int(input("Ingrese valor 3° venta: $"))
com3 = venta3 * 0.10
sueldo_total = sueldo + com1 + com2 + com3
print ("Sueldo total a cobrar: $",sueldo_total)
