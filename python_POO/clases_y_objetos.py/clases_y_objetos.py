class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
# Siempre se les pasa el parametro self a los metodos de un clase

    def llamar(self):
        print(f"Estas haciendo un llamado desde un {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada desde un {self.modelo}")


celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")

# Llamando a los métodos de los celulares, instancias de la clase Celular
celular1.llamar()
celular2.cortar()
