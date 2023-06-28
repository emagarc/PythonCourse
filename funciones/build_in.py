# Las siguientes son funciones integradas o llamadas build in

numeros = [4, 18, 45, 11, 111, 34]

# Encontrando el numero mayor de una lista
# Tambien funciona en tuplas y conjuntos.

numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrando el numero menor de una lista
# Tambien funciona en tuplas y conjuntos.

numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondeando a 6 decimales.

numero = 12.5698634565
redondeado = round(numero, 2)
print(redondeado)

# Retorna False si le pasamos => 0, elementos vacios, False, NoNe o ninguno
# Devuelve True a la inversa

numero = 1
booleano = bool(numero)
print(booleano)

# Retorna True si todos los datos de un iterable son verdaderos.

resultado_all = all([1, 2, 86, None, False, True])  # aca retorna False
print(resultado_all)

# Suma todos los elementos de un iterable

resultado_suma = sum(numeros)
print(resultado_suma)
