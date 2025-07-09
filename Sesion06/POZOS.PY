#Crear un arreglo con la produccion total de cada pozo en la semana
import numpy as np
#Pozo No 1
pozo1 = np.array([120, 130, 125, 140, 135, 128, 132])

# Pozo No 2 
pozo2 = np.array([110, 115, 118, 120, 122, 119, 121])

# Pozo No 3
pozo3 = np.array([150, 155, 160, 158, 162, 159, 161])

#Array con Producción Total
total_pozo1 = np.sum(pozo1)
total_pozo2 = np.sum(pozo2)
total_pozo3 = np.sum(pozo3)

produccion_total_de_la_semana = np.array ([total_pozo1, total_pozo2, total_pozo3])

# Mostrar resultados 
print(produccion_total_de_la_semana)

# Si quieres un arreglo con todos los pozos (cada fila es un pozo, cada columna un día)
pozos = np.array([pozo1, pozo2, pozo3])

# Precio promedio del petróleo para cada pozo
precio_petroleo = np.array([78, 80, 83])  # Un precio para cada pozo

# Ingresos de Petróleo por pozo (total semanal)
ingresos = produccion_total_de_la_semana * precio_petroleo
print("ingreso_por_pozo:", ingresos)

# Ingreso total de Petróleo
ingreso_total = np.sum(ingresos)
print("ingreso_total:", ingreso_total)

# Calcular producción semanal por pozo (ya está en produccion_total_de_la_semana)
print("Producción semanal por pozo:", produccion_total_de_la_semana)

# Calcular los ingresos diarios por pozo
ingresos_semanales = pozos * precio_petroleo[:, np.newaxis]  # Multiplica cada fila por su precio

# Día con mayor ingreso por pozo (1-7)
dias = np.argmax(ingresos_semanales, axis=1) + 1
print("Día con mayor ingreso por pozo:", dias)