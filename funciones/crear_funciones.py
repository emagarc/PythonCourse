# Creando uan funcion simple:

def saludar():
    print("Hola maestro como andas")


saludar()

# Creando una funcion que tenga parametros:


def saludar_con_param(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "femenino"):
        print(f"Hola Srta {nombre}, como andas?")
    if (sexo == "masculino"):
        print(f"Hola Sr. {nombre}, como estass?")


saludar_con_param("Emanuel", "Masculino")

# Crear una funcion que nos retorne valores:


def crear_contrasena_random(num):
    chars = "abcdefghijk"
    numero_entero = str(num)
    c1 = int(numero_entero[0]) - 2
    c2 = int(numero_entero[0])
    c3 = int(numero_entero[0]) - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c1]}{num * 2}"
    return contrasena


contrasena_generada = crear_contrasena_random(5978)
print(contrasena_generada)
