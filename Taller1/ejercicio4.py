tamano = int(input("Ingrese el tamaño que quiere que tenga la lista: "))

lista = [0 for i in range(tamano)]

for i in range(tamano):
    lista[i] = int(input(f"Ingrese un numero para la posicion {i} de la lista: "))

for i in lista:
    print(f"{i} - {i**2} - {i**3}")