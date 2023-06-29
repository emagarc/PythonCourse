# Forma no optima de sumar valores

def suma(a, b):
    return a+b


resultado = suma(5, 3)
print(resultado)

# Sumando recorriendo la lista con un bucle
# No es la manera mas optima de hacer la suma


def suma_lista(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados


lista_sumada = suma_lista([5, 3, 8, 11, 269, 2])
print(lista_sumada)


# forma optima de sumar valores


def suma_total(numeros):
    return sum([*numeros])


resultado2 = suma_total([5, 3, 6, 9, 8, 5, 5, 23, 7])
print(resultado2)

# Lo mismo que arriba pero utilizamos el parametro args.


def suma_args(nombre, *numeros):
    return f"{nombre}, esta es la suma de tus numeros: {sum(numeros)}"


resultado = suma_args("Emanuel", 5, 3, 8, 11, 269, 2)
print(resultado)
