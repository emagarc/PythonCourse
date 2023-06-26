# Creando diccionarios con dict();

diccionario = dict(nombre="Emanuel", apellido="Garcia")

# Las listas no pueden ser claves si usamos frozenset para meter conjuntos

diccionario = {frozenset(["Ema", "rancio"]): "jajajaj"}

# Creando diccionarios con fromkeys() cada clave tiene none como valor

# Le pasamos una lista // alor por defecto: none

diccionario = dict.fromkeys(["nombre", "apellido", "suscriptores"])

# Cuando lo hacemos de la siguiente forma es un iterable sobre el primer atributo cada caracter es una clave y
# y si ponemos segundo parametro es el valor

diccionario = dict.fromkeys("EMA", "GARCIA")

print(diccionario)

# Creando diccionario con fromkeys() valor por defecto a "no se"

diccionario = dict.fromkeys(["nombre", "apellido"], "No Se")


print(diccionario)
