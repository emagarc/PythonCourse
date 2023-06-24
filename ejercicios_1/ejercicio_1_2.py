# EJERCICIO 2

# Le pedimos al usuario que nos diga una frase (o varias)
frase = input("Decime una frase y te calculo cuanto tardarias en decrislo: ")

# Creamos una lista con todas las palabras del input (se separan por cada espacio)

palabras_separadas = frase.split(" ")

# Usamos len para contar la cantidad de palabras

cantidad_de_palabras = len(palabras_separadas)

# En caso que tarde mas de un minuto en decirlo, le decimos que pare un poco

if cantidad_de_palabras > 120:
    print("Para flaco, tampoco te pedi un testamento")

print(
    f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras /2} en decirlo")

print(
    f"Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos")
