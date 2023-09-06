# Creamos dos clases con el mismo metodo pero distinto output.

class Gato():
    def sonido(self):
        return "Miau"


class Perro():
    def sonido(self):
        return "Guau"

# Creamos una funcion que toma el animal y ejecuta el metodo sonido.


def hacer_sonido(animal):
    print(animal.sonido())

# Creamos un perro y un gato


gato = Gato()
perro = Perro()

# Invocamos los metodos en cada animal (objeto creado)

# Hay polimorfismo ya que llamamos al mismo metodo con distintos objetos
hacer_sonido(gato)
hacer_sonido(perro)

# Hay polimorfismo porque printeamos el mismo metodo en distintos objetos
print(gato.sonido())
print(perro.sonido())

# Otro caso de polimorfismo


def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es {item}")


lista = [1, 2, 3, 4, 5]
lista2 = ["Maquina", "Perro", "Utensillo", "Plata", "Oro"]
lista3 = "ABECEDARIO"

recorrer(lista)
recorrer(lista2)
recorrer(lista3)

# Investigar sobre Duck Typing, Enlaces dinamicos y estaticos. Tipo real y tipo declarado.
