import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
data = pd.read_csv("tendencia_de_los_lenguajes_de_programacion_a_lo_largo_del_tiempo.csv")

# Mostrar las primeras filas para verificar el contenido
print(data.head())

# Convertir la columna 'Year' a tipo datetime para un mejor manejo
data['Year'] = pd.to_datetime(data['Year'], format='%m/%d/%Y')

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar las tres columnas de programación
plt.plot(data['Year'], data['Python'], label='Python', marker='o')
plt.plot(data['Year'], data['Java'], label='Java', marker='o')
plt.plot(data['Year'], data['C++'], label='C++', marker='o')

# Etiquetas y título
plt.title('Uso de Lenguajes de Programación a lo Largo del Tiempo')
plt.xlabel('Año')
plt.ylabel('Porcentaje de Uso')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para que no se sobrepongan
plt.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
