import string

palabras = ["Hola", "mundo", "esto", "es", "Python"]

frase = ""

for i in palabras:
    frase = frase + " " + i

frase = frase.lstrip()

print("La suma de las palabras queda como:")
print(frase)