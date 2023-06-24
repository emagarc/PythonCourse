# Creando un copnjunto con set()

conjunto = set(["dato 1", "dato 2"])
print(conjunto)

# Metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)

# Teoria de conjuntos

conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Verificamos que sea un subconjunto
resultado = conjunto2.issubset(conjunto1)
print(resultado)  # True
resultado = conjunto2 <= conjunto1  # True
print(resultado)

# Verificamos que sea un superconjunto
resultado = conjunto2.issuperset(conjunto1)
print(resultado)  # False
resultado = conjunto2 >= conjunto1  # False
print(resultado)

# Verificamos si hay algun numero en comun (si hay algun numero en comun da False)
resultado = conjunto2.isdisjoint(conjunto1)  # False
