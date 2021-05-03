import math
cat_ady = float(input("Introduce el valor del cateto adyacente:"))
cat_op = float(input("Introduce el valor del cateto opuesto:"))
hipotenusa = math.sqrt((cat_ady ** 2) + (cat_op ** 2))
print("La hipotenusa es",round(hipotenusa,2))
