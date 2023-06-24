# Promedio de duracion en horas:

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

# Duracion de CRUDOS

crudo_promedio = 5
crudo_dalto = 3.5


# Diferencias de duracion:

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / \
    10  # para evitar muchos decimales (division baja)
diferencia_con_prom = 100 - dalto_curso / otros_cursos_prom * 100

# Calculando el porcentaje de tiempo vacio removido

tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 // crudo_promedio / 10

tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


# Mostrando als diferenciass de duracion (ejercicio A)
print("-------------------")
print("El curso de Dalto dura: ")
print(
    f" - El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido")

print(
    f" - El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")

print(
    f" - El curso de Dalto dura un {diferencia_con_prom}% menos que el promedio")

print("-------------------")

# Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo")
print(f"Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")
print("-------------------")

# Mostrando diferencias si los cursos duraran 10hs

print(
    f"Ver 10 hs de este curso equivale a ver {otros_cursos_prom * 100 // dalto_curso / 10} horas de otros cursos")

print(
    f"Ver 10 hs de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_prom / 10} horas de este curso")

print("-------------------")
