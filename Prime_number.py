print("====Este programa determina si un numero es primo o no=====")
print("Ingrese un numero")
pn=True;
numero=int(input())
for i in range(2, numero):
    resultado=numero%i
    if resultado==0:
        pn=False
if pn==True:        
    print("El numero: ",numero,"es primo")
else:
    print("El numero: ", numero,"no es primo")
print("Muchas Gracias")
