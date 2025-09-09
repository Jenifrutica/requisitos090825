# Requerimiento Funcional 6: Publicación de Notas
def obtener_notas():
    """Retorna la estructura de datos para almacenar notas por curso"""
    return {}

def validar_datos_nota(estudiante_nombre, calificacion, curso_id, tarea_id=None):
    """Valida los datos de la nota antes de publicarla"""
    if not estudiante_nombre or not estudiante_nombre.strip():
        return False, "El nombre del estudiante es obligatorio"
    
    try:
        calificacion_float = float(calificacion)
        if calificacion_float < 0 or calificacion_float > 10:
            return False, "La calificación debe estar entre 0 y 10"
    except (ValueError, TypeError):
        return False, "La calificación debe ser un número válido"
    
    if curso_id <= 0:
        return False, "ID de curso inválido"
    
    if tarea_id is not None and tarea_id <= 0:
        return False, "ID de tarea inválido"
    
    return True, "OK"

def publicar_nota(estudiante_nombre, calificacion, curso_id, notas, tarea_id=None, comentarios=""):
    """Publica una nueva nota para un estudiante en el curso especificado"""
    if curso_id not in notas:
        notas[curso_id] = []
    
    nueva_nota = {
        "id": len(notas[curso_id]) + 1,
        "estudiante": estudiante_nombre.strip(),
        "calificacion": float(calificacion),
        "curso_id": curso_id,
        "tarea_id": tarea_id,
        "comentarios": comentarios.strip() if comentarios else ""
    }
    
    notas[curso_id].append(nueva_nota)
    tarea_info = f" (Tarea ID: {tarea_id})" if tarea_id else ""
    print(f"Nota {calificacion} publicada exitosamente para {estudiante_nombre} en curso {curso_id}{tarea_info}")
    return nueva_nota["id"]

def mostrar_notas_curso(curso_id, notas, cursos):
    """Muestra todas las notas de un curso específico"""
    if curso_id not in notas or not notas[curso_id]:
        print(f"No hay notas publicadas para el curso: {cursos.get(curso_id, 'Desconocido')}")
        return
    
    print(f"\n=== NOTAS DEL CURSO: {cursos.get(curso_id, 'Desconocido')} ===")
    for nota in notas[curso_id]:
        print(f"ID: {nota['id']}")
        print(f"Estudiante: {nota['estudiante']}")
        print(f"Calificación: {nota['calificacion']}")
        if nota['tarea_id']:
            print(f"Tarea ID: {nota['tarea_id']}")
        if nota['comentarios']:
            print(f"Comentarios: {nota['comentarios']}")
        print("-" * 40)

def obtener_notas_estudiante(estudiante_nombre, curso_id, notas):
    """Obtiene todas las notas de un estudiante específico en un curso"""
    if curso_id not in notas:
        return []
    
    notas_estudiante = []
    for nota in notas[curso_id]:
        if nota["estudiante"].lower() == estudiante_nombre.lower():
            notas_estudiante.append(nota)
    
    return notas_estudiante

def calcular_promedio_estudiante(estudiante_nombre, curso_id, notas):
    """Calcula el promedio de notas de un estudiante en un curso"""
    notas_estudiante = obtener_notas_estudiante(estudiante_nombre, curso_id, notas)
    
    if not notas_estudiante:
        return None
    
    total_calificaciones = sum(nota["calificacion"] for nota in notas_estudiante)
    promedio = total_calificaciones / len(notas_estudiante)
    
    return round(promedio, 2)