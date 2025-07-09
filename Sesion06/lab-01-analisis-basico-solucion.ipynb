{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Laboratorio 1: Análisis de Datos E-commerce (SOLUCIÓN)\n",
        "\n",
        "Este notebook contiene la solución completa del laboratorio de análisis de datos de e-commerce."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Importar bibliotecas necesarias\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from IPython.display import display\n",
        "\n",
        "# Configurar visualización\n",
        "plt.style.use('Solarize_Light2')\n",
        "%matplotlib inline\n",
        "plt.rcParams['figure.figsize'] = [10, 6]\n",
        "sns.set_palette('husl')\n",
        "\n",
        "# Configurar pandas\n",
        "pd.set_option('display.max_columns', None)\n",
        "pd.set_option('display.float_format', lambda x: '%.2f' % x)\n",
        "\n",
        "print('Ambiente configurado correctamente')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 1. Exploración Inicial\n",
        "\n",
        "Primero cargaremos y exploraremos los datos de ventas."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Crear dataset de ejemplo\n",
        "np.random.seed(42)\n",
        "data = {\n",
        "    'fecha': pd.date_range('2024-01-01', periods=1000, freq='H'),\n",
        "    'producto': np.random.choice(['Laptop', 'Smartphone', 'Tablet', 'Auriculares'], 1000),\n",
        "    'categoria': np.random.choice(['Electrónica', 'Accesorios'], 1000),\n",
        "    'precio': np.random.uniform(100, 1000, 1000).round(2),\n",
        "    'cantidad': np.random.randint(1, 5, 1000),\n",
        "    'canal': np.random.choice(['Online', 'Tienda'], 1000)\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# Exploración inicial\n",
        "print('Primeras 5 filas del DataFrame:')\n",
        "display(df.head())\n",
        "\n",
        "print('\\nInformación del DataFrame:')\n",
        "df.info()\n",
        "\n",
        "print('\\nEstadísticas descriptivas:')\n",
        "display(df.describe())\n",
        "\n",
        "print('\\nValores únicos por columna:')\n",
        "for col in ['producto', 'categoria', 'canal']:\n",
        "    print(f'\\n{col.title()}:')\n",
        "    display(df[col].value_counts())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 2. Análisis de Ventas\n",
        "\n",
        "Calculamos métricas de ventas y creamos visualizaciones básicas."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Calcular ventas\n",
        "df['ventas'] = df['precio'] * df['cantidad']\n",
        "\n",
        "# Métricas generales\n",
        "metricas = {\n",
        "    'Ventas Totales': df['ventas'].sum(),\n",
        "    'Ticket Promedio': df['ventas'].mean(),\n",
        "    'Número de Transacciones': len(df),\n",
        "    'Cantidad Total Vendida': df['cantidad'].sum()\n",
        "}\n",
        "\n",
        "print('Métricas Generales:')\n",
        "metricas_df = pd.DataFrame(metricas.items(), columns=['Métrica', 'Valor'])\n",
        "metricas_df['Valor'] = metricas_df['Valor'].round(2)\n",
        "display(metricas_df)\n",
        "\n",
        "# Análisis por categoría\n",
        "print('\\nVentas por Categoría:')\n",
        "ventas_categoria = df.groupby('categoria').agg({\n",
        "    'ventas': ['sum', 'mean', 'count'],\n",
        "    'cantidad': 'sum'\n",
        "}).round(2)\n",
        "display(ventas_categoria)\n",
        "\n",
        "# Top productos\n",
        "print('\\nTop Productos por Ventas:')\n",
        "display(df.groupby('producto')['ventas'].sum().sort_values(ascending=False))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Visualizaciones de ventas\n",
        "fig, axes = plt.subplots(2, 2, figsize=(15, 12))\n",
        "\n",
        "# 1. Ventas por categoría\n",
        "sns.barplot(data=df, x='categoria', y='ventas', estimator='sum', ax=axes[0,0])\n",
        "axes[0,0].set_title('Ventas Totales por Categoría')\n",
        "axes[0,0].set_ylabel('Ventas ($)')\n",
        "\n",
        "# 2. Distribución por producto\n",
        "df.groupby('producto')['ventas'].sum().plot(kind='pie', autopct='%1.1f%%', ax=axes[0,1])\n",
        "axes[0,1].set_title('Distribución de Ventas por Producto')\n",
        "\n",
        "# 3. Histograma de ventas\n",
        "sns.histplot(data=df, x='ventas', bins=30, ax=axes[1,0])\n",
        "axes[1,0].set_title('Distribución de Montos de Venta')\n",
        "axes[1,0].set_xlabel('Monto de Venta ($)')\n",
        "\n",
        "# 4. Box plot de precios\n",
        "sns.boxplot(data=df, x='categoria', y='precio', ax=axes[1,1])\n",
        "axes[1,1].set_title('Distribución de Precios por Categoría')\n",
        "axes[1,1].set_ylabel('Precio ($)')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 3. Análisis Temporal\n",
        "\n",
        "Analizamos patrones y tendencias en el tiempo."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Análisis temporal\n",
        "df['hora'] = df['fecha'].dt.hour\n",
        "df['dia'] = df['fecha'].dt.date\n",
        "\n",
        "# Ventas por día\n",
        "ventas_diarias = df.groupby('dia')['ventas'].sum()\n",
        "\n",
        "# Calcular tendencia\n",
        "tendencia = ventas_diarias.rolling(window=24).mean()\n",
        "\n",
        "# Visualizar tendencia\n",
        "plt.figure(figsize=(15, 6))\n",
        "plt.plot(ventas_diarias.index, ventas_diarias.values, label='Ventas diarias', alpha=0.5)\n",
        "plt.plot(tendencia.index, tendencia.values, label='Tendencia (24 horas)', linewidth=2)\n",
        "plt.axhline(y=ventas_diarias.mean(), color='r', linestyle='--', label='Promedio')\n",
        "\n",
        "plt.title('Tendencia de Ventas')\n",
        "plt.xlabel('Fecha')\n",
        "plt.ylabel('Ventas ($)')\n",
        "plt.legend()\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Análisis por hora y canal\n",
        "# Ventas por hora\n",
        "ventas_hora = df.groupby('hora')['ventas'].agg(['mean', 'sum', 'count']).round(2)\n",
        "print('Análisis de ventas por hora:')\n",
        "display(ventas_hora)\n",
        "\n",
        "# Ventas por canal\n",
        "ventas_canal = df.groupby(['canal', 'producto'])['ventas'].sum().unstack()\n",
        "print('\\nVentas por canal y producto:')\n",
        "display(ventas_canal)\n",
        "\n",
        "# Visualizar distribución por canal\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.boxplot(data=df, x='canal', y='ventas')\n",
        "plt.title('Distribución de Ventas por Canal')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 4. Análisis de Correlaciones"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Matriz de correlación\n",
        "variables_numericas = ['precio', 'cantidad', 'ventas', 'hora']\n",
        "correlaciones = df[variables_numericas].corr()\n",
        "\n",
        "# Visualizar correlaciones\n",
        "plt.figure(figsize=(10, 8))\n",
        "sns.heatmap(correlaciones, annot=True, cmap='coolwarm', center=0)\n",
        "plt.title('Matriz de Correlación - Variables Numéricas')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# Correlaciones más importantes\n",
        "print('\\nCorrelaciones más significativas:')\n",
        "corr_flat = correlaciones.unstack()\n",
        "corr_ord = corr_flat[corr_flat != 1.0].abs().sort_values(ascending=False)\n",
        "display(corr_ord.head())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 5. Conclusiones\n",
        "\n",
        "### Principales Hallazgos:\n",
        "\n",
        "1. **Métricas Clave de Ventas**\n",
        "   - Se analizaron {len(df)} transacciones\n",
        "   - Ventas totales: ${df['ventas'].sum():,.2f}\n",
        "   - Ticket promedio: ${df['ventas'].mean():,.2f}\n",
        "\n",
        "2. **Patrones por Categoría**\n",
        "   - La categoría más vendida fue {df.groupby('categoria')['ventas'].sum().idxmax()}\n",
        "   - El producto más vendido fue {df.groupby('producto')['ventas'].sum().idxmax()}\n",
        "\n",
        "3. **Patrones Temporales**\n",
        "   - Se identificaron picos de venta en determinadas horas\n",
        "   - La tendencia general muestra {tendencia.diff().mean() > 0 and 'crecimiento' or 'decrecimiento'}\n",
        "\n",
        "4. **Patrones por Canal**\n",
        "   - El canal dominante es {df.groupby('canal')['ventas'].sum().idxmax()}\n",
        "   - Existen diferencias significativas entre canales\n",
        "\n",
        "### Recomendaciones:\n",
        "\n",
        "1. Optimizar el inventario basado en patrones de venta\n",
        "2. Desarrollar estrategias específicas por canal\n",
        "3. Aprovechar las horas pico identificadas\n",
        "4. Implementar promociones basadas en datos"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": ".venv",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.12.1"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}
