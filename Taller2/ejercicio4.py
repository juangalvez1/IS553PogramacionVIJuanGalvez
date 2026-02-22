from io import *

class Cliente:
    id = 0
    nombre = ""
    edad = 0
    ciudad = ""
    saldo = 0

    def save_client(self):
        file = open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\clientes.txt", "a")

        file.write(f"{self.id},{self.nombre},{self.edad},{self.ciudad},{self.saldo}\n")

        file.close()

    def show_neg_balance(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\clientes.txt", "r") as file:
            clientes = []
            
            for line in file:
                if line.strip() == "":
                    continue

                data = line.strip().split(",")

                temp = Cliente()
                temp.saldo = int(data[4])

                if temp.saldo < 0:
                    temp.id = int(data[0])
                    temp.nombre = data[1]
                    temp.edad = int(data[2])
                    temp.ciudad = data[3]
                    clientes.append(temp)
                else:
                    pass

            print("Clientes con saldo negativo\n")
            for i in range(len(clientes)):
                print(f"cliente {i+1}: {clientes[i].id} - {clientes[i].nombre} - {clientes[i].edad} - {clientes[i].ciudad} - {clientes[i].saldo}")



def main():
    tam = int(input("Ingerse la cantidad de clientes a guardar en el archivo: "))

    temp = Cliente()
    for i in range(tam):
        print(f"\ncliente {i+1}")
        temp.id = int(input(f"Ingrese la id del cliente {i+1}: "))
        temp.nombre = input(f"Ingrese el nombre del cliente {i+1}: ")
        temp.edad = int(input(f"Ingrese la edad del cliente {i+1}: "))
        temp.ciudad = input(f"Ingrese la ciudad del cliente {i+1}: ")
        temp.saldo = int(input(f"Ingrese el saldo del cliente {i+1}: "))

        temp.save_client()
    
    temp.show_neg_balance()

main()