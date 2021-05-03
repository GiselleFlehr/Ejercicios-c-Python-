np1 = float(input("Calificación 1° Parcial: "))
np2 = float(input("Calificación 2° Parcial: "))
np3 = float(input("Calificación 3° Parcial: "))
nota_parcial = ((np1+np2+np3)/3)*0.55
ef = float(input("Calificación Examen Final: "))
examen_final = ef*0.30
tp = float(input("Calificación Trabajo Final: "))
trabajo_final = tp*.15
nota_final = nota_parcial + examen_final + trabajo_final
print("Calificación final - Algoritmos: ",nota_final)
