lista = ["oso", "casa", "murciélago", "ventana", "programación"]

tamano = int(input("Ingrese el tamaño de la cadena que quiera ver: "))

contador_palabras = 0

for i in lista:
    if len(i) == tamano:
        print(i)
        contador_palabras += 1
    else:
        pass

if contador_palabras == 0:
    print(f"No habian palabras con {tamano} letras en la lista.")
else:
    pass