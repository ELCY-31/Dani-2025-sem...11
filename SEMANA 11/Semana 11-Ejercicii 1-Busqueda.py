# Funcion para realizar la busqueda en la Matriz
def buscar_en_matriz(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return fila, columna # Retorno la posicion (fila, columna)
    return None # Retorna None si el valor no fue encontrado

# Matriz bidimensional de ejemplo (3x3)
matriz = [
  [5, 3, 6,],
  [7, 2, 9,],
  [4, 1, 8,]
]

# Valor que queremos buscar en la matriz
valor_a_buscar = 6

# Llamada a la función de busqueda
resultado = buscar_en_matriz(matriz, valor_a_buscar)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontro en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontro en la matriz planteada.")
