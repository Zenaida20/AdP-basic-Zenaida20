import pandas as pd
import numpy as np

# Ejemplo a trabajar: Datos del proyectos de consultoría
proyectos = pd.DataFrame({
    'proyecto_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'cliente': ['Empresa A', 'Empresa B', 'Empresa A', 'Empresa C', 'Empresa B', 'Empresa D'],
    'presupuesto': [50000, 75000, 30000, 120000, 45000, 90000],
    'duracion_dias': [30, 45, 20, 60, 25, 50],
    'estado': ['Completado', 'En Progreso', 'Completado', 'Retrasado', 'En Progreso', 'Completado'],
    'region': ['Norte', 'Sur', 'Norte', 'Centro', 'Sur', 'Norte']
})
print("Datos de Proyectos:")
print(proyectos)

# Ejercicio 1: Filtrar proyectos con presupuesto mayor a 60000
filtro_presupuestos = proyectos['presupuesto'] > 60000
filtro_estados = proyectos['estado'].isin(['Completado', 'En Progreso'])
filtro_presupuestos_estados = proyectos[filtro_presupuestos & filtro_estados]
print("\nProyectos con presupuesto mayor a 60000 y estado 'Completado' o 'En Progreso':")
print(filtro_presupuestos_estados)

# Ejercicio 2: Uso de isin()
# Parte 1. Filtrar proyectos de las regiones Norte o Centro y pertenecientes a Empresa A o Empresa C
# Respuesta 1:
filtro_regiones = proyectos['region'].isin(['Norte', 'Centro'])
filtro_clientes = proyectos['cliente'].isin(['Empresa A', 'Empresa C'])
filtro_regiones_clientes = proyectos[filtro_regiones & filtro_clientes]
print("\nProyectos de las regiones Norte o Centro y pertenecientes a Empresa A o Empresa C:")
print(filtro_regiones_clientes)


# Parte 2. Buscara a que empresa prertenecen las Empresa A o Empresa C
# Respuesta 2:
filtro_empresas = proyectos['cliente'].isin(['Empresa A', 'Empresa C'])
filtro_empresas_resultado = proyectos[filtro_empresas]
print("\nProyectos pertenecientes a Empresa A o Empresa C:")
print(filtro_empresas_resultado)

# Ejercicio 3: Filtrado con Negación Se deben buscar proyectos que:
# Parte 1: NO estén completados
# Respuesta 1:      
filtro_no_completados = proyectos['estado'] != 'Completado'
resultados_filtro_no_completados = proyectos[filtro_no_completados]
print("\nProyectos que NO están completados:")
print(resultados_filtro_no_completados) 

# 2. Y NO sean de la región Sur
# Respuesta 2:
filtro_no_sur = ~proyectos['region'].isin(['Sur'])
filtro_no_sur_resultado = proyectos[filtro_no_completados & filtro_no_sur]
print("\nProyectos que NO están completados y NO son de la región Sur:")
print(filtro_no_sur_resultado)           

# ejercicio 3: filtrado con negación
filtro_no_completados = proyectos[~(proyectos['estado'] == 'Completado')]
filtro_no_sur = proyectos[~(proyectos['region'] == 'Sur')]
filtro_combinado_negacion = filtro_no_completados & filtro_no_sur
print("Proyectos que no están Completados y no son de la región Sur:")
print(proyectos[filtro_combinado_negacion])