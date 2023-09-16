class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad

    @property
    def nombre(self):
        """
        Getter: Retorna el valor del atributo privado __nombre.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        """
        Setter: Permite establecer un nuevo valor para el atributo privado __nombre.
        """
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        """
        Deleter: Permite eliminar el atributo privado __nombre.
        """
        del self.__nombre


emanuel = Persona("Emanuel", 29)

# Usamos el getter para obtener el nombre
nombre = emanuel.nombre
print("Nombre inicial:", nombre)

# Usamos el setter para cambiar el nombre
emanuel.nombre = "Nuevo Nombre"
print("Nombre modificado:", emanuel.nombre)

# Usamos el deleter para eliminar el nombre
del emanuel.nombre
# Si intentamos acceder al nombre ahora, obtendremos un error porque se ha eliminado
# Aquí manejo la excepción para que no cause un error en el programa.
try:
    print("Nombre después de eliminar:", emanuel.nombre)
except AttributeError:
    print("El atributo 'nombre' ha sido eliminado.")
