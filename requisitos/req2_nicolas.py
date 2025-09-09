# Requerimiento Funcional 2: Descarga de Recursos Académicos
# Plataforma Estudiantil - Sistema Simple de Descarga

def obtener_recursos():
    """Retorna la lista de recursos disponibles"""
    return {
        1: {"nombre": "Manual de Python", "tipo": "PDF"},
        2: {"nombre": "Ejercicios Matemáticas", "tipo": "DOCX"},
        3: {"nombre": "Guía de SQL", "tipo": "PDF"},
        4: {"nombre": "Algoritmos Básicos", "tipo": "PDF"},
        5: {"nombre": "Plantilla HTML", "tipo": "DOCX"}
    }

def mostrar_recursos(recursos):
    """Muestra los recursos disponibles"""
    print("\n=== RECURSOS DISPONIBLES ===")
    for numero, info in recursos.items():
        print(f"{numero}. {info['nombre']} ({info['tipo']})")

def confirmar_descarga(recurso):
    """Confirma si el usuario quiere descargar el recurso"""
    print(f"\nRecurso: {recurso['nombre']}")
    print(f"Tipo: {recurso['tipo']}")
    
    respuesta = input("¿Confirmar descarga? (s/n): ")
    return respuesta.lower() in ['s', 'si', 'sí']

def descargar_recurso(recurso):
    """Simula la descarga del recurso"""
    print(f"\nDescargando {recurso['nombre']}...")
    print("Por favor espera...")
    print(f"Descarga completa: {recurso['nombre']}")

# def main():
#     """Función principal del sistema de descarga"""
#     recursos = obtener_recursos()
#     descargas = []
#     
#     print("📚 SISTEMA DE DESCARGA DE RECURSOS")
#     
#     nombre = input("Ingresa tu nombre: ")
#     print(f"¡Hola {nombre}!")
#     
#     while True:
#         mostrar_recursos(recursos)
#         
#         if descargas:
#             print(f"\nTus descargas:")
#             for recurso_id in descargas:
#                 print(f"- {recursos[recurso_id]['nombre']}")
#         
#         print("\nEscribe el número del recurso o 'salir'")
#         entrada = input("Opción: ")
#         
#         if entrada.lower() == 'salir':
#             break
#             
#         try:
#             numero_recurso = int(entrada)
#             
#             if numero_recurso in recursos:
#                 recurso = recursos[numero_recurso]
#                 
#                 if confirmar_descarga(recurso):
#                     descargar_recurso(recurso)
#                     descargas.append(numero_recurso)
#                 else:
#                     print("Descarga cancelada")
#             else:
#                 print("Recurso no existe")
#                 
#         except ValueError:
#             print("Ingresa un número válido")
#     
#     print(f"\n¡Gracias {nombre}! Descargaste {len(descargas)} recurso(s)")
# 
# if __name__ == "__main__":
#     main()