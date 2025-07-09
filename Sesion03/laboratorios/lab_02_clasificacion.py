# Archivo: lab_02_clasificacion.py
"""
Laboratorio 2: Clasificación de Productos
Objetivo: Practicar estructuras if-elif-else

El sistema debe clasificar productos según su precio:
- Menos de 50: "Económico"
- Entre 50 y 100: "Estándar"
- Más de 100: "Premium"

Si el precio es negativo o 0, debe lanzar una excepción ValueError.
"""

def clasificar_producto(precio):
    """
    Clasifica un producto según su precio
    Args:
        precio (float): Precio del producto
    Returns:
        str: Categoría del producto (Económico, Estándar, Premium)
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa la función
        ValueError: Cuando el precio es inválido (negativo o cero)
    """
    # TODO: Implementar la clasificación siguiendo estos pasos:
    # 1. Primero, validar que el precio sea mayor que 0
    #    - Si no lo es, lanzar ValueError con mensaje "El precio debe ser mayor que 0"
    
    # TODO: Escribe tu código de validación aquí
    
    
    # 2. Luego, implementar la lógica de clasificación usando if-elif-else
    #    - Si precio < 50: retornar "Económico"
    #    - Si precio está entre 50 y 100: retornar "Estándar"
    #    - Si precio > 100: retornar "Premium"
    
    # TODO: Escribe tu código de clasificación aquí
    
    
    # Por ahora, lanzamos NotImplementedError para indicar que falta implementar
    raise NotImplementedError("¡Función no implementada! Debes escribir el código de clasificación.")

def main():
    # Casos de prueba
    precios = [25.99, 75.50, 150.00, -10.00]
    
    print("=== Clasificación de Productos ===")
    
    for precio in precios:
        print(f"\nPrecio: ${precio}")
        try:
            categoria = clasificar_producto(precio)
            print(f"Categoría: {categoria}")
        except NotImplementedError as e:
            print(f"Estado: {str(e)}")
        except ValueError as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()