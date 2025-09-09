# Requerimiento Funcional 5: Publicación de Tareas
def obtener_tareas():
    """Retorna la estructura de datos para almacenar tareas por curso"""
    return {}

def validar_datos_tarea(titulo, descripcion, fecha_entrega, curso_id):
    """Valida los datos de la tarea antes de publicarla"""
    if not titulo or not titulo.strip():
        return False, "El título de la tarea es obligatorio"
    
    if not descripcion or not descripcion.strip():
        return False, "La descripción de la tarea es obligatoria"
    
    if not fecha_entrega or not fecha_entrega.strip():
        return False, "La fecha de entrega es obligatoria"
    
    if curso_id <= 0:
        return False, "ID de curso inválido"
    
    return True, "OK"

def publicar_tarea(titulo, descripcion, fecha_entrega, curso_id, tareas):
    """Publica una nueva tarea en el curso especificado"""
    if curso_id not in tareas:
        tareas[curso_id] = []
    
    nueva_tarea = {
        "id": len(tareas[curso_id]) + 1,
        "titulo": titulo.strip(),
        "descripcion": descripcion.strip(),
        "fecha_entrega": fecha_entrega.strip(),
        "curso_id": curso_id
    }
    
    tareas[curso_id].append(nueva_tarea)
    print(f"Tarea '{titulo}' publicada exitosamente en el curso {curso_id}")
    return nueva_tarea["id"]

def mostrar_tareas_curso(curso_id, tareas, cursos):
    """Muestra todas las tareas de un curso específico"""
    if curso_id not in tareas or not tareas[curso_id]:
        print(f"No hay tareas publicadas para el curso: {cursos.get(curso_id, 'Desconocido')}")
        return
    
    print(f"\n=== TAREAS DEL CURSO: {cursos.get(curso_id, 'Desconocido')} ===")
    for tarea in tareas[curso_id]:
        print(f"ID: {tarea['id']}")
        print(f"Título: {tarea['titulo']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha de entrega: {tarea['fecha_entrega']}")
        print("-" * 40)

def obtener_tarea_por_id(tarea_id, curso_id, tareas):
    """Obtiene una tarea específica por su ID y curso"""
    if curso_id not in tareas:
        return None
    
    for tarea in tareas[curso_id]:
        if tarea["id"] == tarea_id:
            return tarea
    
    return None