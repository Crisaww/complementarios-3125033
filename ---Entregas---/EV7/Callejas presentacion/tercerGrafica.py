import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo CSV
df = pd.read_csv("resultados_encuesta.csv")

# Crear una gráfica de barras horizontales
plt.figure(figsize=(10, 6))
plt.barh(df["Pregunta"], df["Resultado (%)"], color="skyblue")

# Configurar título y etiquetas
plt.title("Resultados de la Encuesta sobre la Industria de Software", fontsize=16)
plt.xlabel("Porcentaje (%)", fontsize=12)
plt.ylabel("Preguntas", fontsize=12)

# Mostrar valores en las barras
for index, value in enumerate(df["Resultado (%)"]):
    plt.text(value + 1, index, str(value), va='center', fontsize=10)

# Ajustar diseño y mostrar la gráfica
plt.tight_layout()
plt.show()
