from io import *
import string

class Numero:
    num = ""

    def sum_digits(self):
        sum = int(self.num[0]) + int(self.num[1]) + int(self.num[2])
        return sum

    def register_num(self, file):
        file.write(f"numero: {self.num} inverso: {self.num[::-1]}\n")

def main():
    num = Numero()
    num.num = input("Ingrese un numero positivo de 3 cifras: ")

    if int(num.num) > 1000 or int(num.num) < 0:
        print("Número ingresado no valido. Intente de nuevo.")
    else:
        pass

    print(f"\nsuma: {num.sum_digits()}\n")
    
    file = open(r"archivos/numeros.txt", "a+")
    num.register_num(file)
    file.close()

    file = open(r"archivos/numeros.txt", "r")
    read = file.read()
    print(f"ARCHIVO:\n{read}")
    file.close()


main()