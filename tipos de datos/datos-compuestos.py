# Listas

lista = ["Emanuel Garcia", True, 1.76]
print(lista[0])

# Tuplas
# las tuplas, a diferencia de las listas no pueden modificarse

tupla = ("Emanuel Garcia", True, 1.76)

# Conjunto (set)
# los conjuntos podemos redefinirlos pero no podemos modificar sus elementos internos.
# no podemos acceder por indice a los elementos de un conjunto como si con las tuplas o listas.
# un conjunto (set) no muestra sus elementos repetidos. No puede tener duplicados.
# son datos desordenados sin indice

conjunto = {"Emanuel Garcia", True, 1.76, True}

# Diccionario
# simil JSON

diccionario = {
    "nombre": "Emanuel Garcia",
    "Le gusta programar ?": True,
    "Altura": 1.76,
    "Dato duplicado": True,
}

print(diccionario["Altura"])
