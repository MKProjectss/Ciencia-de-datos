# Cargano librerías matplotlib, pandas
import matplotlib.pyplot as plt
import pandas as pd

# Leyendo datos del archivo "datos.csv"
data = pd.read_csv ("datos/datos.csv")

# Visualizando las primeras 5 líneas de los datos cargados
print(data.head ())

# Graficando variables
data.plot(x ='year', y='natality', kind = 'line')
plt.show()
