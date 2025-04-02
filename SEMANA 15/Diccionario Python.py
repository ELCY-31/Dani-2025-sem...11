# Crear un diccionario llamado informacion_personal

INFORMACION_PERSONAL = {
    "Nombre": "Elody Escobar",
    "EDAD": "18",
    "CIUDAD": "Orellana",
    "PROFESIÓN": "Desarrollador de software"
}

# Acceder y Modificar Valores
# Accede al valor asociado con la clave "ciudad" y modifícalo
INFORMACION_PERSONAL["CIUDAD"] = "Joya de los Sachas"

# Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona
# (En este caso, modificamos la profesión existente)
INFORMACION_PERSONAL["PROFESIÓN"] = "Ingeniera de sistemas"

# Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala
if "TELEFONO" not in INFORMACION_PERSONAL:
    INFORMACION_PERSONAL["TELEFONO"] = "098700032"

# Elimina la clave "edad" del diccionario
del INFORMACION_PERSONAL["EDAD"]

# Imprimir el diccionario final
print(INFORMACION_PERSONAL)
