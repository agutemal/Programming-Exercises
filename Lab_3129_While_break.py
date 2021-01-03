
#La instrucción break se usa para salir/terminar un ciclo.

#Diseña un programa que use un ciclo while y le pida continuamente 
#al usuario que ingrese una palabra a menos que ingrese "chupacabra" 
#como la palabra de salida secreta, en cuyo caso el mensaje 
#"¡Has dejado el ciclo con éxito". Debe imprimirse en la pantalla y el ciclo debe terminar.

print("Programa prueba de la funcion break")

condicion=1
palabraCondicion=""
while condicion==1:
    palabraCondicion=input("Ingresa una palabra, si es correcta saldras del bucle:")
    if palabraCondicion=="chupacabra":
        break
print("¡Has dejado el ciclo con éxito")