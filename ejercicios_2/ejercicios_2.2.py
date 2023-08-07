# Creando una funcion que nos devuelva los numeros primos entre 0
#  y el numero que le pasamos.

# Creamos una funcion que verifique si un número es primo:

def es_primo(num):
    # verificamos que el nnumero pasado no pueda dividirse
    # por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num-1):
        # Si es divisible por alguno retornamos False y termina el bucle
        if num % i == 0:
            return False
        # Si termina el bucle significa que no fue divisible y es primo
    return True


# Creamos una funcion que retorna una lista con todos los primos.
def primos_hasta(num):
    # Creamos la lista
    primos = []
    for i in range(3, num+1):
        # Verificamos si el valor es primo
        resultado = es_primo(i)
        # En caso que lo sea lo agregamos a la lista
        if resultado == True:
            primos.append(i)
    return primos


# Creamos resultado llamando a la funcion y lo printiamos.
resultado = primos_hasta(80)
print(resultado)
