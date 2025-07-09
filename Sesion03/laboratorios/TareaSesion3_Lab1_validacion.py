# Tarea 1 de la Sesion 3 
# Validación de datos basicos de productos

# Definición de las premisas en el procedimiento y obtención de resultados

# 1. El precio debe ser mayor que 0, si es menor a 0, debe indicar (ValueError = "El precio debe ser mayor a 0")
# 2. El stock (disponible) debe ser mayor o igual a 0

def validar_producto(precio, stock):
    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")
    if stock < 0:
        raise ValueError("El stock no puede ser negativo")
    return True

def resultados():
    productos = [
        {"precio": 100, "stock": 5},    # Debe ser válido
        {"precio": -50, "stock": 0},    # Inválido por precio negativo
        {"precio": 75.5, "stock": -1}   # Inválido por stock negativo
    ]
    print("=== Validación de Productos ===")
    for i, producto in enumerate(productos, 1):
        print(f"\nProducto {i}:")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']}")
        
if __name__ == "__main__":
    resultados()

 