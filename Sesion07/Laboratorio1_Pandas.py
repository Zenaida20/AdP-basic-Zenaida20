import pandas as pd
import numpy as np
print(pd.__version__)

# Crear un DataFrame para una empresa de ventas
# Crear un DataFrame con datos de clientes
clientes = pd.DataFrame({
    'empresa': ['Tech Corp', 'Finance Ltd', 'Retail SA', 'Energy Co', 'Health Inc'],
    'sector': ['Tecnología', 'Finanzas', 'Retail', 'Energía', 'Salud'],
    'facturacion_anual': [250000, 180000, 320000, 290000, 195000],
    'proyectos_activos': [3, 2, 5, 4, 2],
    'años_relacion': [2, 5, 1, 3, 4]
})

# 1. Visualizar el DataFrame
print("Portfolio de Clientes:")
print(clientes)

# 2. Calcular métricas clave
clientes['facturacion_por_proyecto'] = (
    clientes['facturacion_anual'] / clientes['proyectos_activos']
)

# 3. Identificar clientes VIP (facturación > 200k)
clientes['es_vip'] = clientes['facturacion_anual'] > 200000

print("\nAnálisis del Portfolio:")
print(clientes[['empresa', 'facturacion_por_proyecto', 'es_vip']])
# 4. Filtrar por columna
clientes_vip = clientes[clientes['es_vip']]
print("\nClientes VIP:")
print(clientes_vip[['empresa', 'facturacion_anual']])

