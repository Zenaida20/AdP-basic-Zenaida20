# Archivo: lab_02_filtrado_solucion.py
"""
Laboratorio 2: Filtrado de Datos (SOLUCIÓN)
Objetivo: Practicar filtrado de datos usando bucles y condiciones
"""

def filtrar_productos(productos, min_precio, max_precio, categoria):
    """
    Filtra una lista de productos según criterios específicos
    Args:
        productos (list): Lista de diccionarios con información de productos
        min_precio (float): Precio mínimo a considerar
        max_precio (float): Precio máximo a considerar
        categoria (str): Categoría de productos a filtrar
    Returns:
        list: Lista de productos que cumplen los criterios
    """
    # Lista para almacenar productos filtrados
    productos_filtrados = []
    
    # Procesar cada producto
    for producto in productos:
        # Verificar todos los criterios
        precio_valido = min_precio <= producto['precio'] <= max_precio
        tiene_stock = producto['stock'] > 0
        categoria_correcta = producto['categoria'] == categoria
        
        # Si cumple todos los criterios, agregar a la lista
        if precio_valido and tiene_stock and categoria_correcta:
            productos_filtrados.append(producto)
    
    return productos_filtrados

def main():
    # Casos de prueba
    productos = [
        {"nombre": "Laptop", "precio": 1200, "stock": 5, "categoria": "Electrónica"},
        {"nombre": "Mouse", "precio": 25, "stock": 10, "categoria": "Electrónica"},
        {"nombre": "Libro", "precio": 30, "stock": 0, "categoria": "Libros"},
        {"nombre": "Monitor", "precio": 300, "stock": 3, "categoria": "Electrónica"}
    ]
    
    print("=== Filtrado de Productos ===")
    print("\nCriterios de filtrado:")
    print("- Precio entre $20 y $500")
    print("- Con stock disponible")
    print("- Categoría: Electrónica")
    
    filtrados = filtrar_productos(productos, 20, 500, "Electrónica")
    print("\nProductos que cumplen los criterios:")
    for producto in filtrados:
        print(f"- {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")

if __name__ == "__main__":
    main()