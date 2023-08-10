# abriendo el archivo con with open

with open("archivos/texto_emanuel.txt", encoding="UTF-8") as archivo:

    # leemos el arcchivo
    contenido = archivo.read()

    # mostramos el archivo:
    print(contenido)

# No es necesario cerrar el archivo al usar with open
