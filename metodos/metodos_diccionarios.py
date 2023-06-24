diccionario = {
    "nombre": "Emanuel",
    "apellido": "Garcia",
    "edad": 29,
    "is_student": True
}

# Ver las claves del diccionario

claves = diccionario.keys()
print(claves)

# GET

# Devuelve True ( si no encuentra lanza exepcion)
is_student = diccionario.get("is_student")
print(is_student)


# POP
# eliminando un elemento del diccionario

diccionario.pop("apellido")  # solo recibe un parametro
print(diccionario)

# Obteniendo un elemento dict_items de un diccionario

diccionario_iterable = diccionario.items()
print(diccionario_iterable)


# CLEAR
# elimina todo el diccionario

diccionario.clear()
print(diccionario)
