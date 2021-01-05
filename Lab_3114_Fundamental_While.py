#Escenario
#Escucha esta historia: Un niño y su padre, un programador 
#de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

#Su pirámide es un poco rara, ya que en realidad 
#es una pared en forma de pirámide, es plana. La 
#pirámide se apila de acuerdo con un principio simple: 
#cada capa inferior contiene un bloque más que la capa superior.

bloques = int(input("Ingrese el número de bloques:"))
altura=0
total_bloques=1
capa_superior=1
while total_bloques<=bloques:
    capa_superior+=1
    total_bloques=total_bloques+capa_superior
    altura+=1


print("La altura de la pirámide:", altura)