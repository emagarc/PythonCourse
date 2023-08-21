# Creando una funcion que suma numeros:

def sumar_dos():
    # Iniciando un bucle
    while True:
        # Pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
            # Si lanzo una excepcion pedirle que reingrese los datos.
        except Exception as e:
            print("Por favor inserte solo un numero de base 10")
            print(f"Error: {type(e).__name__}")
            # Si todo salio bien finalizamos el bucle
        else:
            break
        finally:
            print("Manejo de excepcion finalizado")
    # Mostrando el resultado
    return resultado


print(sumar_dos())
