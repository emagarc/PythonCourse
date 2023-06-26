animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [8, 5, 454, 5]

# Recorriendo la lista animales

for animal in animales:
    print(f"Ahora la variable es igual a: {animal}")

# Recorriendo la lista numeros y multiplicando cada valor por 10

for numero in numeros:
    resultado = numero * 10
    print(resultado)

# Iterando dos listas del mismo tamaño al mismo tiempo.

for numero, animal in zip(animales, numeros):
    print(f"recorriendo la lista Numeros, Ahora en el valor {numero}")
    print(f"recorriendo la lista Animales, Ahora en el animal {animal}")

# Iterando con range

for num in range(5, 15):
    print(num)

# Forma NO correcta de iterar una lista

for num in range(len(numeros)):
    print(numeros[num])

# Forma correcta de recorrer una lista con su indice:

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")

# Usando el for/else

for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termmino")
