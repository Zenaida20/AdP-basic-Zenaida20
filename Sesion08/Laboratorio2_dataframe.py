import pandas as pd
import numpy as np

# Dataset de empleados para consultoría
empleados = pd.DataFrame({
    'empleado_id': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008'],
    'nombre': ['Ana García', 'Carlos López', 'María Rodriguez', 'Juan Pérez', 
               'Laura Martín', 'Pedro Sánchez', 'Sofia Hernández', 'Diego Torres'],
    'departamento': ['Consultoría', 'IT', 'Consultoría', 'Finanzas', 'IT', 'Consultoría', 'Finanzas', 'IT'],
    'salario': [65000, 70000, 62000, 75000, 68000, 67000, 72000, 69000],
    'antiguedad': [3, 5, 2, 7, 4, 6, 3, 1],
    'evaluacion': [8.5, 9.2, 7.8, 9.0, 8.8, 8.2, 9.1, 7.5],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona']
})

# Configurar índice personalizado
empleados.set_index('empleado_id', inplace=True)
print(empleados.head())

#Ejercicio 1: Selección Específica
# TODO: Usando loc, selecciona:

# Parte 1. Empleados E002, E004, E006
empleados_seleccionados = empleados.loc[['E002', 'E004', 'E006']]
print("\nEmpleados seleccionados (E002, E004, E006):")
print(empleados_seleccionados)

# Parte 2. Solo las columnas: nombre, departamento, salario
empleados_seleccionados_columnas = empleados_seleccionados[['nombre', 'departamento', 'salario']]
print("\nEmpleados seleccionados con columnas específicas (nombre, departamento, salario):")
print(empleados_seleccionados_columnas)

# Ejercicio 2: Selección Condicional
# TODO: Encuentra empleados que:

# Parte 1. Trabajen en Madrid O Barcelona
empleados_madrid_barcelona = empleados[empleados['ciudad'].isin(['Madrid', 'Barcelona'])]
print("\nEmpleados que trabajan en Madrid o Barcelona:")
print(empleados_madrid_barcelona)

# Parte 2. Tengan evaluación >= 8.0
empleados_evaluacion_alta = empleados[empleados['evaluacion'] >= 8.0]
print("\nEmpleados con evaluación >= 8.0:")
print(empleados_evaluacion_alta)

# Parte 3. Muestren solo: nombre, ciudad, evaluacion, salario
empleados_evaluacion_alta_columnas = empleados_evaluacion_alta[['nombre', 'ciudad', 'evaluacion', 'salario']]
print("\nEmpleados con evaluación >= 8.0 y columnas específicas (nombre, ciudad, evaluacion, salario):")
print(empleados_evaluacion_alta_columnas)

# Ejercicio 3: Análisis con iloc
# TODO: Usando iloc:
# Parte 1. Selecciona los últimos 3 empleados
ultimos_3_empleados = empleados.iloc[-3:]
print("\nÚltimos 3 empleados:")
print(ultimos_3_empleados)
    
# Parte 2. Solo las primeras 4 columnas
ultimos_columnas_empleados = ultimos_3_empleados.iloc[:, :4]
print("\nÚltimos 3 empleados con las primeras 4 columnas:")
print(ultimos_columnas_empleados)



