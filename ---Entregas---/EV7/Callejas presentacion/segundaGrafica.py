import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Datos ajustados cargados en el CSV
file_path = 'metricas_arquitectura_software.csv'
df = pd.read_csv(file_path)

# Asegurarse de que las columnas sean numéricas
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

# Crear las variables para la regresión lineal
x = range(1, len(df) + 1)  # Índices de las métricas como eje X
y = df['Valor']  # Valores numéricos como eje Y

# Calcular la línea de regresión
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='lightblue', label='Datos')
plt.plot(x, intercept + slope * np.array(x), color='red', label='Línea de regresión')

# Etiquetas y diseño
plt.title("Regresión Lineal - Métricas de Arquitectura", fontsize=16)
plt.xlabel("Índice de Métricas", fontsize=12)
plt.ylabel("Valores", fontsize=12)
plt.xticks(ticks=x, labels=df['Métrica'], rotation=45, ha='right')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Mostrar la gráfica
plt.show()
