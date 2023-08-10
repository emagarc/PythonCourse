# Si el modulo estuviera e una carperta en la misma ruta se importa asi:

import sys
import funciones_buenas.modulo_saludito as saludo

saludito = saludo.saludar

bienvenida = saludito("Emanuel")
print(bienvenida)


print(sys.path)
