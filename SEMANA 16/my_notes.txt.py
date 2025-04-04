# Abrir el archivo para la escritura
Archivo = open('my_notes.txt', 'w')
# Escribir 3 líneas de notas personales
Archivo.write('Los exámenes de la universidad comienzan la siguiente semana.\n')
Archivo.write('Mañana sábado tengo clases desde las 7:30AM hasta las 14:45PM.\n')
Archivo.write('Hoy tengo que entrar a la tutoría de programación.\n')
# Cerrar el archivo después de escribir
Archivo.close()

# Abrir el archivo para la lectura
Archivo = open('my_notes.txt', 'r')
# Indicar que se debe lee línea a línea y eliminar los saltos de las líneas extras
print(Archivo.readline().strip())
print(Archivo.readline().strip())
print(Archivo.readline().strip())
# Cerrar el archivo
Archivo.close()
