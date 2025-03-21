# CALCULAR EL DESCUENTO DE 2 COMPRAS
def calcular_descuento(valor, porcentaje=10):
    return valor * (porcentaje / 100)

# Primera compra con el descuento por defecto del (10%)
valor_total_1 = 250.68  # Asignar valor a la compra
descuento_1 = calcular_descuento(valor_total_1)  # Llamar a la función calcular_descuento
valor_final_1 = valor_total_1 - descuento_1  # Calcular el monto final a pagar

# Segunda compra con un porcentaje de descuento personalizado
valor_total_2 = 832.78  # Asignar un valor a la compra
valor_desc_2 = 10  # Asignar el porcentaje de descuento
descuento_2 = calcular_descuento(valor_total_2, valor_desc_2)  # Llamar a la función con porcentaje personalizado
valor_final_2 = valor_total_2 - descuento_2  # Calcular el valor final a pagar

# Mostrar los resultados con 3 decimales y el descuento
print()
print(f"COMPRA 1")
print(f"Valor total: {valor_total_1:.3f}, ")
print(f"El porcentaje de descuento es del 10%, ")
print(f"Valor del descuento: {descuento_1:.3f}, ")
print(f"Valor final a pagar: {valor_final_1:.3f}")

print()
print(f"COMPRA 2")
print(f"Valor total: {valor_total_2:.3f}, ")
print(f"El porcentaje de descuento es del {valor_desc_2}%, ")
print(f"Valor del descuento: {descuento_2:.3f}, ")
print(f"Valor final a pagar: {valor_final_2:.3f}")
