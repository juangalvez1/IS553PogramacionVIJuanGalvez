lista = ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp", "pereira"]
vocales = "aeiouáéíóú"

contador_consonantes = 0

for palabra in lista:
    for letra in palabra:
        if vocales.find(letra) == -1:
            contador_consonantes += 1
        else:
            pass

print(f"En las cadenas de la lista del programa hay {contador_consonantes} letras que NO son vocales.")