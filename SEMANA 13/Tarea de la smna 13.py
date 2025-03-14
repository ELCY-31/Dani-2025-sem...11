# Almacenar todas las temperaturas por ciudad, semana y día, en una matriz 3D
# Nombres de las ciudades
ciudades = ["Quito", "Loja", "Guayaquil"]
num_semanas = 4

temperaturas = [
    # Ciudad: Quito
    [
        [18, 20, 22, 24, 25, 26, 27],
        [19, 21, 23, 25, 26, 27, 28],
        [17, 19, 21, 23, 24, 25, 26],
        [20, 22, 24, 26, 27, 28, 29]
    ],
    # Ciudad: Loja
    [
        [15, 16, 18, 19, 20, 21, 22],
        [14, 16, 17, 19, 20, 21, 23],
        [13, 15, 16, 18, 19, 20, 22],
        [16, 18, 19, 21, 22, 23, 24]
    ],
    # Ciudad: Guayaquil
    [
        [28, 29, 30, 31, 32, 33, 34],
        [27, 28, 29, 30, 31, 32, 33],
        [29, 30, 31, 32, 33, 34, 35],
        [30, 31, 32, 33, 34, 35, 36]
    ]
]

# Calcular el promedio de las temperaturas por cada ciudad
def calcular_promedio_total(matriz, ciudades):
    for ciudad in range(len(matriz)):  # Iterar sobre cada ciudad
        total_temperaturas = 0  # Acumular todas las temperaturas de la ciudad
        total_datos = 0  # Contar el total de datos registrados

        for semana in range(len(matriz[ciudad])):  # Iterar sobre cada semana
            total_temperaturas += sum(matriz[ciudad][semana])  # Sumar las temperaturas
            total_datos += len(matriz[ciudad][semana])  # Contar los datos

        promedio_total = total_temperaturas / total_datos  # Calcular el promedio total
        print(f"Promedio total de temperatura en {ciudades[ciudad]}: {promedio_total:.2f}°C")

# Calcular el promedio de temperatura por semana en cada ciudad
def calcular_promedio_semanal(matriz, ciudades):
    for ciudad in range(len(matriz)):
        print(f"\nPromedios semanales de temperatura en {ciudades[ciudad]}:")
        for semana in range(len(matriz[ciudad])):
            promedio_semanal = sum(matriz[ciudad][semana]) / len(matriz[ciudad][semana])
            print(f"  Semana {semana + 1}: {promedio_semanal:.2f}°C")

# Calcular y mostrar los promedios
calcular_promedio_total(temperaturas, ciudades)
calcular_promedio_semanal(temperaturas, ciudades)

