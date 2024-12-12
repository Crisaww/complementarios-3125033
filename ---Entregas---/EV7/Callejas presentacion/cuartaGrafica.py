import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Cargar los datos del CSV
file_path = "datos_lenguajes.csv"
df = pd.read_csv(file_path)

# Variables independientes (x) y dependientes (y)
x = df["Nov 2023"]
y = df["Nov 2024"]

# Calcular la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color="blue", alpha=0.7, label="Datos reales")

# Dibujar la línea de regresión
plt.plot(x, intercept + slope * x, color="red", label=f"Línea de regresión (R²={r_value**2:.2f})")

# Añadir etiquetas y diseño
plt.title("Diagrama de Correlación Lineal: Lenguajes de Programación", fontsize=16)
plt.xlabel("Popularidad Nov 2023", fontsize=12)
plt.ylabel("Popularidad Nov 2024", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
