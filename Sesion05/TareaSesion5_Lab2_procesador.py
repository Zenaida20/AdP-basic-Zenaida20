# Tarea 1 de la Sesion 5
# Aplicacion de procesador 

def procesar_ventas(*args, **kwargs):
    
    # 1. Se debe validar que existan ventas
    if not args:
        return {"error": "No hay ventas para procesar"}
    
    # 2. Se debe reportar los resultados
    resultados = {}
    
    # 3. Se calcular el total (hacerlo por kwargs)
    if kwargs.get('calcular_total'):
        resultados['total'] = sum(args)
    
    # Encontrar máximo si se solicita
    if kwargs.get('buscar_el_maximo'):
        resultados['maximo'] = max(args)
    
    # Contar ventas superiores si se solicita
    if kwargs.get('contar_superiores'):
        umbral = kwargs.get('umbral', 0)
        resultados['superiores_a_umbral'] = len([v for v in args if v > umbral])
    
    return resultados

def procesador_ventas():
    # Casos de prueba
    ventas = [100, 200, 300, 150, 250, 385, 500]
    
    print("=== Procesador de Ventas ===")
    print(f"Ventas a procesar: {ventas}")
    
    # Caso 1: Calcular total y máximo
    resultado1 = procesar_ventas(*ventas, calcular_total=True, encontrar_maximo=True)
    print("\nCaso 1 - Total y Máximo:")
    print(f"Resultados: {resultado1}")
    
    # Caso 2: Contar ventas superiores
    resultado2 = procesar_ventas(*ventas, contar_superiores=True, umbral=200)
    print("\nCaso 2 - Ventas superiores a $200:")
    print(f"Resultados: {resultado2}")

if __name__ == "__main__":
    procesador_ventas()