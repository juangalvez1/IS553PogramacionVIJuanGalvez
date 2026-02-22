from io import *
import string

class Frase:
    texto = ""
    autor = ""

    def count_word(self, word, list, tam):
        counter = 0
        for i in range(tam):
            counter += list[i].texto.lower().split().count(word.lower())

        print(f"La palabra '{word}' esta {counter} veces en la lista de frases.")
        return counter
                
def main():
    tam = int(input("Ingrese el tamaño para la lista de frases: "))

    list = [Frase() for i in range(tam)]

    for i in range(tam):
        list[i].texto = input(f"Ingrese la frase {i+1} de la lista: ")

    word = input("Ingrese la palabra que quiere buscar en las frases de la lista: ")

    temp = Frase()
    temp.count_word(word, list, tam)

    file = open(r"archivos/frase.txt", "a")

    for i in range(tam):
        file.write(list[i].texto)
        if i != tam - 1:
            file.write(" - ")
    file.write("\n")

    file.close()

main()