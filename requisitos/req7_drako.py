# R1: Crear cursos virtuales y presenciales
print("1. Creando cursos:")

# Lista para almacenar los cursos
cursos = []

# Curso virtual
curso1 = "Matemáticas - Virtual"
cursos.append(curso1)
print(f" Creado: {curso1}")

# Curso presencial  
curso2 = "Historia - Presencial"
cursos.append(curso2)
print(f" Creado: {curso2}")

print(f"\nTotal cursos creados: {len(cursos)}")

# Mostrar todos los cursos
print("Lista de cursos:")
for i in range(len(cursos)):
    print(f"{i+1}. {cursos[i]}")
