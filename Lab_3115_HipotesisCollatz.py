
#Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
#Si es par, evalúa un nuevo c0 como c0 ÷ 2.
#De lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1.
#Si c0 ≠ 1, salta al punto 2.

c0=int(input("Ingresa un numero"))
pasos=0
bucle=True
if c0 <=0:
    print("El numero ingresado no debe ser menos o igual a 0")
else:
    
    while bucle==True:
        pasos+=1
        c0par=c0%2
        if c0par==0:
            c0=c0/2
            print(c0)
        else:
            c0=3*c0+1
            print(c0)
        if c0 ==1:
            bucle=False
                
print("Pasos =",pasos)