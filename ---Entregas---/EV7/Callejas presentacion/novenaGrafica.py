import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
data = pd.read_csv('interes_de_python_linea_del_tiempo.csv')

# Convertir la columna 'Mes' a formato de fecha
data['Mes'] = pd.to_datetime(data['Mes'], format='%Y-%m')

# Crear una nueva columna con el año
data['Año'] = data['Mes'].dt.year

# Realizar un gráfico de correlación lineal entre 'Año' y 'Popularidad'
plt.figure(figsize=(12, 6))
sns.regplot(x='Año', y='Popularidad', data=data, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title('Correlación Lineal entre el Año y la Popularidad de Python en Colombia', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Popularidad de Python en Colombia', fontsize=12)
plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para mayor claridad
plt.tight_layout()  # Ajustar el espacio para que las etiquetas no se solapen
plt.show()
