# Creando una lista con list

lista = list(["hola", "Emanuel", 55, "Octubre", False])
print(lista)

# LEN

resultado = len(lista)  # devuelve 5
print(resultado)

# APPEND

lista.append("JAJAJA")
print(lista)

# INSERT
# agrega un elemento en la lista en el indice especificado.

lista.insert(1, "Chau")  # agrega "Chau" en el indice 2
print(lista)

# EXTEND
# agrega varios elementos a la lista

lista.extend([False, 2023])
print(lista)

# POP
# eliminando un elemento de la lista por su indice

lista.pop(1)  # elimina chau (indice 1)
print(lista)

lista.pop(-1)  # elimina el ultimo elemento de la lista "2023" (pop en js)
print(lista)

# elimina el anteultimo elemento de la lista y asu sucesivamente.
lista.pop(-2)
print(lista)  # Se elimino "JAJA"

# REMOVE
# remueve un elemento de la lista por su valor

lista.remove(55)  # se removio 55
print(lista)

# SORT
# ordena la lista si no tiene cadena de textos, por eso primero eliminamos los
# elementos de texto de la lista y luego agregamos mas numeros.

lista.remove("hola")
lista.remove("Emanuel")
lista.remove("Octubre")
lista.extend([25, 2023, 1931, 0, 24])
print(lista)

# Ahora aplicamos el SORT

lista.sort()  # pone los False, primero luego True y luego nums de menor a mayor
print(lista)

# SORT reverse

lista.sort(reverse=True)
print(lista)  # devuelve la lista invertida

# REVERSE
# directamente invierte loe elementos de una lista no la ordena solo invierte.

lista.extend(["hola", "PEPE"])  # agrega estos elementos al ultimo
lista.reverse()  # la invertimos y ahora estaran primeros
print(lista)

# En una TUPLA solo podemos buscar elementos y contarlos. No podemos alterarlos.


# CLEAR
# eliminando todos los elementos de la lista.

lista.clear()  # devuelve una rray vacio
print(lista)
