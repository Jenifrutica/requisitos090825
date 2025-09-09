# R2: Inscribir estudiantes
print(" Inscribiendo estudiantes:")

# Inicializar listas y cursos
estudiantes = []
cursos = []
curso1 = "Matemáticas - Virtual"
curso2 = "Historia - Presencial"
cursos.append(curso1)
cursos.append(curso2)

# Crear algunos estudiantes
estudiante1 = "Juan Pérez"
estudiante2 = "María García" 
estudiante3 = "Carlos López"

estudiantes.append(estudiante1)
estudiantes.append(estudiante2)
estudiantes.append(estudiante3)

print(f"Estudiantes registrados: {len(estudiantes)}")

# Mostrar estudiantes
print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(f"- {estudiante}")

# Inscripciones simples
print("Realizando inscripciones:")

# Juan se inscribe en Matemáticas
print(f"{estudiante1} se inscribió en {curso1}")

# María se inscribe en Historia
print(f" {estudiante2} se inscribió en {curso2}")

# Carlos se inscribe en Matemáticas
print(f" {estudiante3} se inscribió en {curso1}")

# Mostrar resumen final
print("=== RESUMEN FINAL ===")
print(f"Total estudiantes: {len(estudiantes)}")
print(f"Total cursos: {len(cursos)}")
print(f"Inscripciones realizadas: 3")

print("\nCursos disponibles:")
for curso in cursos:
    if "Virtual" in curso:
        print(f"{curso}")
    else:
        print(f"{curso}")

print("¡Sistema funcionando correctamente!")