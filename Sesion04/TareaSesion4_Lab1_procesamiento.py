# Tarea 1 de la Sesion 4
# Procesamientos de datos 

# Uso de bucles aplicado al procesamiento de datos

# 1. De la lista de ventas se debe generar estadisticas: (suma, maximo, minimo, promedio)

def analizar_ventas(ventas, umbral):

# 1. Inicializar variables
    total_ventas = 0
    venta_maxima = ventas[0] if ventas else 0
    ventas_altas = 0
    
    # 2. Procesar cada venta
    for venta in ventas:
        # 2.1 Ventas totales
        total_ventas += venta
        
        # 2.2 Venta máxima
        if venta > venta_maxima:
            venta_maxima = venta
            
        # 2.3 Venta mas alta
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

