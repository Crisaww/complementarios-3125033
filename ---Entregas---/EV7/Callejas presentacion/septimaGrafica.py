import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Cargar el archivo CSV
file_path = "herramientas_mas_utilizadas_en_2024.csv"  # Guarda el archivo con este nombre
data = pd.read_csv(file_path)

# Variables independientes y dependientes
x = data["Usage Index"]
y = data["Porcentaje"]

# Calcular la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.7, label="Datos reales")
plt.plot(x, slope * x + intercept, color='red', label=f"Línea de regresión (R²={r_value**2:.2f})")

# Etiquetas y título
plt.title("Diagrama de Correlación Lineal: Herramientas y Popularidad", fontsize=16)
plt.xlabel("Índice de Uso", fontsize=12)
plt.ylabel("Porcentaje de Popularidad (%)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
