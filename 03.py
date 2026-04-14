import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

reading = df["reading score"]

print("Columna reading score:")
print(reading)

print("Cantidad de datos:", reading.count())

print("Suma total:", reading.sum())