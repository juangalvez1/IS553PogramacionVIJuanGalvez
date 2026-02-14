lista = ["oso", "casa", "murciélago", "ventana", "programación","objetos", "listas", "métodos", "utp"]

char = input("Ingrese eun caracter, para buscarlo en las palabras de la lista: ")

contador_palabra = 0

for i in lista:
    if i.find(char) != -1:
        print(f"{i} - la palabra es {'par' if len(i) % 2 == 0 else 'impar'}")
        contador_palabra += 1
    else:
        pass

if contador_palabra == 0:
    print(f"No habian palabras con la letra {char} en ellas")
else:
    pass