import random

lista = [random.randint(0, 100) for i in range(15)]

for i in lista:
    print(f"{i} - {i**2} - {i**3}")