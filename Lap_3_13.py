
#Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

    #Si el número del año no es divisible entre cuatro, es un año común.
    #De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
    #De lo contrario, si el número del año no es divisible entre 400, es un año común.
    #De lo contrario, es un año bisies

año = int(input("Introduzca un año:"))

if año<1582:
    print("No dentro del periodo del calendario gregoriano")
else:
    if (año%4)!=0:
        print(año,"Es un año comun")
    elif(año%100)!=0:
        print(año,"Es un año bisiesto")
    elif(año%400)!=0:
        print(año,"Es una año comun")
    else:
        print(año,"Es un año bisiesto")