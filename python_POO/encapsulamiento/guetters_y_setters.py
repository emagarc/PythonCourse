class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

# Creamos el objeto de la clase Persona


emanuel = Persona("Emanuel", 29)

# Accedemos a su propiedad privada mediante su getter

nombre = emanuel.get_nombre()
print(nombre)

# Seteamos su nuevo nombre

emanuel.set_nombre("Andres")

# Actualizamos el valos de la variable nombre y comprobamos que se actualizo el nombre del objeto emanuel
nombre = emanuel.get_nombre()
print(nombre)
