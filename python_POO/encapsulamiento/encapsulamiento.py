# En python para declarar privado un atributo o valor usamos un _ al principio del atributo.

class MIClase:
    def __init__(self):
        self._atributo_privado = "Valor"

# Ahora si queremos llevar el atributo a un nivel mayor de encampsulamiento utilizamos el doble guion __


class MIClase2:
    def __init__(self):
        self.__atributo_privado = "Valor"

    def __hablar(self):
        print("Hola como estas!S")

# Ahora intentamos acceder al metodo hablar.
# Que deberia comentar aqui? se puede acceder a este metodo encapsulado?


objeto = MIClase()
print(objeto._atributo_privado)

# Creamos otros objetos instancias de MIClase2
# Que deberia comentar aqui? se puede acceder a este metodo encapsulado?

objeto2 = MIClase2()
print(objeto2.__atributo_privado)
