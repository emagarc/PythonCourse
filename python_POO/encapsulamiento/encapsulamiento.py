# En Python, para declarar un atributo como privado, utilizamos un guión bajo (_) al principio del nombre del atributo.

class MIClase:
    def __init__(self):
        self._atributo_privado = "Valor"  # Atributo privado con guión bajo al inicio

# Ahora, si queremos llevar el atributo a un nivel mayor de encapsulamiento, utilizamos el doble guion bajo (__).


class MIClase2:
    def __init__(self):
        # Atributo altamente privado con doble guion bajo al inicio
        self.__atributo_privado = "Valor"

    def __hablar(self):
        # Método privado con doble guion bajo al inicio
        print("Hola, ¿cómo estás?")

# Ahora intentamos acceder al método "hablar" y al atributo "__atributo_privado".
#¿Se puede acceder a estos elementos encapsulados?


# Para el primer objeto (MIClase), podemos acceder al atributo privado con un guion bajo:
objeto = MIClase()
print(objeto._atributo_privado)

# Para el segundo objeto (MIClase2), intentamos acceder al atributo altamente privado con doble guion bajo.
# Esto generará un error ya que Python realiza una modificación del nombre del atributo para hacerlo más privado.
# Por lo tanto, deberíamos comentar que este acceso generará un error:
objeto2 = MIClase2()
print(objeto2.__atributo_privado)

# Creamos otros objetos instancias de MIClase2
# ¿Qué deberíamos comentar aquí? ¿Se puede acceder al método encapsulado?


# Intentar acceder al método "__hablar" generará un error similar al del atributo "__atributo_privado".
# Deberíamos comentar que este acceso también generará un error:
objeto2.__hablar()
