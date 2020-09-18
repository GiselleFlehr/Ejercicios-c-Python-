#Ejercicio 9

var1 = 0
var2 = 0
var3 = ""
var4 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for n in range(4):
	a=int(input("Grados: "))
	var1 = int(a/10) + var1
	var2 = (var4[var1])
	var3 = var3 + str(var2)
print(var3)	
