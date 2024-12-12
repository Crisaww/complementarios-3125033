import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = 'ai_ml_language_popularity.csv'
data = pd.read_csv(file_path)

# Crear la gráfica de líneas
plt.figure(figsize=(10, 6))
plt.plot(data['Language'], data['Percentage'], marker='o', color='skyblue', linestyle='-', alpha=0.7)
plt.title('Popularidad de Lenguajes en AI/ML', fontsize=16)
plt.xlabel('Lenguajes de Programación', fontsize=12)
plt.ylabel('Porcentaje de Uso (%)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Mostrar la gráfica
plt.show()
