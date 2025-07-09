# Tarea 1 de la Sesion 5
# Aplicacion de la calculadora

def calcular_precio_final(precio_base, cantidad, descuento=0):
    
    # 1. Validar valores
    if precio_base <= 0:
        raise ValueError("El precio base debe ser mayor que 0")
    if cantidad <= 0:
        raise ValueError("Da error cuando la cantidad debe ser mayor que 0")
    if not 0 <= descuento <= 1:
        raise ValueError("El descuento debe estar entre 0 y 1")
    
    # 2. Calcular subtotal
    subtotal = precio_base * cantidad
    
    # 3. Aplicar descuento
    subtotal_con_descuento = subtotal * (1 - descuento)
    
    # 4. Inclusión del IVA
    precio_final = subtotal_con_descuento * 0.19
    
    return round(precio_final, 2)

def calculadora():
    # Casos de prueba
    print("=== Calculadora de Precios ===")
    
    # Caso 1: Sin descuento
    precio1 = calcular_precio_final(100, 2)
    print(f"\nCaso 1 - Precio base: $100, Cantidad: 2")
    print(f"Precio final: ${precio1}")
    
    # Caso 2: Con descuento
    precio2 = calcular_precio_final(100, 2, 0.1)
    print(f"\nCaso 2 - Precio base: $100, Cantidad: 2, Descuento: 10%")
    print(f"Precio final: ${precio2}")

if __name__ == "__main__":
    calculadora()