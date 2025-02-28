# Función de ordenación Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Corregido arr[j+1] en lugar de arr[1]

# Función para ordenar todas las filas de la matriz
def ordenar_matriz(matriz):
    for fila in matriz:
        bubble_sort(fila)

# Matriz bidimensional de ejemplo (3x3)
matriz = [
   [8, 3, 9],
   [2, 7, 1],
   [4, 6, 2]
]

# Mostrar la matriz original
print("MATRIZ ORIGINAL:")
for fila in matriz:
    print(fila)

# Ordenar todas las filas de la matriz
ordenar_matriz(matriz)

# Mostrar la matriz organizada
print("MATRIZ ORGANIZADA:")
for fila in matriz:
    print(fila)
