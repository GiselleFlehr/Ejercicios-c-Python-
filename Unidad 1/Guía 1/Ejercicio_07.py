num = int(input("Ingrese la cantidad de minutos a convertir: ")) 
minutes = num % 60
print ("Minutos: ", minutes)
hours = (num - minutes)/60
print ("Horas: ",hours)
result = str(hours) + "horas" + ":" + str(minutes) + "min."
print (result)

