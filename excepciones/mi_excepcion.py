# Creando mi propia excepcion eprsonalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante cometiste el siguiente error: {err}")


# Manejando la excepcion
try:
    raise MiExcepcion("jajajajajaj, persona poco culta")
except:
    print("Como vas a cometer ese error?")

# Lanzando mi propia excepcion:
raise MiExcepcion("jajajaja persona poco culta")
