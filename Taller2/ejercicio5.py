from io import *

class Electrodomestico:
    marca = ""
    nombre = ""
    consumo = 0

    def clasify(self):
        if self.consumo < 500:
            return "bajo consumo"
        else:
            return "alto consumo"
        
    def save(self):
        file = open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\electrodomesticos.txt", "a")

        file.write(f"{self.marca} - {self.nombre} - {self.consumo} -> {self.clasify()}\n")

        file.close()

        
def main():
    tam = int(input("Ingerse la cantidad de electrodomesticos a guardar en el archivo: "))

    temp = Electrodomestico()
    for i in range(tam):
        print(f"\nelectrodomestico {i+1}")
        temp.marca = input(f"Ingrese la marca del electrodomestico {i+1}: ")
        temp.nombre = input(f"Ingrese el nombre del electrodomestico {i+1}: ")
        temp.consumo = int(input(f"Ingrese el consumo (en Watts) del electrodomestico {i+1}: "))

        temp.save()

main()