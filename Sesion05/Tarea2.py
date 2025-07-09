# Producciones diarias de la semana (lunes a domingo)
producciones = [145, 152, 148, 160, 155, 142, 158]

print("=== ANÁLISIS DE PRODUCCIÓN SEMANAL ===")

# TODO 1: Calcula y muestra la producción total de la semana
total_produccion = sum(producciones)
print(f"Producción total de la semana: {total_produccion} unidades")


# TODO 2: Encuentra el día con mayor producción (pista: usa max() e index())
mayor_produccion = max(producciones)
indice_mayor = producciones.index(mayor_produccion)+1
print(f"Día con mayor producción: {indice_mayor} con {mayor_produccion} barriles")


# TODO 3: Encuentra el día con menor producción
min_produccion = min(producciones)
indice = producciones.index(min_produccion)
print(f"Día con menor producción: {indice} con {min_produccion} barriles)")



# TODO 4: Calcula el promedio de producción diaria
promedio = sum ( / len(producciones)
print(f"Promedio de producción diaria: {promedio:.2f} barriles")


# TODO 5: Muestra las producciones de los primeros 3 días
primeros_3_dias = producciones[:3]
print(f"Producción de los primeros 3 días (Lunes a Miércoles): {primeros_3_dias}")