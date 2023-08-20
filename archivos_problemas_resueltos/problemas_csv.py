# Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos/datos.csv")
print(df)

# Convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

# Mostrar el tipo de dato del primer elemento de la columna edad.
print(type(df["edad"][0]))

# Reemplazando los datos garcia por Gutierres
df["apellido"].replace("garcia", "Gutierres", inplace=True)

# Mostrando la columna apellido
print(df["apellido"])

# Para eliminar las filas con datos vacios es:
df = df.dropna()

# Para eliminar las columnas con datos faltantes:
df = df.dropna(axis=1)

# Eliminando las filas repetidas:
df = df.drop_duplicates()

# Creando un CSV con el df resultante:

df.to_csv("archivos_problemas_resueltos/datos_limpios.csv")
