palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord

userWord=input("Ingrece una palabra:")
userWord = userWord.upper()

for letra in userWord:
    if letra=="A":
        continue
    elif letra=="E":
        continue
    elif letra=="I":
        continue
    elif letra=="o":
        continue
    elif letra=="u":
        continue
    palabraSinVocal=palabraSinVocal+letra

print(palabraSinVocal)