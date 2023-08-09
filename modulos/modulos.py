# Distintas formas de importar modulos.
import modulo_saludar
import modulo_saludar as m_saludar
from modulo_saludar import saludar
from modulo_saludar import saludar as bienvenida_a_lo_culiado

# Probamos usar la funcion saludar de las dos formas.
saludo = m_saludar.saludar("Emanuel")
print(saludo)
saludo2 = saludar("Mateo")
print(saludo2)
saludo3 = bienvenida_a_lo_culiado("Pablito")
print(saludo3)


# Printeamos el tipo o clase de elemento que es cada cosa.

print(type(modulo_saludar))
print(type(m_saludar))
print(type(saludar))
print(type(saludo2))

# Printeamos todas las propiedades y metodos de m_saludar

print(dir(m_saludar))

# Accedemos al nombre del modulo que importamos con otro nombre.

print(m_saludar.__name__)

# Accedemos al nombre del modulo actual va a decir main, ya que es el principal.

print(__name__)
