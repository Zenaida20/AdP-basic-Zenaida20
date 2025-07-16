# Archivo: lab_01_indexacion_multinivel.py
"""
Laboratorio 1: Indexación Multinivel y Jerarquías
Objetivo: Dominar las técnicas de indexación multinivel y operaciones jerárquicas
          con DataFrames para análisis avanzado de datos petroleros.

Este laboratorio utiliza datos del archivo pozos_multinivel.csv
"""
import pandas as pd
import numpy as np
from datetime import datetime       

def main():
    # Cargar datos de ejemplo
    try:
        df_pozos = pd.read_csv('datos/pozos_multinivel.csv')
        print("Datos cargados exitosamente")
        print(f"Forma del DataFrame: {df_pozos.shape}")
        print(f"Columnas: {list(df_pozos.columns)}")
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'datos/pozos_multinivel.csv'")
        return
    except ImportError as e:
        print("Error de importación:", e)
        print("Asegúrate de instalar pandas y numpy con: pip install pandas numpy")
        return
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return

    print("\n=== Laboratorio 1: Indexación Multinivel y Jerarquías ===\n")

    # Validar columnas necesarias
    columnas_necesarias = {'campo', 'pozo', 'fecha', 'produccion_diaria', 'presion_cabeza', 'agua_cut'}
    if not columnas_necesarias.issubset(df_pozos.columns):
        print(f"Error: El archivo debe contener las columnas: {columnas_necesarias}")
        return

    # EJERCICIO 1: Crear MultiIndex jerárquico
    print("Ejercicio 1: Crear MultiIndex jerárquico")
    df_multi = df_pozos.copy()
    df_multi['fecha'] = pd.to_datetime(df_multi['fecha'], errors='coerce')
    df_multi = df_multi.set_index(['campo', 'pozo', 'fecha'])

    print(f"Forma del DataFrame con MultiIndex: {df_multi.shape}")
    print("Niveles del MultiIndex:")
    for i, level in enumerate(df_multi.index.names):
        print(f"  Nivel {i}: {level}")
    print("\nPrimeras filas del DataFrame con MultiIndex:")
    print(df_multi.head())

    print("\n" + "-"*50 + "\n")

    # EJERCICIO 2: Selección jerárquica avanzada
    print("Ejercicio 2: Selección jerárquica avanzada")
    try:
        campo_libertad = df_multi.loc['Campo Libertad']
        pozo_lib001 = df_multi.loc[('Campo Libertad', 'LIB-001')]
        fecha_especifica = df_multi.loc[('Campo Libertad', 'LIB-001', pd.Timestamp('2024-01-01'))]

        print("a) Datos del Campo Libertad:")
        print(f"   Filas: {len(campo_libertad)}")
        print(f"   Pozos únicos: {campo_libertad.index.get_level_values('pozo').unique()}")

        print("\nb) Datos del pozo LIB-001 en Campo Libertad:")
        print(f"   Filas: {len(pozo_lib001)}")
        print(f"   Fechas: {list(pozo_lib001.index.get_level_values('fecha'))}")

        print("\nc) Datos específicos de fecha:")
        print(f"   Producción diaria: {fecha_especifica['produccion_diaria']} BPD")
        print(f"   Presión de cabeza: {fecha_especifica['presion_cabeza']} PSI")
    except KeyError as e:
        print(f"Advertencia: No se encontró el valor en el índice: {e}")

    print("\n" + "-"*50 + "\n")

    # EJERCICIO 3: Operaciones por niveles del MultiIndex
    print("Ejercicio 3: Operaciones por niveles del MultiIndex")
    produccion_por_campo = df_multi.groupby(level='campo')['produccion_diaria'].mean()
    produccion_por_pozo = df_multi.groupby(level=['campo', 'pozo'])['produccion_diaria'].mean()
    mejor_pozo_por_campo = df_multi.groupby(level='campo')['produccion_diaria'].agg(['mean', 'idxmax'])

    print("a) Producción promedio por campo:")
    for campo, produccion in produccion_por_campo.items():
        print(f"   {campo}: {produccion:.2f} BPD")

    print("\nb) Producción promedio por pozo:")
    for (campo, pozo), produccion in produccion_por_pozo.items():
        print(f"   {campo} - {pozo}: {produccion:.2f} BPD")

    print("\nc) Mejor pozo por campo:")
    for campo in df_multi.index.get_level_values('campo').unique():
        try:
            mejor_idx = mejor_pozo_por_campo.loc[campo, 'idxmax']
            mejor_pozo = mejor_idx[1]  # El pozo está en el segundo nivel
            mejor_produccion = mejor_pozo_por_campo.loc[campo, 'mean']
            print(f"   {campo}: {mejor_pozo} ({mejor_produccion:.2f} BPD)")
        except Exception as e:
            print(f"   {campo}: Error al calcular mejor pozo ({e})")

    print("\n" + "-"*50 + "\n")

    # EJERCICIO 4: Reestructuración de datos (Pivot y Stack/Unstack)
    print("Ejercicio 4: Reestructuración de datos (Pivot y Stack/Unstack)")
    try:
        df_pivot = df_pozos.pivot_table(
            index='campo',
            columns='pozo',
            values='produccion_diaria',
            aggfunc='mean'
        )
        df_unstacked = df_multi['produccion_diaria'].unstack(level='pozo')
        df_stacked = df_unstacked.stack()

        print("a) Pivot table (producción promedio por campo y pozo):")
        print(df_pivot)
        print("\nb) DataFrame unstacked (pozos como columnas):")
        print(df_unstacked)
        print("\nc) DataFrame re-stacked:")
        print(df_stacked.head(10))
    except Exception as e:
        print(f"Error en reestructuración de datos: {e}")

    print("\n" + "-"*50 + "\n")

    # EJERCICIO 5: Análisis comparativo avanzado
    print("Ejercicio 5: Análisis comparativo avanzado")
    try:
        df_multi['eficiencia'] = df_multi['produccion_diaria'] / df_multi['agua_cut']
        eficiencia_por_campo = df_multi.groupby(level='campo')['eficiencia'].mean()
        variabilidad_pozos = df_multi.groupby(level=['campo', 'pozo'])['produccion_diaria'].agg(['mean', 'std'])
        variabilidad_pozos['coeficiente_variacion'] = variabilidad_pozos['std'] / variabilidad_pozos['mean']
        ranking_campos = df_multi.groupby(level='campo').agg({
            'produccion_diaria': ['mean', 'sum'],
            'eficiencia': 'mean',
            'agua_cut': 'mean'
        }).round(2)

        print("a) Eficiencia operacional por campo:")
        for campo, eficiencia in eficiencia_por_campo.items():
            print(f"   {campo}: {eficiencia:.2f} BPD/%")

        print("\nb) Pozos con mayor variabilidad (CV > 0.1):")
        pozos_variables = variabilidad_pozos[variabilidad_pozos['coeficiente_variacion'] > 0.1]
        for (campo, pozo), datos in pozos_variables.iterrows():
            print(f"   {campo} - {pozo}: CV = {datos['coeficiente_variacion']:.3f}")

        print("\nc) Ranking de campos por rendimiento:")
        print(ranking_campos)
    except Exception as e:
        print(f"Error en análisis comparativo: {e}")

    print("\n" + "-"*50 + "\n")

    # EJERCICIO 6: Operaciones condicionales con MultiIndex
    print("Ejercicio 6: Operaciones condicionales con MultiIndex")
    try:
        df_multi['sobre_promedio'] = df_multi.groupby(level='campo')['produccion_diaria'].transform(
            lambda x: x > x.mean()
        )
        df_multi['produccion_normalizada'] = df_multi.groupby(level='campo')['produccion_diaria'].transform(
            lambda x: (x - x.mean()) / x.std()
        )
        anomalias = df_multi[abs(df_multi['produccion_normalizada']) > 2]

        print("a) Pozos con producción sobre el promedio de su campo:")
        pozos_sobre_promedio = df_multi[df_multi['sobre_promedio'] == True]
        for (campo, pozo, fecha), datos in pozos_sobre_promedio.iterrows():
            print(f"   {campo} - {pozo} ({fecha}): {datos['produccion_diaria']} BPD")

        print(f"\nb) Estadísticas de normalización:")
        print(f"   Media: {df_multi['produccion_normalizada'].mean():.3f}")
        print(f"   Desv. Est.: {df_multi['produccion_normalizada'].std():.3f}")

        print(f"\nc) Anomalías detectadas: {len(anomalias)} registros")
        for (campo, pozo, fecha), datos in anomalias.iterrows():
            print(f"   {campo} - {pozo} ({fecha}): {datos['produccion_diaria']} BPD (z-score: {datos['produccion_normalizada']:.2f})")
    except Exception as e:
        print(f"Error en operaciones condicionales: {e}")

if __name__ == "__main__":
    main()