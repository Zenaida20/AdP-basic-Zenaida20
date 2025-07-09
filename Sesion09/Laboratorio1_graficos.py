import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('datos/produccion_historica.csv')
df['fecha'] = pd.to_datetime(df['fecha'])

# Crear visualización simple
plt.figure(figsize=(10, 6))
for pozo in df['pozo'].unique():
    datos_pozo = df[df['pozo'] == pozo]
    plt.plot(datos_pozo['fecha'], datos_pozo['barriles_diarios'], label=pozo)

plt.title('Producción Diaria por Pozo')
plt.xlabel('Fecha')
plt.ylabel('Barriles por Día')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()