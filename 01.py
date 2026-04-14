import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

columnas = df[["gender", "lunch", "math score"]]

print(columnas.head(12))
print(columnas.tail(8))