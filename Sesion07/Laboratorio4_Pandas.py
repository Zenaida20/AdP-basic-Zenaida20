# Instalar dependencias necesarias

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Lectura simple


# Con hoja específica


# Preparar datos de ejemplo
import pandas as pd
import os

# Crear un archivo Excel con múltiples hojas
with pd.ExcelWriter('datos/encuestas_satisfaccion.xlsx', engine='openpyxl') as writer:
    # Hoja 1: Resultados
    resultados = pd.DataFrame({
        'cliente': ['Tech Corp', 'Finance Ltd', 'Retail SA', 'Energy Co', 'Health Inc'],
        'proyecto': ['P001', 'P002', 'P003', 'P004', 'P005'],
        'satisfaccion_general': [4.5, 4.2, 4.8, 3.9, 4.6],
        'calidad_entrega': [4.6, 4.3, 4.9, 4.0, 4.5],
        'comunicacion': [4.4, 4.1, 4.7, 3.8, 4.7],
        'valor_precio': [4.5, 4.2, 4.8, 3.9, 4.6],
        'fecha_encuesta': pd.date_range('2024-01-01', periods=5, freq='W')
    })
    resultados.to_excel(writer, sheet_name='Resultados', index=False)

    # Hoja 2: Preguntas
    preguntas = pd.DataFrame({
        'id_pregunta': ['Q1', 'Q2', 'Q3', 'Q4'],
        'categoria': ['General', 'Calidad', 'Comunicación', 'Valor'],
        'pregunta': [
            '¿Qué tan satisfecho está con el proyecto en general?',
            '¿Cómo califica la calidad de los entregables?',
            '¿Cómo evalúa la comunicación del equipo?',
            '¿Considera que recibió valor por su inversión?'
        ],
        'escala': ['1-5', '1-5', '1-5', '1-5']
    })
    preguntas.to_excel(writer, sheet_name='Preguntas', index=False)

print("Archivo 'encuestas_satisfaccion.xlsx' creado exitosamente")

# Crear Excel con celdas combinadas (simulado)
reporte_regional = pd.DataFrame({
    'Region': ['Norte', 'Norte', 'Norte', 'Sur', 'Sur', 'Sur'],
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo'],
    'Ventas': [120000, 135000, 140000, 95000, 105000, 115000],
    'Gastos': [80000, 85000, 82000, 70000, 72000, 75000],
    'Utilidad': [40000, 50000, 58000, 25000, 33000, 40000]
})

reporte_regional.to_excel('datos/reporte_regional.xlsx', index=False)

# Leer y procesar
df_regional = pd.read_excel('datos/reporte_regional.xlsx')

# Agrupar por región para manejar datos jerárquicos
resumen_regional = df_regional.groupby('Region').agg({
    'Ventas': 'sum',
    'Gastos': 'sum',
    'Utilidad': 'sum'
})
print("\nResumen por región:")
print(resumen_regional)

# Guardar el resumen en un nuevo archivo Excel
resumen_regional.to_excel('datos/resumen_regional.xlsx')
# Leer el archivo Excel con múltiples hojas
df_encuestas = pd.read_excel('datos/encuestas_satisfaccion.xlsx', sheet_name='Resultados')
print("\nDatos de encuestas de satisfacción:")
print(df_encuestas)
# Filtrar datos por satisfacción general mayor a 4.5
df_satisfaccion_alta = df_encuestas[df_encuestas['satisfaccion_general'] > 4.5]
print("\nDatos de encuestas con satisfacción general mayor a 4.5:")
print(df_satisfaccion_alta)


