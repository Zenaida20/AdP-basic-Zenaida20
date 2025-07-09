import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Dataset de ventas para análisis
ventas = pd.DataFrame({
    'venta_id': ['V001', 'V002', 'V003', 'V004', 'V005', 'V006', 'V007', 'V008'],
    'cliente': ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa A', 'Empresa D', 'Empresa B', 'Empresa C', 'Empresa E'],
    'producto': ['Consultoría', 'Software', 'Consultoría', 'Training', 'Software', 'Consultoría', 'Training', 'Software'],
    'cantidad': [1, 2, 1, 3, 1, 2, 2, 1],
    'precio_unitario': [50000, 25000, 75000, 15000, 30000, 60000, 20000, 35000],
    'descuento_pct': [0, 5, 10, 0, 15, 8, 5, 12],
    'fecha_venta': ['2024-01-15', '2024-01-20', '2024-02-10', '2024-02-15', '2024-03-05', '2024-03-10', '2024-03-20', '2024-04-01'],
    'vendedor': ['Ana', 'Carlos', 'María', 'Ana', 'Pedro', 'Carlos', 'María', 'Pedro']
})

# Convertir fecha a datetime
ventas['fecha_venta'] = pd.to_datetime(ventas['fecha_venta'])
print(ventas.info())
print(ventas.head())

# Ejercicio 1: Métricas Básicas
# TODO: Crear las siguientes columnas:

# Parte 1: 'Precio_con_descuento': precio unitario después del descuento
ventas['precio_con_descuento'] = ventas['precio_unitario'] * (1 - ventas['descuento_pct'] / 100)   

# 2. 'Categoria_Precio': 'Alto' si precio_unitario > 40000, sino 'Normal'
ventas['categoria_precio'] = np.where(ventas['precio_unitario'] > 40000, 'Alto', 'Normal')      
   
# 3. 'Mes_Texto': nombre del mes de la venta (dt.strftime('%B') identidica el mes en texto)
ventas['mes_texto'] = ventas['fecha_venta'].dt.strftime('%B')   

print (ventas [['precio_unitario','precio_con_descuento', 'categoria_precio', 'mes_texto']])

#Ejercicio 2: Análisis Temporal
# TODO: Crear columnas que muestren:

# Parte 1. 'trimestre_texto': 'Q1', 'Q2', etc.
ventas['trimestre_texto'] = 'Q' + ((ventas['fecha_venta'].dt.month - 1) // 3 + 1).astype(str)  

# Parte 2. 'es_primer_semestre': True si la venta fue en los primeros 6 meses del año     
ventas['es_primer_semestre'] = ventas['fecha_venta'].dt.month <= 6

# Parte 3. 'semanas_desde_inicio': semanas transcurridas desde la primera (// da la division entera-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------)
ventas['semanas_desde_inicio'] = ((ventas['fecha_venta'] - ventas['fecha_venta'].min()).dt.days // 7)
print(ventas[['fecha_venta', 'trimestre_texto', 'es_primer_semestre', 'semanas_desde_inicio']])     

#Ejercicio 3: Función Personalizada
# TODO: Crear una función que evalúe el 'potencial_cliente':

# - 'Alto': si tiene más de 1 compra Y valor total > 50000
# - 'Medio': si tiene 1 compra Y valor > 30000, O más compras con valor total <= 50000
# - 'Bajo': otros casos

def evaluar_potencial_cliente(cantidad_compras, valor_total_cliente):
    if cantidad_compras > 1 and valor_total_cliente > 50000:
        return 'Alto'
    elif cantidad_compras == 1 and valor_total_cliente > 30000:
        return 'Medio'
    else:               
        return 'Bajo'
      
# Aplicar la función al DataFrame
ventas['valor_total_cliente'] = ventas.groupby('cliente')['precio_con_descuento'].transform('sum')
ventas['cantidad_compras'] = ventas.groupby('cliente')['venta_id'].transform('count')
ventas['potencial_cliente'] = ventas.apply(lambda row: evaluar_potencial_cliente(row['cantidad_compras'], row['valor_total_cliente']), axis=1)  

ventas_copia = ventas.copy()
ventas_copia['total_bruto'] = ventas_copia['cantidad'] * ventas_copia['precio_unitario']
ventas_copia['descuento_monto'] = ventas_copia['total_bruto'] * (ventas_copia['descuento_pct'] / 100)
ventas_copia['total_neto'] = ventas_copia['total_bruto'] - ventas_copia['descuento_monto']
# Agrupar por cliente para obtener métricas
cliente_resumen = ventas_copia.groupby('cliente').agg({
    'venta_id': 'count',
    'total_neto': 'sum'
}).rename(columns={'venta_id': 'num_compras', 'total_neto': 'valor_total'}).reset_index()

def clasificar_potencial(row):
    num_compras = row['num_compras']
    valor_total = row['valor_total']
    
    if num_compras > 1 and valor_total > 50000:
        return 'Alto'
    elif (num_compras == 1 and valor_total > 30000) or (num_compras > 1 and valor_total <= 50000):
        return 'Medio'
    else:
        return 'Bajo'
# Aplicar la clasificación
cliente_resumen['potencial_cliente'] = cliente_resumen.apply(clasificar_potencial, axis=1)
print( cliente_resumen[['cliente','potencial_cliente']])