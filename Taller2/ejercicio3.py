from io import *
from random import randint
import string

class Cadena:
    texto = str()

    def sort_by_vowel(self, lista):
        tempVowels = []
        tempNotvowels = []

        vowels = "aeiou"

        for cadena in lista:
            if cadena.texto[0] in vowels:
                tempVowels.append(cadena)
            else:
                tempNotvowels.append(cadena)

        lista.clear()
        lista = tempVowels + tempNotvowels

        return lista


def main():
    lista = [Cadena() for i in range(15)]

    letters = "abcdefghijklmnopqrstuvwxyz"

    for i in range(15):
        tam = randint(2, 20) # Tamaño de la cadena i en 'lista'
        lista[i].texto = "".join(letters[randint(0, 25)] for i in range(tam))

    temp = Cadena()
    lista = temp.sort_by_vowel(lista)

    for cadena in lista:
        print(cadena.texto)

    file = open(r"archivos/cadenas.txt", "a")

    file.write("[")
    for i in range(15):
        file.write(lista[i].texto)
        if(i != 14):
            file.write(", ")
    file.write("]\n")

main()