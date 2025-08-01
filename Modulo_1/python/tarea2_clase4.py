# Diccionario inicial
alumnos = {
    "Luis": {"matematicas", "historia", "biologia"},
    "Ana": {"matematicas", "fisica", "quimica"},
    "Carlos": {"historia", "arte", "biologia"},
}

#  materias únicas
materias_unicas = set.union(*alumnos.values())
print("materias unicas: ", materias_unicas)

# materias comunes entre Luis y Ana
comunes_luis_ana = alumnos["Luis"].intersection(alumnos["Ana"])
print("materias comunes entre Luis y Ana:", comunes_luis_ana)

# agregar "fisica" a Carlos
alumnos["Carlos"].add("Física")

# eliminar "arte" de Carlos
alumnos["Carlos"].discard("arte")

# cada alumno y cantidad de materias
print("\n Alumnos y cantidad de materias:")
for alumno, materias in alumnos.items():
    print(f"{alumno}: {len(materias)} materias")
 