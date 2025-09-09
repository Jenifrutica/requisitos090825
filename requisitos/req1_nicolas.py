# Requerimiento Funcional 1: Inscripción a Cursos
# Plataforma Estudiantil - Sistema Simple de Inscripciones

def obtener_cursos():
    """Retorna la lista de cursos disponibles"""
    return {
        1: "Programación en Python",
        2: "Matemáticas Discretas", 
        3: "Bases de Datos",
        4: "Algoritmos y Estructuras",
        5: "Desarrollo Web"
    }

def mostrar_cursos(cursos):
    """Muestra los cursos disponibles"""
    print("\n=== CURSOS DISPONIBLES ===")
    for numero, nombre in cursos.items():
        print(f"{numero}. {nombre}")

def validar_curso(numero, cursos, inscripciones):
    """Valida si se puede inscribir al curso"""
    if numero not in cursos:
        return False, "Curso no existe"
    
    if numero in inscripciones:
        return False, "Ya estás inscrito en este curso"
    
    return True, "OK"

def inscribir_curso(numero, cursos, inscripciones):
    """Inscribe al estudiante en el curso"""
    inscripciones.append(numero)
    print(f"Te inscribiste exitosamente en: {cursos[numero]}")

#def main():
#    """Función principal del sistema de inscripciones"""
#    cursos = obtener_cursos()
#    inscripciones = []
#    
#    print("SISTEMA DE INSCRIPCIÓN A CURSOS")
#    
#    nombre = input("Ingresa tu nombre: ")
#    print(f"¡Hola {nombre}!")
#    
#    while True:
#        mostrar_cursos(cursos)
#        
#        if inscripciones:
#            print(f"\nTus inscripciones:")
#            for curso_id in inscripciones:
#                print(f"- {cursos[curso_id]}")
#        
#        print("\nEscribe el número del curso o 'salir'")
#        entrada = input("Opción: ")
#        
#        if entrada.lower() == 'salir':
#            break
#            
#        try:
#            numero_curso = int(entrada)
#            es_valido, mensaje = validar_curso(numero_curso, cursos, inscripciones)
#            
#            if es_valido:
#                inscribir_curso(numero_curso, cursos, inscripciones)
#            else:
#                print(f"Error: {mensaje}")
#                
#        except ValueError:
#            print("Ingresa un número válido")
#    
#    print(f"\n¡Gracias {nombre}! Te inscribiste en {len(inscripciones)} curso(s)")
#
#if __name__ == "__main__":
#    main()