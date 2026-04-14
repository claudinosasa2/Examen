import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

primeras_2 = df.iloc[:, :2]
print("Primeras 2 columnas:")
print(primeras_2)

print("Tipos de datos:")
print(df.dtypes)

print("Últimas 10 filas:")
print(df.tail(10))