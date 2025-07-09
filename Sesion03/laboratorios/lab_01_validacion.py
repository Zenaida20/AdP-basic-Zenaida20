# Archivo: lab_01_validacion.py
"""
Laboratorio 1: Validación Básica de Datos
Objetivo: Practicar el uso de operadores de comparación y condicionales

La función debe validar:
1. El precio debe ser mayor que 0
2. El stock debe ser mayor o igual a 0

Si alguna validación falla, debe lanzar una excepción ValueError con el mensaje específico del error.
"""

def validar_producto(precio, stock):
    """
    Validar si un producto cumple con los requisitos mínimos
    Args:
        precio (float): Precio del producto
        stock (int): Cantidad en inventario
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa la función
        ValueError: Cuando alguna validación falla
    """
    # TODO: Implementar las validaciones siguiendo estos pasos:
    # 1. Primero, validar que el precio sea mayor que 0
    #    - Si no lo es, lanzar ValueError con mensaje "El precio debe ser mayor que 0"
    
    # TODO: Escribe tu código de validación de precio aquí
    
    
    # 2. Luego, validar que el stock no sea negativo
    #    - Si es negativo, lanzar ValueError con mensaje "El stock no puede ser negativo"
    
    # TODO: Escribe tu código de validación de stock aquí
    
    
    # 3. Si llegamos aquí, significa que todo está válido
    #    - Puedes retornar True o cualquier otro valor que indique éxito
    
    # Por ahora, lanzamos NotImplementedError para indicar que falta implementar
    raise NotImplementedError("¡Función no implementada! Debes escribir el código de validación.")

def main():
    # Casos de prueba
    productos = [
        {"precio": 100, "stock": 5},
        {"precio": -50, "stock": 0},
        {"precio": 75.5, "stock": -1}
    ]
    
    print("=== Validación de Productos ===")
    
    for i, producto in enumerate(productos, 1):
        print(f"\nProducto {i}:")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']}")
        
        try:
            validar_producto(producto["precio"], producto["stock"])
            print("Estado: Válido")
        except NotImplementedError as e:
            print(f"Estado: {str(e)}")
        except ValueError as e:
            print(f"Estado: Error - {str(e)}")

if __name__ == "__main__":
    main()