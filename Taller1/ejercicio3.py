n_materias = int(input("Ingrese el numero de materias: "))

materias = [0 for i in range(n_materias)]
promedio = [[0 for i in range(5)] for i in range(n_materias)]

for i in range(n_materias):
    print()
    materias[i] = input(f"ingrese el nombre de la {i + 1} materia: ")

    promedio[i][0] = float(input(f"ingrese la nota 1 de {materias[i]}: "))
    promedio[i][1] = float(input(f"ingrese la nota 2 de {materias[i]}: "))
    promedio[i][2] = float(input(f"ingrese la nota 3 de {materias[i]}: "))
    promedio[i][3] = float(input(f"ingrese la nota 4 de {materias[i]}: "))

    promedio[i][4] = (promedio[i][0] + promedio[i][1] + promedio[i][2] + promedio[i][3]) / 4

print()

for i in range(n_materias):
    print()
    
    print(f"{materias[i]} - nota1: {promedio[i][0]}, nota2: {promedio[i][1]}, nota3: {promedio[i][2]}, nota4: {promedio[i][3]}")
    print(f"Promedio de {materias[i]}: {promedio[i][4]} - asignatura {'aprobada' if promedio[i][4] >= 3 else 'perdida'}")

promedio_total = 0.0

for i in range(n_materias):
    promedio_total += promedio[i][4]

promedio_total /= n_materias

print(f"\nPromedio general: {promedio_total} - {'Semestre perdido' if promedio_total < 3 else 'buen trabajo' if promedio_total < 4  else 'felicidades seras becado'}")