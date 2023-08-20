# 2 listas, una con nombres la otra con apellidos.
nombres = ["Emanuel", "Pedro", "Camila", "Joaquin", "Roberto"]
apellidos = ["Garcia", "Hernandez", "De Petris", "Fernandez", "Gonzalez"]

# Registrar esta informacion en un txt de forma optima.

with open("archivos_problemas_resueltos/nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n")
     for n, a in zip(nombres, apellidos)]

# Haciendo lo mismo:

# for n, a in zip(nombres, apellidos):
#    arch.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n")
