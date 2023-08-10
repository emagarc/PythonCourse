# Leemos archivos TXT
archivo_sin_leer = open("archivos/texto_emanuel.txt", encoding="UTF-8")

# Leer archivo completo
archivo = archivo_sin_leer.read()
print(archivo)

# Cerramos el archivo después de leerlo
archivo_sin_leer.close()

# Abrir nuevamente el archivo para leer líneas
archivo_sin_leer = open("archivos/texto_emanuel.txt", encoding="UTF-8")

# Leer linea por linea, nos devuelve una lista de lineas
lineas = archivo_sin_leer.readlines()
print(lineas)

# Cerramos el archivo nuevamente después de leer líneas
archivo_sin_leer.close()

# Abrir nuevamente el archivo para leer una línea
archivo_sin_leer = open("archivos/texto_emanuel.txt", encoding="UTF-8")

# Leer una línea
linea = archivo_sin_leer.readline()
print(linea)

# Cerramos el archivo finalmente
archivo_sin_leer.close()
