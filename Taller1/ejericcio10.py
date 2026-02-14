lista = ["casa", "programación", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]
lista_temp = []

# punto a del ejercicio

for i in range(len(lista)):
    if lista[i] not in lista_temp:
        lista_temp.append(lista[i])
    else:
        pass

# lista = lista_temp
print(f"\nPunto A:\nLista original:\t\t\t{lista} \nLista sin palabas repetidas:\t{lista_temp}")


input("\npresione enter para continuar con el siguiente punto del ejercicio: ")

# punto b del ejercicio
lista_temp.clear()
vocales = "aeiouáéíóú"

for palabra in lista:
    contador_vocales = 0
    
    for letra in palabra:
        if letra in vocales:
            contador_vocales += 1
        else:
            pass
    
    if contador_vocales != 0:
        lista_temp.append(palabra)

print(f"\nPunto B:\nLista original:\t\t\t{lista} \nLista sin palabras sin vocales:\t{lista_temp}")


input("\npresione enter para continuar con el siguiente punto del ejercicio: ")

# punto c del ejercicio
lista_temp = lista.copy()
lista_temp.sort()

print(f"\nPunto C:\nLista original:\t\t\t{lista} \nLista ordenada alfabeticamente:\t{lista_temp}")