# Definición de un decorador llamado 'decorador'
def decorador(funcion):
    # Definición de una función interna llamada 'funcion_modificada'
    def funcion_modificada():
        # Imprime un mensaje antes de llamar a la función original
        print("Antes de llamar a la función")
        funcion()  # Llama a la función original que fue pasada como argumento a 'decorador'

    # Devuelve la función interna 'funcion_modificada', que actúa como una versión modificada de la función original
    return funcion_modificada

# Definición de una función 'saludo'


# def saludo():
#     print("Hola soy Emanuel, ¿cómo estás?")


# # Aplicación del decorador 'decorador' a la función 'saludo'
# # Esto crea una nueva función llamada 'saludo_modificado' que tiene el comportamiento modificado por el decorador
# saludo_modificado = decorador(saludo)

# # Llama a la función 'saludo_modificado', que ejecutará la versión modificada de 'saludo'
# saludo_modificado()

# LO DE ARRIBA COMENTADO SE REALIZA DE LA SIGUIENTE MANERA:

@decorador
def saludo():
    print("Hola soy dalto como Andas")


saludo()
