# Preparar datos de ejemplo
import pandas as pd
import os

# Crear directorio si no existe
os.makedirs('datos', exist_ok=True)

# Crear archivo CSV de ventas
ventas_csv = """fecha,cliente,producto,cantidad,precio_unitario,total
2024-01-15,Empresa A,Consultoría,40,150,6000
2024-01-16,Empresa B,Análisis,20,200,4000
2024-01-17,Empresa C,Desarrollo,60,180,10800
2024-01-18,Empresa A,Consultoría,30,150,4500
2024-01-19,Empresa D,Análisis,25,200,5000"""

with open('datos/ventas.csv', 'w', encoding='utf-8') as f:
    f.write(ventas_csv)

# Leer el archivo
df_ventas = pd.read_csv('datos/ventas.csv')
print("Datos de ventas:")
print(df_ventas)

columnas_a_importar = ['fecha', 'cliente', 'total']
df_ventas_filtrado = df_ventas[columnas_a_importar]
print("\nDatos de ventas filtrados:")
print(df_ventas_filtrado)
# Filtrar datos por cliente
cliente_especifico = 'Empresa A'
df_cliente_especifico = df_ventas_filtrado[df_ventas_filtrado['cliente'] == cliente_especifico]
print(f"\nDatos de ventas para el cliente {cliente_especifico}:")
print(df_cliente_especifico)
# Calcular estadísticas
estadisticas = df_ventas_filtrado['total'].describe()
print("\nEstadísticas de ventas:")
print(estadisticas)
# Guardar el DataFrame filtrado en un nuevo archivo CSV
df_ventas_filtrado.to_csv('datos/ventas_filtradas.csv', index=False)
# Crear un DataFrame de ejemplo para operaciones de agrupamiento
df_ventas_agrupado = df_ventas.groupby('cliente').agg({'cantidad': 'sum', 'total': 'sum'}).reset_index()
print("\nDatos de ventas agrupados por cliente:")
print(df_ventas_agrupado)
# Guardar el DataFrame agrupado en un nuevo archivo CSV
df_ventas_agrupado.to_csv('datos/ventas_agrupadas.csv', index=False)
# Crear un DataFrame de ejemplo para operaciones de ordenamiento
df_ventas_ordenado = df_ventas.sort_values(by='total', ascending=False)
print("\nDatos de ventas ordenados por total:")
print(df_ventas_ordenado)
# Guardar el DataFrame ordenado en un nuevo archivo CSV
df_ventas_ordenado.to_csv('datos/ventas_ordenadas.csv', index=False)
# Crear un DataFrame de ejemplo para operaciones de fusión
df_clientes = pd.DataFrame({
    'cliente': ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D'],
    'contacto': ['              contacto A', 'contacto B', 'contacto C', 'contacto D'],
    'telefono': ['123456789', '987654321', '456789123', '321654987']
})
df_empelados = pd.read_csv  ('datos/empleados.csv', encoding='utf-8')
# Fusionar DataFrames
df_ventas_fusionado = pd.merge(df_ventas, df_clientes, on='cliente', how='left')
print("\nDatos de ventas fusionados con información de clientes:")
print(df_ventas_fusionado)
# Guardar el DataFrame fusionado en un nuevo archivo CSV
df_ventas_fusionado.to_csv('datos/ventas_fusionadas.csv', index=False)
# Crear un DataFrame de ejemplo para operaciones de pivote
df_pivot = df_ventas.pivot_table(index='cliente', values='total', aggfunc='sum').reset_index()
print("\nTabla dinámica de ventas por cliente:")
print(df_pivot)
# Guardar la tabla dinámica en un nuevo archivo CSV
df_pivot.to_csv('datos/ventas_pivot.csv', index=False)
# Crear un DataFrame de ejemplo para operaciones de concatenación
df_ventas_extra = pd.DataFrame({
    'fecha': ['2024-01-20', '2024-01-21'],
    'cliente': ['Empresa E', 'Empresa F'],
    'producto': ['Consultoría', 'Análisis'],
    'cantidad': [15, 10],
    'precio_unitario': [150, 200],
    'total': [2250, 2000]
})
df_ventas_concatenado = pd.concat([df_ventas, df_ventas_extra], ignore_index=True)
print("\nDatos de ventas concatenados:")
print(df_ventas_concatenado)
# Guardar el DataFrame concatenado en un nuevo archivo CSV          
