print("===Calculadora de indice de masa corporal===")
print("Ingresa tu altura en metros")
altura=float(input())
print("Ingresa tu peso en Kg")
peso=float(input())
IMC=peso/altura**2

print("================================")
print("Peso inferior al normal Menos de 18.5")
print("Normal 18.5 – 24.9")
print("Peso superior al normal 25.0 – 29.9")
print("Obesidad Más de 30.0")
print("================================")

print("Su IMC es: ",round(IMC,2))
