#Ejercicio 2

pi=3.14
radio=0
vueltas=0
longitud=0
distancia_cm=0
distancia=0

print("Calcular distancia recorrida por una rueda.")

def recorrido(radio,vueltas):
	print("Ingrese valor de radio (en cm) y cantidad de vueltas, separado por un espacio.")
	radio,vueltas=input("Ingrese radio y vueltas: ").split()
	print("Radio: ",radio,". Vueltas: ",vueltas)
	longitud=2*int(radio)*pi
	distancia_cm=longitud*int(vueltas)
	distancia=distancia_cm*0.01
	print("La rueda recorre: ",distancia," mts.")	

recorrido(radio,vueltas)
