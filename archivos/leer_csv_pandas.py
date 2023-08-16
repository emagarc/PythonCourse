import pandas as pd

# usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos/datos.csv")


# Obteniendo los datos de la columna nombre
print(df["nombre"])

# Ordernamos a data frame por edad
df_ordenado = df.sort_values("edad")
print(df_ordenado)

# Ordenando de forma descendente
df_ordenado_des = df.sort_values("edad", ascending=False)
print(df_ordenado_des)

# Concatenamos dos archivos
df2 = pd.read_csv("archivos/datos.csv")

df_concatenado = pd.concat([df, df2])
print(df_concatenado)

# Accediendo a la primer fila con head(1)
primer_fila = df.head(1)
print(f"Esta es la primer fila {primer_fila}")

# Accediendo a las primeras 2 filas con heaad(2)
primeras_dos_filas = df.head(2)
print(f"Estas son las primeras dos filas {primeras_dos_filas}")

# Accediendo a las dos ultimas filas con tail(2)
ultimas_dos_filas = df.tail(2)
print(f"Estas son las ultimas dos filas {ultimas_dos_filas}")

# Accediendo a la cantidad de filas (primero) y columnas(segundo) con shape
filas_y_columnas_totales = df.shape

# nos devuelve una tupla (3, 4)
print(filas_y_columnas_totales)

# Desenpaquetando
filas_totales, columnas_totales = df.shape
print(filas_totales)
print(columnas_totales)

# Obteniendo ata estadistica del dataframe:
df_info = df.describe()
print(df_info)

# Accediendo a un elemento especifico del df con loc
# Accediendo a la edad de la fila 2
elemento_esp = df.loc[2, "edad"]
print(elemento_esp)

# Accediendo a la edad de la fila 2 con iloc
elemento_esp = df.iloc[2, 2]
print(elemento_esp)

# Accediendo a todas las filas de una columna.
apellidos = df.iloc[:, 1]
print(apellidos)

# Accediendo a filas con edad mayor de 30
mayor_que_30 = df.loc[df["edad"] > 30, :]
print(mayor_que_30)
