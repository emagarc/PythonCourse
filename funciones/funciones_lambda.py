
# Creando una funcion labda para multiplicar por dos
# Al parecer ahora no te deja guardr la funcion asi
# multiplicar_por_dos = lambda x : x*2

# El corrector de python corrige la sintaxis a como muestro a continuacion:

def multiplicar_por_dos(x): return x*2


print(multiplicar_por_dos(5))


numeros = [1, 2, 3, 4, 54, 8, 5, 544, 15, 2]

# Creando una funcion que diga si es par o no:


def es_par(num):
    if (num % 2 == 0):
        return True


# Usando filter con una funcion comun

numeros_pares = filter(es_par, numeros)
print(numeros_pares)
# Nos devuelve un Filter Object <filter object at 0x1028bdab0>

print(list(numeros_pares))  # Devuelve una lista filtrada [2, 4, 54, 8, 544, 2]

# Haciendo lo mismo con labda veremos si nos deja el corrector:

numeros_pares_lambda = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numeros_pares_lambda))
# Si nos deja y nos devuelve la misma lista filtrada
