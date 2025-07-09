import pandas as pd
import numpy as np
print(pd.__version__)

# Dataset de proyectos
proyectos = pd.DataFrame({
    'codigo': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'cliente': ['Tech Corp', 'Finance Ltd', 'Retail SA', 'Tech Corp', 'Energy Co'],
    'consultor_lead': ['C001', 'C003', 'C002', 'C004', 'C005'],
    'presupuesto': [75000, 120000, 45000, 95000, 150000],
    'estado': ['Activo', 'Completado', 'Activo', 'Activo', 'Planificado']
})

# 1. Proyectos activos
activos = proyectos[proyectos['estado'] == 'Activo']
print("Proyectos activos:")
print(activos)

# 2. Proyectos de alto valor (>80k) de Tech Corp
tech_alto_valor = proyectos[
    (proyectos['cliente'] == 'Tech Corp') & 
    (proyectos['presupuesto'] > 80000)
]
print("\nProyectos Tech Corp > 80k:")
print(tech_alto_valor)

# 3. Información del consultor lead para proyectos activos
info_leads = proyectos.loc[
    proyectos['estado'] == 'Activo',
    ['codigo', 'consultor_lead', 'presupuesto']
]
print("\nConsultores lead de proyectos activos:")
print(info_leads)

# 4. Resumen de proyectos por cliente
resumen_clientes = proyectos.groupby('cliente').agg({
    'presupuesto': ['sum', 'mean'],
    'estado': 'count'
}).reset_index()
resumen_clientes.columns = ['cliente', 'presupuesto_total', 'presupuesto_promedio', 'numero_proyectos']
print("\nResumen de proyectos por cliente:")
print(resumen_clientes)
# 5. Proyectos con presupuesto mayor al promedio
presupuesto_promedio = proyectos['presupuesto'].mean()
proyectos_mayor_promedio = proyectos[proyectos['presupuesto'] > presupuesto_promedio]
print("\nProyectos con presupuesto mayor al promedio:")
print(proyectos_mayor_promedio[['codigo', 'cliente', 'presupuesto']])
# 6. Proyectos por estado
proyectos_por_estado = proyectos['estado'].value_counts().reset_index()
proyectos_por_estado.columns = ['estado', 'cantidad']
print("\nCantidad de proyectos por estado:")
print(proyectos_por_estado)
