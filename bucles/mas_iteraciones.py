# Creando las listas

frutas = ["banana", "manzana", "pera", "pomelo", "tomate", "anana", "durazno"]
cadena = "Hola Ema"
numeros = [2, 5, 9, 11, 10]

for fruta in frutas:
    print(f"Me voy a comer una {fruta}")

# Evitando que coma el elemento tomate con "continue"

for fruta in frutas:
    if fruta == "tomate":
        continue
    print(f"Me voy a comer una {fruta}")

# Interrumpir el bucle con "break", en caso de encontrar un break el else tampoco se ejecuta

for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "tomate":
        break
else:
    print("terminado")


# Recorrer una cadena de texto:

for letra in cadena:
    print(letra)

# for en una sola linea de codigo:

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
