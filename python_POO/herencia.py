# Herencia simple
# Creando dos clases a partir de la clase Persona.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


emanuel = Empleado("Emanuel", 29, "argentino", "Programador", 100000)

print(emanuel.nacionalidad)
emanuel.hablar()

# Herencia multiple:

# Creamos una nueva clase: Artista


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return self.habilidad


# Ahora creamos la clase Empleado Artista

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    # Usando self definimos un metodo que se llama igual que un metodo heredado

    def mostrar_habilidad(self):
        return "No tengo jaja"

    # Usando super llamamos al metodo heredado de la clase Artista

    def presentarse(self):
        return f"Hola, soy {self.nombre} y mi habilidad es: {super().mostrar_habilidad()} y trabajo en: {self.empresa}"

# Creamos un empleado artista:


javier = EmpleadoArtista("Javier", 51, "argentino", "Pintor", 1000, "INCA")

# Llamamos a sus metodos.

print(javier.mostrar_habilidad())
print(javier.presentarse())
