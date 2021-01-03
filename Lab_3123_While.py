#Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

#Pedirá al usuario que ingrese un número entero.
#Utilizará un ciclo while.
#Comprobará si el número ingresado por el usuario es el mismo que el número 
#escogido por el mago. Si el número elegido por el usuario es diferente al 
#número secreto del mago, el usuario debería ver el mensaje 
#"¡Ja, ja! ¡Estás atrapado en mi ciclo!"  y se le solicitará que ingrese un número nuevamente. 
#Si el número ingresado por el usuario coincide con el número escogido por el 
#mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora".


print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numeroSecreto = 777
adivinar=False
while adivinar==False:
    numeroIngresado=int(input("Ingresa una numero:"))
    if numeroSecreto!=numeroIngresado:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    else:
        print("¡Bien hecho, muggle! Eres libre ahora")
        adivinar=True