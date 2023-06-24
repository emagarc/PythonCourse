cadena1 = "Hola soy Emanuel"
cadena2 = "bienvenido Emanuel"

# Funcion DIR

# dir no es un metodo, es una funcion que nos devuelve informacion
resultado = dir(cadena1)
print(resultado)  # Print sería otra funcion.

# METODOS:

# UPPER

# Este metodo convierte toda la cadena en mayuscula.
resultado = cadena1.upper()
# Se escribe primero el dato, luego el metodo y los parentesis ()
print(resultado)

# LOWER

resultado = cadena1.lower()
print(resultado)

# CAPITALIZE ( primer letra mayuscula )

resultado = cadena2.capitalize()
print(resultado)

# FIND ( bucamos una cadena dentro de otra cadena)
# El metodo devuelve la posicion dentro de la  lista en la cual encuentra coincidencia.
# Si no encuentra nada devuelve -1

resultado = cadena1.find("soy")  # En este caso devuelve 5
print(resultado)

# INDEX
# El metodo INDEX si no encuentra nada devuelve una exepcion

resultado = cadena1.index("s")  # devuelve lo mismo
print(resultado)

# ISNUMERIC & ISALPHA

resultado = cadena1.isnumeric()
print(resultado)
resultado = cadena1.isalpha()
# da falso xq la cadena contiene espacios podrian eliminarse prev los espacios con replace
print(resultado)

# COUNT
# Nos dice cuantas veces encontro una coincidencia

resultado = cadena2.count("a")
print(resultado)  # en este caso es 1

# LEN
# Cuenta la cantidad de caracteres en una cadena

# Lo escribimos asi ya que LEN no es un metodo es una funcion.
resultado = len(cadena1)
print(resultado)

# ENDSWITH & STARTSWIDTH

# devuelve True dado que la cadena comienza con "b"
resultado = cadena2.startswith("b")
print(resultado)

# devuelve False xq la cadena no termina con "o"
resultado = cadena1.endswith("o")  # devuelve False
print(resultado)


# REPLACE
# Recibe dos parametros el primero es el parametro a replazar y el segundo el reemplazo.

resultado = cadena1.replace("la", "lu")  # devuelve "Holu soy Emanuel"
print(resultado)
