# Tarea 2 de la Sesion 3 
# Clasificación de productos

# Definición de las premisas en el procedimiento y obtención de resultados
# Aplicacion de las estructuras if-elif-else

#1. Clasificar productos según su precio: 
#   1.1 Si es menor a 50 es: "Económico"
#   1.2 Si es mayor o igual a 50 y menor o igual a 100 es: "Estándar"
#   1.3 Si es mayor a 100 es: "Premium"

def clasificar_producto(precio):
    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")
        
    if precio < 50:
        return "Económico"
    elif precio <= 100:
        return "Estándar"
    else:
        return "Premium"

def resultados():
    # Lista de precios de productos para clasificar
    precios = [25.99, 75.50, 150.00]
    
    print("=== Clasificación de Productos ===")
    
    for precio in precios:
        categoria = clasificar_producto(precio)
        print(f"\nPrecio: ${precio}")
        print(f"Categoría: {categoria}")

if __name__ == "__main__":
    resultados()