equipo=[]
goles=[]
resultados=[]
partidos=[]

for i in range(1,6):
        print("Partido %d" %i)
        print("**************")
        for x in range(1,3):
                equipo=input("Equipo %d: " %x)
                partidos.append(equipo)
                
                goles=input("Goles: ")  
                resultados.append(goles)

for t in zip(partidos,resultados):
        print(t[0],t[1])
        
