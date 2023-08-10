with open("archivos/texto_emanuel.txt", "w", encoding="UTF-8") as archivo:
    # Sobreescribiendo el archivo
    # archivo.write("jajajaja se sobreescribio todo el archivo")

    # Agregando dos lienas con writelines
    archivo.writelines(["Hola maestro me alegra verte bien\n", "Troglodita\n"])
    # agregando dos lineas mas
    archivo.writelines(["Agregando otra linea\n", "Pepetuelo\n"])
