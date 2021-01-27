# paso 1
beatles=[]
print("Paso 1:", beatles)

# paso 2

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)
# paso 3

for i in range(2):
    if i==0:
        beatles.append(input("Inprese el nombre de Stu Sutcliffe: "))
    else:
        beatles.append(input("Ingrese el nombre de Pete Best: "))
print("Paso 3:", beatles)        
# etapa 4

beatles.remove("Stu Sutcliffe")
beatles.remove("Pete Best")
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)



# probando la longitud de la lista
print("Los Fab", len(beatles))
