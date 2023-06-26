diccionario = {
    "nombre": "Emanuel",
    "apellido": "Garcia",
    "subs": 1000000
}

print(diccionario)

# Recorriendo un diccioanrio para obtener las claves

for key in diccionario.items():
    key
    print(f"La clave es: {key}")

# Recorriendo un diccionario con items() para obtener la clave y el valor

for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"La clave es: {key} y el valor es: {valor}")
