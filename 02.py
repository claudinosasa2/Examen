import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

ultimas_3 = df.iloc[:, -3:]
print("Últimas 3 columnas:")
print(ultimas_3)

vacios = df.isnull()

print("¿Hay valores vacíos?")
print(vacios.any())

print("Cantidad de valores vacíos por columna:")
print(df.isnull().sum())

ultima_columna = df.columns[-1]
print("Última columna:", ultima_columna)
print("Tipo de dato:", df[ultima_columna].dtype)