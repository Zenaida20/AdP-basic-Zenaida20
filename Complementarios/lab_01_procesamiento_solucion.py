# Archivo: lab_01_procesamiento_solucion.py
"""
Laboratorio 1: Procesamiento de Datos (SOLUCIÓN)
Objetivo: Practicar el uso de bucles para procesar datos
"""

def analizar_ventas(ventas, umbral):
    """
    Analiza una lista de ventas y genera estadísticas
    Args:
        ventas (list): Lista de montos de ventas
        umbral (float): Valor para comparar ventas
    Returns:
        dict: Diccionario con estadísticas de ventas
    """
    # Inicializar variables
    total_ventas = 0
    venta_maxima = ventas[0] if ventas else 0
    ventas_altas = 0
    
    # Procesar cada venta
    for venta in ventas:
        # Actualizar total
        total_ventas += venta
        
        # Actualizar máximo
        if venta > venta_maxima:
            venta_maxima = venta
            
        # Contar ventas altas
        if venta > umbral:
            ventas_altas += 1
    
    # Retornar resultados
    return {
        "total": total_ventas,
        "maxima": venta_maxima,
        "num_ventas_altas": ventas_altas
    }

def main():
    # Casos de prueba
    ventas_dia = [100, 200, 50, 300, 150, 80]
    umbral_alto = 150
    
    print("=== Análisis de Ventas ===")
    print(f"Ventas del día: {ventas_dia}")
    print(f"Umbral para ventas altas: ${umbral_alto}")
    
    resultados = analizar_ventas(ventas_dia, umbral_alto)
    print("\nResultados:")
    print(f"Total de ventas: ${resultados['total']}")
    print(f"Venta más alta: ${resultados['maxima']}")
    print(f"Número de ventas altas: {resultados['num_ventas_altas']}")

if __name__ == "__main__":
    main()