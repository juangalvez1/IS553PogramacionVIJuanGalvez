tamano = int(input("Ingrese la cantidad de cadenas que quiere que tenga la lista: "))

lista = ["" for i in range(tamano)]

min = ""
max = ""

for i in range(tamano):
    lista[i] = input("Ingrese una cadena para la lista: ")
    if i == 0:
        min = max = lista[i]
    elif len(lista[i]) > len(max):
        max = lista[i]
    elif len(lista[i]) < len(min):
        min = lista[i]

print(f"Cadena mayor = {max} \nCadena menor = {min}")

