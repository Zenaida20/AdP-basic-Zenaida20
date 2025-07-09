# Libreria necesaria para inciar el análisis de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display


# Creando la dataset 
np.random.seed(42)
data = {
    'fecha': pd.date_range('2024-01-01', periods=1000, freq='H'),
    'producto': np.random.choice(['Laptop', 'Smartphone', 'Tablet', 'Auriculares'], 1000),
    'categoria': np.random.choice(['Electrónica', 'Accesorios'], 1000),
    'precio': np.random.uniform(100, 1000, 1000).round(2),
    'cantidad': np.random.randint(1, 5, 1000),
    'canal': np.random.choice(['Online', 'Tienda'], 1000)
}

df = pd.DataFrame(data)

print('Primeras 5 filas del DataFrame:')
display(df.head())

print('\nInformación del DataFrame:')
df.info()

print('\nEstadísticas descriptivas:')
display(df.describe())

print('\nValores únicos por columna:')
for col in ['producto', 'categoria', 'canal']:
    print(f'\n{col.title()}:')
    display(df[col].value_counts())
    
# Calculo de las ventas 
df['ventas'] = df['precio'] * df['cantidad']

#  Cálculo de métricas generales
print('\nCálculo de métricas generales:') 

metricas = {
    'Ventas Totales': df['ventas'].sum(),
    'Ticket Promedio': df['ventas'].mean(),
    'Número de Transacciones': len(df),
    'Cantidad Total Vendida': df['cantidad'].sum()
}

print('Métricas Generales:')
metricas_df = pd.DataFrame(metricas.items(), columns=['Métrica', 'Valor'])
metricas_df['Valor'] = metricas_df['Valor'].round(2)
display(metricas_df)

# Análisis por categoría
print('\nVentas por Categoría:')
ventas_categoria = df.groupby('categoria').agg({
    'ventas': ['sum', 'mean', 'count'],
    'cantidad': 'sum'
}).round(2)
display(ventas_categoria)

# El producto "Top"
print('\nTop Productos por Ventas:')
display(df.groupby('producto')['ventas'].sum().sort_values(ascending=False))

# Análisis temporal
df['hora'] = df['fecha'].dt.hour
df['dia'] = df['fecha'].dt.date
print('\nVentas por Hora:')
ventas_hora = df.groupby('hora')['ventas'].sum().sort_values(ascending=False)
display(ventas_hora)    

# Ventas por día
ventas_diarias = df.groupby('dia')['ventas'].sum()
print('\nVentas por Día:')
display(ventas_diarias) 

# Calcular tendencia
tendencia = ventas_diarias.rolling(window=24).mean()    
print('\nTendencia de Ventas Diarias (Media Móvil de 24 horas):')

