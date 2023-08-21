import re

texto = '''Hola Maestro esta es la cadena 145. como estas mi capitan
Esta es la segunda linea de texto.
Y esta es la final definitiva mi capitan
'''

# No devuelve un objetio con la coincidencia <re.Match object; span=(0, 4), match='Hola'>
resultado = re.search("Hola", texto)
print(resultado)

# Nos devuelve una rray con todas las coincidencias.
resultado = re.findall("Esta", texto, flags=re.IGNORECASE)
print(resultado)

# Ahora si arrancamos con expresiones regulares:

# \d -- busca digitos numericos del 0 al 9
resultado = re.findall(r"\d", texto)
print(resultado)

# \D -- con D mayuscula busca todo menos digitos numericos.
resultado = re.findall(r"\D", texto)
print(resultado)

# \w -- busca caracteres alfanumericos [a-z A-Z 0-9 _ ] incluye guion bajo.
resultado = re.findall(r"\w", texto)
print(resultado)

# \W -- busca todo menos [a-z A-Z 0-9 _ ] incluyendo guion bajo.
resultado = re.findall(r"\W", texto)
print(resultado)

# \s -- busca espacios en blanco --> espacios, tabs, saltos de linea.
resultado = re.findall(r"\s", texto)
print(resultado)

# \S -- busca TODO menos espacios en blanco --> espacios, tabs, saltos de linea.
resultado = re.findall(r"\S", texto)
print(resultado)

# . -> Busca TODO MENOS saltos en linea.
resultado = re.findall(r".", texto)
print(resultado)

# \n -> Busca saltos en linea.
resultado = re.findall(r"\n", texto)
print(resultado)

# \n -> Busca todos los puntos (.)
resultado = re.findall(r"\.", texto)
print(resultado)

# Armando una cadena que busque un nunmero, seguido de un punto y un espacio.
resultado = re.findall(f"\d\.\s", texto)
print(resultado)

# Buscando el comienzo de una linea ^. ( va a verificar si el comienzo de una linea con Hola existe)
# flags=re.M activa la multilinea.
resultado = re.findall(f"^Hola", texto, flags=re.M)
print(resultado)

# $ -> Buscando el final de una linea.
resultado = re.findall(f"capitan$", texto, flags=re.M)
print(resultado)

# {n} -> busca n cantidad de veces el valor de la izquierda.
resultado = re.findall(r"\d{3}", texto)
print(resultado)

# {n, m} -> al menos n como maximo m
resultado = re.findall(r"\d{2,4}", texto)
print(resultado)

# | -> busca una cosa o la otra -- En este caso devuelve ambas xq encontro ambas
resultado = re.findall(r"\d{2,4}|Hola", texto)
print(resultado)
