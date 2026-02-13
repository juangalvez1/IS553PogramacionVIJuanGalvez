Lista= [2, 8, "hola", "programación", 10, "utp", 85, 82, 100,"mundo"]

suma = 0

for i in Lista:
    if isinstance(i, int):
        suma += i
    else:
        pass

print(f"La suma de los valores numericos de la Lista es: {suma}")